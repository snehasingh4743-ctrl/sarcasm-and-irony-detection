from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "").lower()

    # Basic sarcasm word list (expand or replace with ML model later)
    sarcastic_words = ["yeah right", "sure", "totally", "amazing", "great job", "perfect", "love that for me", "obviously", "Wow", "LOVE", "😍", "meeting", "UGHHHHHH"]

    # Simple rule-based sarcasm detection
    is_sarcastic = any(word in text for word in sarcastic_words)
    label = "sarcastic" if is_sarcastic else "not sarcastic"

    # Randomized confidence for demo feel
    confidence = random.uniform(0.7, 0.95) if is_sarcastic else random.uniform(0.3, 0.6)

    # Highlight any detected sarcasm cues
    highlights = [word for word in sarcastic_words if word in text]

    return jsonify({
        "label": label,
        "confidence": confidence,
        "highlights": highlights
    })

if __name__ == "__main__":
    app.run(debug=True, port=5001)