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
6. 선택한 로컬 폴더에 PNG와 `captures.csv` 이력이 저장됩니다.

## 3. 저장·보안

- 화면 캡처 및 파일 기록은 사용자 브라우저에서 실행하며 **GitHub로 업로드하지 않습니다.**
- 화면/창 공유 및 폴더 저장은 브라우저의 사용자 권한 허용이 필요합니다.
- 웹 브라우저 보안 때문에 기존 X11 프로그램처럼 PC의 전역 마우스 클릭을 추적하지 않습니다. 자동 촬영은 **화면 변화 감지** 방식입니다.
- 화면 공유 권한이 해제되거나 탭이 종료되면 화면 캡처가 중단됩니다.
- 촬영된 자료는 먼저 검증 전(`UNREVIEWED`) 상태로 관리합니다.

## 4. 저장소 파일

- `index.html`: 웹앱 전체 (단일 HTML)
- `.nojekyll`: Jekyll 빌드 비활성화
- `README.md`: 사용법

기존 SoC 실습 교재 저장소 `Yuul-Jung/soc`와 독립적으로 유지합니다.
