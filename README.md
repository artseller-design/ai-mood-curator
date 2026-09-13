# AI Mood Curator

AI Mood Curator는 사용자가 입력한 감정이나 상황을 바탕으로 Google Gemini AI가 감정을 분석하고, 그 감정에 어울리는 음악과 미술 작품을 추천해주는 웹서비스입니다.

사용자는 자신의 현재 기분을 문장으로 입력할 수 있으며, AI는 입력 내용을 바탕으로 감정 요약, 공감 메시지, 음악 추천, 미술 작품 추천을 제공합니다.

---

## 배포 URL

아래 링크에서 서비스를 확인할 수 있습니다.

```text
배포 URL: https://your-project-name.vercel.app
```

> 아직 배포 전이라면 위 주소는 Vercel 배포가 완료된 후 실제 주소로 수정하면 됩니다.

---

## 서비스 소개

현대인은 기분이나 감정을 표현하고 싶어도 그 감정에 어울리는 음악이나 예술 작품을 직접 찾기 어려울 때가 많습니다.

AI Mood Curator는 이러한 문제를 해결하기 위해 만들어진 감정 기반 AI 예술 큐레이션 서비스입니다.

사용자가 예를 들어 다음과 같이 입력하면,

```text
요즘 너무 지치고 아무것도 하기 싫어요.
```

AI는 사용자의 문장을 분석하여 다음과 같은 정보를 제공합니다.

- 현재 감정 요약
- 사용자에게 전하는 짧은 공감과 위로 메시지
- 감정에 어울리는 음악 추천
- 감정에 어울리는 미술 작품 추천

이 서비스는 단순히 콘텐츠를 추천하는 것을 넘어, 사용자의 감정을 이해하고 그에 맞는 예술적 경험을 제안하는 것을 목표로 합니다.

---

## 주요 기능

### 1. 감정 입력

사용자는 현재 자신의 감정, 기분, 상황을 자유롭게 입력할 수 있습니다.

예시:

```text
오늘은 왠지 외롭고 조용한 음악을 듣고 싶어요.
```

### 2. Gemini AI 감정 분석

입력된 문장을 Google Gemini AI가 분석하여 사용자의 감정 상태를 요약합니다.

예시:

```text
현재 사용자는 외로움과 차분함이 섞인 감정을 느끼고 있습니다.
```

### 3. 음악 추천

분석된 감정에 어울리는 음악을 추천합니다.

추천 결과에는 다음과 같은 정보가 포함될 수 있습니다.

- 곡 제목
- 아티스트
- 추천 이유

### 4. 미술 작품 추천

사용자의 감정과 어울리는 미술 작품을 추천합니다.

추천 결과에는 다음과 같은 정보가 포함될 수 있습니다.

- 작품명
- 작가명
- 추천 이유

### 5. 공감 메시지 제공

단순한 분석 결과가 아니라 사용자의 감정을 위로하거나 공감하는 짧은 메시지를 제공합니다.

---

## 기술 스택

### Frontend

| 기술 | 설명 |
|---|---|
| HTML | 웹페이지 구조 작성 |
| CSS | 화면 디자인 및 스타일링 |
| JavaScript | 사용자 입력 처리 및 서버와 통신 |

### Backend

| 기술 | 설명 |
|---|---|
| Python | 백엔드 로직 구현 |
| Flask | 웹 서버 및 API 라우팅 구현 |

### AI API

| 기술 | 설명 |
|---|---|
| Google Gemini API | 감정 분석 및 음악/미술 추천 결과 생성 |

### Deployment

| 기술 | 설명 |
|---|---|
| GitHub | 프로젝트 코드 저장 및 관리 |
| Vercel | 웹서비스 배포 |

---

## 프로젝트 구조

```text
.
├── api/
│   └── index.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   ├── script.js
│   └── images/
│       └── mood_art.png
├── requirements.txt
├── vercel.json
├── .gitignore
└── README.md
```

### 주요 파일 설명

