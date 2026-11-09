# SoC Capture Web — 실습 화면 캡처

**독립 실행 주소:** https://yuul-jung.github.io/capture-web/

GitHub Pages에서 설치 없이 실행하는 브라우저 기반 Vivado/Vitis 화면 캡처 웹앱입니다. Python, PyQt5, X11 프로그램은 필요 없습니다.

## 1. GitHub Pages 최초 활성화

[저장소 Pages 설정](https://github.com/Yuul-Jung/capture-web/settings/pages)에서 한 번만 설정합니다.

1. **Build and deployment → Source**: `Deploy from a branch`
2. **Branch**: `main` / `(root)`
3. **Save** 클릭
4. 공개된 주소 `https://yuul-jung.github.io/capture-web/` 접속

GitHub 저장소에 `index.html`과 `.nojekyll`이 있으므로 별도 빌드 과정은 필요하지 않습니다.

## 2. 사용 방법

1. Ubuntu PC에서 Chrome 또는 Chromium으로 웹앱을 엽니다.
2. **저장 폴더 선택**에서 본인 PC에 캡처 결과를 저장할 폴더를 선택하고 접근 권한을 허용합니다.
3. **챕터 / STEP** 번호를 지정합니다.
4. **화면 공유 시작**을 눌러 Vivado/Vitis 창 또는 전체 화면을 선택합니다.
5. **현재 화면 PNG 저장**, **5초 후 촬영**, **자동 캡처 시작**, **영역 선택** 중 원하는 촬영 기능을 사용합니다.
   - 자동 캡처 방식: **화면 변화 감지 / 일정 주기 / 변화 + 일정 주기**
   - 촬영 간격: **4초, 6초, 10초, 30초, 1분, 5분**
   - 변화 감도와 화면 안정화 대기시간을 별도로 조정할 수 있습니다.
   - 자동 캡처 설정은 이 브라우저에 저장되어 다음 방문 시 복원됩니다.
6. 선택한 로컬 폴더에 PNG와 `captures.csv` 이력이 저장됩니다.

## 3. 저장·보안

- 화면 캡처 및 파일 기록은 사용자 브라우저에서 실행하며 **GitHub로 업로드하지 않습니다.**
- 화면/창 공유 및 폴더 저장은 브라우저의 사용자 권한 허용이 필요합니다.
- 웹 브라우저 보안 때문에 PC의 전역 마우스 클릭을 추적하지 않습니다. 클릭 등으로 생긴 화면 변화를 감지하거나 일정 주기로 촬영합니다.
- **일정 주기 모드**는 화면 변화가 없어도 촬영합니다. 장시간 사용 시 파일이 많이 쌓일 수 있습니다.
- 브라우저가 백그라운드에서 타이머를 지연시키거나 PC가 절전 상태에 들어가면 정확한 주기가 보장되지 않습니다.
- 화면 공유 권한이 해제되거나 탭이 종료되면 화면 캡처가 중단됩니다.
- 촬영된 자료는 먼저 검증 전(`UNREVIEWED`) 상태로 관리합니다.

## 4. 저장소 파일

- `index.html`: 웹앱 전체 (단일 HTML)
- `.nojekyll`: Jekyll 빌드 비활성화
- `README.md`: 사용법

기존 SoC 실습 교재 저장소 `Yuul-Jung/soc`와 독립적으로 유지합니다.

## 5. Ubuntu X11 전역 마우스 클릭 촬영 (별도 실행 도구)

`x11_click_capture.py`는 웹앱과 독립 실행되는 로컬 보조 프로그램입니다. X11 전역 마우스 버튼 놓기 이벤트 후 기본 0.7초 동안 추가 클릭이 없으면 전체 모니터를 PNG로 저장하고, 30초마다 보조 촬영합니다. 브라우저의 화면 공유나 저장 폴더 권한은 필요하지 않습니다.

```bash
# X11 여부 확인
echo "$XDG_SESSION_TYPE"

# 프로젝트 다운로드
git clone https://github.com/Yuul-Jung/capture-web.git
cd capture-web
git switch feature/capture-autosave-v2

# 독립 Python 환경 생성 및 X11 마우스 감지/스크린샷 라이브러리 설치
python3 -m venv .venv
.venv/bin/pip install pynput mss

# 전역 클릭 감지 및 캡처 실행
.venv/bin/python x11_click_capture.py --chapter 1 --step 1 --delay 0.7 --interval 30
```

기본 저장 위치는 `~/soc/evidence/ch01/step01/raw/`이며 이력은 별도 `captures_x11.csv`에 기록됩니다. 웹앱의 `captures.csv`와 스키마가 다르므로 혼합하지 않습니다. 중지하려면 터미널에서 Ctrl+C를 누릅니다.

**주의:** 전역 클릭이므로 캡처 앱 자체 클릭도 감지하며, 화면에 표시된 개인정보나 토큰이 촬영될 수 있습니다. 캡처 제외 창 설정과 웹앱 통합은 아직 구현하지 않았습니다. 이 도구는 X11 로컬 실행용이며 GitHub Pages에서 직접 실행되지 않습니다.

### X11 지정 영역 캡처

```bash
# 마우스로 영역의 대각선 두 모서리를 차례로 클릭하여 지정
.venv/bin/python x11_click_capture.py --select-region --interval 30

# 화면의 절대 좌표 X=200, Y=150부터 가로 1200, 세로 800 픽셀만 촬영
.venv/bin/python x11_click_capture.py --region 200 150 1200 800 --interval 30
```

영역 선택 단계에서는 마우스 **왼쪽 버튼으로 두 모서리를 차례로 클릭**합니다. 두 번째 클릭 후 자동 촬영 감지가 시작됩니다. 선택 범위는 전체 가상 데스크톱 안에 있어야 합니다. `--region`과 `--select-region`은 동시에 사용할 수 없습니다. `--monitor`는 전체 모니터 모드에만 적용됩니다. 지정 영역은 현재 실행 동안 유지되며 재실행 시 다시 선택해야 합니다.
