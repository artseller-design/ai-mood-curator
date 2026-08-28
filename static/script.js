document.addEventListener("DOMContentLoaded", () => {
  const emotionInput = document.getElementById("emotionInput");
  const situationInput = document.getElementById("situationInput");
  const recommendBtn = document.getElementById("recommendBtn");
  const resultBox = document.getElementById("result");
  const loading = document.getElementById("loading");

  // HTML 요소 연결 확인
  if (!emotionInput || !situationInput || !recommendBtn || !resultBox || !loading) {
    console.error("HTML 요소를 찾지 못했습니다.");
    alert("HTML 요소 id가 script.js와 맞지 않습니다. index.html을 확인하세요.");
    return;
  }

  recommendBtn.addEventListener("click", async () => {
    const emotion = emotionInput.value.trim();
    const situation = situationInput.value.trim();

    // 입력값 확인
    if (!emotion && !situation) {
      alert("감정이나 상황을 입력해주세요.");
      return;
    }

    // 요청 전 화면 상태 변경
    resultBox.classList.add("hidden");
    loading.classList.remove("hidden");
    recommendBtn.disabled = true;
    recommendBtn.textContent = "추천 중...";

    try {
      const response = await fetch("/api/recommend", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          emotion,
          situation
        })
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || data.error || "추천 요청에 실패했습니다.");
      }

      showResult(data);

    } catch (error) {
      console.error("추천 오류:", error);

      resultBox.innerHTML = `
        <h2>오류가 발생했어요</h2>
        <p>${error.message}</p>
      `;

      resultBox.classList.remove("hidden");

    } finally {
      loading.classList.add("hidden");
      recommendBtn.disabled = false;
      recommendBtn.textContent = "추천 받기";
    }
  });

  function showResult(data) {
    const musicList = data.music || [];
    const artList = data.art || [];

    resultBox.innerHTML = `
      <h2>감정 요약</h2>
      <p>${data.emotion_summary || "감정 요약이 없습니다."}</p>

      <h2>추천 음악</h2>
      ${
        musicList.length > 0
          ? musicList.map(song => `
            <div class="item">
              <strong>${song.title || "제목 없음"}</strong>
              <span> - ${song.artist || "아티스트 없음"}</span>
              <p>${song.reason || "추천 이유가 없습니다."}</p>
            </div>
          `).join("")
          : "<p>추천 음악이 없습니다.</p>"
      }

      <h2>추천 미술 작품</h2>
      ${
        artList.length > 0
          ? artList.map(art => `
            <div class="item">
              <strong>${art.title || "작품명 없음"}</strong>
              <span> - ${art.artist || "작가 없음"}</span>
              <p>${art.reason || "추천 이유가 없습니다."}</p>
            </div>
          `).join("")
          : "<p>추천 미술 작품이 없습니다.</p>"
      }

      <div class="message">
        ${data.message || ""}
      </div>
    `;

    resultBox.classList.remove("hidden");
  }
});