| 파일 경로 | 설명 |
|---|---|
| `api/index.py` | Flask 서버 및 Gemini API 연동 코드 |
| `templates/index.html` | 메인 웹페이지 HTML 파일 |
| `static/style.css` | 웹페이지 스타일 파일 |
| `static/script.js` | 프론트엔드 JavaScript 파일 |
| `static/images/mood_art.png` | 웹페이지에 사용되는 이미지 파일 |
| `requirements.txt` | Python 패키지 목록 |
| `vercel.json` | Vercel 배포 설정 파일 |
| `.gitignore` | GitHub에 올리지 않을 파일 설정 |

---

## 환경 변수 설정 방법

이 프로젝트는 Google Gemini API를 사용하기 때문에 API 키를 환경 변수로 설정해야 합니다.

보안을 위해 API 키는 코드에 직접 작성하지 않고 `.env` 파일 또는 배포 플랫폼의 환경 변수 설정을 사용합니다.

### 1. Gemini API 키 발급

Google AI Studio에서 Gemini API 키를 발급받습니다.

```text
https://aistudio.google.com/
```

API 키를 발급받은 뒤 아래와 같은 형태로 저장합니다.

```text
GEMINI_API_KEY=발급받은_API_키
```

### 2. 로컬 환경 변수 설정

프로젝트 루트 폴더에 `.env` 파일을 생성합니다.

```text
.env
```

그리고 아래 내용을 입력합니다.

```env
GEMINI_API_KEY=본인의_Gemini_API_키
```

예시:

```env
GEMINI_API_KEY=AIzaSyxxxxxxxxxxxxxxxxxxxxxxxx
```

> 주의: `.env` 파일은 절대 GitHub에 업로드하면 안 됩니다. API 키가 공개되면 다른 사람이 사용할 수 있기 때문에 보안상 위험합니다.

### 3. `.gitignore` 설정

`.env` 파일이 GitHub에 올라가지 않도록 `.gitignore` 파일에 아래 내용이 포함되어 있어야 합니다.

```gitignore
.env
__pycache__/
venv/
.venv/
```

---

## 로컬 실행 방법

### 1. 저장소 클론

GitHub 저장소를 로컬 컴퓨터로 가져옵니다.

```bash
git clone https://github.com/사용자이름/저장소이름.git
```

프로젝트 폴더로 이동합니다.

```bash
cd 저장소이름
```

### 2. 가상환경 생성

Python 가상환경을 생성합니다.

```bash
python -m venv venv
```

가상환경을 실행합니다.

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 3. 필요한 패키지 설치

`requirements.txt` 파일에 적힌 패키지를 설치합니다.

```bash
pip install -r requirements.txt
```

### 4. 환경 변수 파일 생성

프로젝트 루트에 `.env` 파일을 만들고 Gemini API 키를 입력합니다.

```env
GEMINI_API_KEY=본인의_Gemini_API_키
```

### 5. Flask 서버 실행

아래 명령어로 서버를 실행합니다.

```bash
python api/index.py
```

또는 Flask 명령어를 사용할 수도 있습니다.

```bash
flask run
```

### 6. 브라우저에서 접속

서버 실행 후 브라우저에서 아래 주소로 접속합니다.

```text
http://127.0.0.1:5000
```

---

## Vercel 배포 방법

이 프로젝트는 Vercel을 통해 배포할 수 있도록 구성되어 있습니다.

### 1. GitHub에 프로젝트 업로드

프로젝트 파일을 GitHub 저장소에 업로드합니다.

필수로 포함되어야 하는 파일은 다음과 같습니다.

```text
api/index.py
templates/index.html
static/style.css
static/script.js
requirements.txt
vercel.json
```

단, `.env` 파일은 업로드하지 않습니다.

### 2. Vercel에서 프로젝트 가져오기

1. Vercel에 로그인합니다.
2. `Add New Project`를 클릭합니다.
3. GitHub 저장소를 선택합니다.
4. 프로젝트를 Import합니다.

### 3. Vercel 환경 변수 설정

Vercel 프로젝트 설정에서 환경 변수를 추가해야 합니다.

경로:

```text
Project Settings → Environment Variables
```

