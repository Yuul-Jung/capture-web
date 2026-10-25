# SoC Capture Web — 독립 GitHub Pages

이 배포본은 `Yuul-Jung/capture-web` **독립 저장소의 최상위 폴더**에 올리도록 구성했습니다.

목표 URL: https://yuul-jung.github.io/capture-web/

- `index.html`: 독립 웹앱. 외부 JS/CSS 설치 없음
- `.nojekyll`: GitHub Pages가 Jekyll 빌드 처리하지 않도록 설정

## GitHub에서 배포

1. https://github.com/new 에서 계정 `Yuul-Jung`, 저장소 이름 `capture-web`, 공개(Public)로 새 저장소 생성
2. 이 ZIP을 풀어서 `index.html`, `.nojekyll`, `README.md`를 저장소의 **최상위(root)** 에 업로드
3. 저장소 **Settings → Pages** 에서 **Deploy from a branch → main / (root) → Save** 선택
4. 위 목표 URL로 접속

## 로컬 저장

Chrome/Chromium에서 페이지를 열고 사용자가 화면 공유와 저장 폴더 권한을 허용합니다.
브라우저가 선택한 폴더 아래에 장/단계별 PNG 및 captures.csv 파일을 생성합니다.
GitHub에는 사용자 캡처 이미지가 업로드되지 않습니다.

## 주의

기존 `Yuul-Jung/soc` 저장소의 교재 링크와 페이지는 변경하지 않습니다. 새 URL에 정상 게시된 것을 확인한 뒤, 예전 `soc/capture-web/`에는 새 URL로 이동하는 안내 또는 리디렉션을 둘 수 있습니다.

## Ubuntu에서 한번에 독립 저장소 게시하기 (선택)

GitHub CLI(명령줄 도구)가 없는 경우 `sudo apt install -y git gh`로 설치하고, `gh auth login`으로 계정을 연결합니다.
그다음 압축을 해제한 폴더에서 `bash publish.sh`를 실행하면, `Yuul-Jung` 계정인지 확인하고 **새 저장소인 경우에만** 생성·푸시·Pages 설정을 시도합니다.
이미 `capture-web` 저장소가 있다면 파일을 덮어쓰지 않고 멈춥니다.