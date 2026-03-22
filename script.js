document.getElementById("analyzeBtn").addEventListener("click", async () => {
    const tweet = document.getElementById("tweetInput").value.trim();
    const resultDiv = document.getElementById("result");
    const label = document.getElementById("label");
    const confidence = document.getElementById("confidence");
    const comment = document.getElementById("comment");

    if (!tweet) {
        alert("Please enter a tweet!");
        return;
    }

    resultDiv.classList.remove("hidden");
    label.textContent = "Analyzing...";
    confidence.textContent = "";
    comment.textContent = "";

    const response = await fetch("/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: tweet })
    });

    const data = await response.json();

    label.textContent = data.label === "sarcastic" ? "😏 Sarcastic" : "🙂 Not Sarcastic";
    confidence.textContent = `Confidence: ${(data.confidence * 100).toFixed(1)}%`;

    const funnyComment = data.label === "sarcastic"
        ? "Oof, that’s dripping with irony 💅"
        : "Seems pretty straightforward. No sarcasm detected 🫡";

    comment.textContent = funnyComment;
});