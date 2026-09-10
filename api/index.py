from flask import Flask, jsonify, render_template, request, send_from_directory
from dotenv import load_dotenv
import google.generativeai as genai
import os
import json
import re
from pathlib import Path
import random
from datetime import datetime


# 현재 파일 기준 경로 설정
# api/index.py 기준:
# BASE_DIR = 프로젝트/api
# ROOT_DIR = 프로젝트 루트
BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent

# .env 파일 로드
load_dotenv(ROOT_DIR / ".env")

# Flask 앱 생성
# index.html이 프로젝트 최상위에 있으므로 template_folder를 ROOT_DIR로 설정합니다.
# static_folder=None 으로 두고, 아래에서 직접 /static 경로를 처리합니다.
app = Flask(
    __name__,
    template_folder=str(ROOT_DIR),
    static_folder=None
)


# Vercel 환경에서 static 파일 직접 제공
@app.route("/static/<path:filename>", endpoint="static")
def serve_static(filename):
    return send_from_directory(str(ROOT_DIR / "static"), filename)


# Gemini API 키 가져오기
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

print("프로젝트 경로:", ROOT_DIR)
print(".env 경로:", ROOT_DIR / ".env")
print("API 키 로드 여부:", bool(GEMINI_API_KEY))


# Gemini API 설정
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)


# Gemini 응답에서 JSON만 추출하는 함수
def extract_json_from_text(text):
    text = text.strip()

    # ```json ... ``` 형태 제거
    text = re.sub(r"^```json", "", text)
    text = re.sub(r"^```", "", text)
    text = re.sub(r"```$", "", text)
    text = text.strip()

    return json.loads(text)


# 메인 페이지
@app.route("/")
@app.route("/api")
@app.route("/api/")
@app.route("/index.py")
@app.route("/api/index")
@app.route("/api/index.py")
def index():
    return render_template("index.html")


# 추천 API
@app.route("/api/recommend", methods=["POST"])
def recommend():
    raw_text = ""

    try:
        # API 키 확인
        if not GEMINI_API_KEY:
            return jsonify({
                "error": "GEMINI_API_KEY가 설정되지 않았습니다.",
                "detail": ".env 파일 위치와 변수명을 확인하세요."
            }), 500

        # 프론트엔드에서 보낸 JSON 데이터 받기
        data = request.get_json(silent=True) or {}

        emotion = data.get("emotion", "").strip()
        situation = data.get("situation", "").strip()

        # emotion 또는 situation 중 하나는 있어야 함
        if not emotion and not situation:
            return jsonify({
                "error": "emotion 또는 situation 값이 필요합니다."
            }), 400

        # 추천 다양성을 위한 값
        random_hint = random.randint(1000, 9999)
        request_time = datetime.now().isoformat()

        # Gemini에게 보낼 프롬프트
        prompt = f"""
너는 감정 기반 음악과 미술 작품을 추천하는 큐레이터야.

사용자의 감정과 상황을 바탕으로 음악 2개와 미술 작품 2개를 추천해줘.

사용자 감정: {emotion}
사용자 상황: {situation}

추천 조건:
1. 반드시 한국어로 답변해.
2. 반드시 JSON 형식으로만 답변해.
3. JSON 외에는 설명 문장을 붙이지 마.
4. 음악은 실제 존재하는 곡으로 추천해.
5. 미술 작품은 실제 존재하는 작품으로 추천해.
6. 사용자의 감정을 위로하거나 공감하는 따뜻한 메시지를 포함해.
7. 너무 유명한 작품만 반복하지 말고 다양하게 추천해.
8. 같은 감정이라도 매번 다른 음악과 작품 조합을 선택해.
9. 음악과 작품 1개씩은 비교적 덜 알려진 후보를 포함해도 좋아.
10. 음악은 장르, 시대, 분위기가 서로 겹치지 않도록 골라.
11. 미술 작품도 작가, 시대, 분위기가 서로 겹치지 않도록 골라.
12. 이전에 많이 추천될 법한 대표작만 고르지 말고 다양한 후보를 고려해.

다양성 참고값:
- random_hint: {random_hint}
- request_time: {request_time}

반드시 아래 JSON 형식만 반환해.

{{
  "emotion_summary": "사용자 감정 요약",
  "music": [
    {{
      "title": "음악 제목",
      "artist": "아티스트",
      "reason": "추천 이유"
    }},
    {{
      "title": "음악 제목",
      "artist": "아티스트",
      "reason": "추천 이유"
    }}
  ],
  "art": [
    {{
      "title": "작품 제목",
      "artist": "작가",
      "reason": "추천 이유"
    }},
    {{
      "title": "작품 제목",
      "artist": "작가",
      "reason": "추천 이유"
    }}
  ],
  "message": "사용자에게 전하는 따뜻한 위로 메시지"
}}
"""

        # Gemini 모델 생성
        model = genai.GenerativeModel("models/gemini-3.6-flash")

        # Gemini API 호출
        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 1.0,
                "top_p": 0.95,
                "top_k": 40,
                "response_mime_type": "application/json"
            }
        )

        raw_text = response.text.strip()

        print("Gemini 원본 응답:")
        print(raw_text)

        # Gemini 응답을 JSON으로 변환
        result = extract_json_from_text(raw_text)

        return jsonify(result), 200

    except json.JSONDecodeError as e:
        print("JSON 변환 오류:", e)
        print("Gemini 원본 응답:", raw_text)

        return jsonify({
            "error": "Gemini 응답을 JSON으로 변환하지 못했습니다.",
            "detail": str(e),
            "raw_response": raw_text
        }), 500

    except Exception as e:
        print("Gemini API 오류:", e)

        return jsonify({
            "error": "추천을 생성하는 중 오류가 발생했습니다.",
            "detail": str(e)
        }), 500


# 로컬 실행용
if __name__ == "__main__":
    app.run(debug=True, port=5000)