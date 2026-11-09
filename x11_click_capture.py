#!/usr/bin/env python3
"""X11 click-triggered local screenshots. Run only on your own desktop."""
import argparse
import csv
import hashlib
import os
import queue
import threading
import time
from datetime import datetime
from pathlib import Path

from mss import mss
from pynput import mouse

CSV_FIELDS = ["timestamp", "chapter", "step", "reason", "mode", "file", "sha256", "status"]


def main():
    parser = argparse.ArgumentParser(description="X11 mouse click capture (local only)")
    parser.add_argument("--output", default=str(Path.home() / "soc" / "evidence"))
    parser.add_argument("--chapter", type=int, default=1)
    parser.add_argument("--step", type=int, default=1)
    parser.add_argument("--delay", type=float, default=0.7, help="Seconds after last click/release")
    parser.add_argument("--interval", type=float, default=30, help="Periodic backup seconds; 0 disables")
    parser.add_argument("--monitor", type=int, default=1, help="mss monitor index; 0 means all")
    args = parser.parse_args()
    if os.environ.get("XDG_SESSION_TYPE", "").lower() != "x11":
        parser.error("This tool requires an X11 session.")
    if not 1 <= args.chapter <= 99 or not 1 <= args.step <= 999:
        parser.error("chapter must be 1..99 and step must be 1..999")
    if args.delay < 0 or args.interval < 0:
        parser.error("delay and interval must be non-negative")

    root = Path(args.output).expanduser().resolve()
    raw = root / f"ch{args.chapter:02d}" / f"step{args.step:02d}" / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    pending = queue.Queue()
    held = set()
    lock = threading.Lock()
    due_at = None
    last_capture = time.monotonic()
    stop = threading.Event()

    def on_click(x, y, button, pressed):
        nonlocal due_at
        with lock:
            if pressed:
                held.add(button)
                due_at = None
            else:
                held.discard(button)
                if not held:
                    due_at = time.monotonic() + args.delay

    def capture(reason):
        nonlocal last_capture
        now = datetime.now().astimezone()
        filename = (f"ch{args.chapter:02d}_step{args.step:02d}_"
                    f"{now:%Y%m%d_%H%M%S_%f}_{reason}.png")
        dest = raw / filename
        with mss() as sct:
            if args.monitor >= len(sct.monitors):
                raise ValueError(f"Monitor {args.monitor} unavailable; valid 0..{len(sct.monitors)-1}")
            sct.shot(mon=args.monitor, output=str(dest))
        digest = hashlib.sha256(dest.read_bytes()).hexdigest()
        relative = dest.relative_to(root).as_posix()
        csv_path = root / "captures_x11.csv"
        new_file = not csv_path.exists() or csv_path.stat().st_size == 0
        with csv_path.open("a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if new_file:
                writer.writerow(CSV_FIELDS)
            writer.writerow([now.isoformat(), args.chapter, args.step,
                             reason, "x11_monitor", relative, digest, "UNREVIEWED"])
        last_capture = time.monotonic()
        print(f"Saved {relative}", flush=True)

    print("X11 capture active. Ctrl+C to stop. Do not capture sensitive screens.", flush=True)
    with mouse.Listener(on_click=on_click) as listener:
        try:
            while not stop.is_set():
                time.sleep(0.08)
                with lock:
                    click_ready = due_at is not None and not held and time.monotonic() >= due_at
                    if click_ready:
                        due_at = None
                if click_ready:
                    capture("mouse_click")
                elif args.interval and time.monotonic() - last_capture >= args.interval:
                    capture("auto_periodic")
        except KeyboardInterrupt:
            print("Stopped.", flush=True)
        finally:
            listener.stop()


if __name__ == "__main__":
    main()