아래 환경 변수를 추가합니다.

| Name | Value |
|---|---|
| `GEMINI_API_KEY` | 본인의 Gemini API 키 |

예시:

```text
Name: GEMINI_API_KEY
Value: AIzaSyxxxxxxxxxxxxxxxxxxxxxxxx
```

환경 변수를 추가한 뒤 다시 배포해야 적용됩니다.

### 4. 배포 실행

환경 변수 설정 후 Vercel에서 Deploy를 실행합니다.

배포가 완료되면 Vercel에서 아래와 같은 주소가 생성됩니다.

```text
https://your-project-name.vercel.app
```

README의 배포 URL 부분을 실제 주소로 수정합니다.

---

## API 키 보안 주의사항

API 키는 절대 GitHub에 공개하면 안 됩니다.

다음과 같은 방식은 사용하지 않는 것이 좋습니다.

```python
GEMINI_API_KEY = "실제_API_키"
```

대신 환경 변수에서 불러오는 방식을 사용해야 합니다.

```python
import os

api_key = os.getenv("GEMINI_API_KEY")
```

이렇게 하면 API 키를 코드에 직접 적지 않아도 되어 보안상 더 안전합니다.

---

## 사용 방법

1. 웹사이트에 접속합니다.
2. 입력창에 현재 감정이나 상황을 적습니다.
3. 추천 버튼을 누릅니다.
4. AI가 감정을 분석합니다.
5. 음악 추천과 미술 작품 추천 결과를 확인합니다.

---

## 입력 예시

```text
요즘 마음이 복잡하고 조용히 쉬고 싶어요.
```

```text
기분이 좋아서 밝고 신나는 음악을 듣고 싶어요.
```

```text
외롭지만 너무 슬프지는 않은 잔잔한 분위기가 좋아요.
```

---

## 결과 예시

사용자가 다음과 같이 입력한 경우,

```text
요즘 너무 지치고 아무것도 하기 싫어요.
```

AI는 다음과 같은 형식의 결과를 제공합니다.

```text
감정 요약:
피로감과 무기력함이 느껴집니다.

공감 메시지:
지금은 스스로를 몰아붙이기보다 잠시 쉬어가도 괜찮은 시간입니다.

음악 추천:
- 곡명: Fix You
- 아티스트: Coldplay
- 추천 이유: 지친 마음을 천천히 위로해주는 분위기의 곡입니다.

미술 작품 추천:
- 작품명: Starry Night
- 작가: Vincent van Gogh
- 추천 이유: 복잡한 감정을 아름답고 깊이 있게 바라볼 수 있는 작품입니다.
```

---

## 개발 과정에서 배운 점

이 프로젝트를 만들면서 다음 내용을 경험했습니다.

- Flask를 이용한 웹 서버 구성
- HTML, CSS, JavaScript를 활용한 웹페이지 제작
- 프론트엔드와 백엔드 연결
- Google Gemini API 연동
- 환경 변수를 이용한 API 키 관리
- GitHub를 통한 코드 관리
- Vercel을 이용한 웹서비스 배포 준비
- 배포 환경에서의 파일 경로와 정적 파일 처리

---

## 향후 개선 사항

앞으로 다음과 같은 기능을 추가할 수 있습니다.

- 추천 음악의 YouTube 또는 Spotify 링크 연결
- 추천 미술 작품 이미지 추가
- 사용자 감정 기록 저장 기능
- 감정별 추천 결과 아카이브
- 모바일 화면 최적화
- 로딩 애니메이션 개선
- 추천 결과 공유 기능
- 사용자 입력 예시 버튼 추가

---

## 프로젝트 의의

AI Mood Curator는 단순한 연습용 웹페이지가 아니라, 사용자의 감정을 입력받고 AI가 분석하여 음악과 미술 작품을 추천하는 하나의 완성된 AI 기반 웹서비스입니다.

이 프로젝트를 통해 기획, 프론트엔드, 백엔드, AI API 연동, GitHub 업로드, 배포 준비까지 웹서비스 개발의 전체 흐름을 직접 경험했습니다.
