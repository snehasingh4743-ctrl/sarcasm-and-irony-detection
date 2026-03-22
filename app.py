from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# -------------------------------
# Step 1: Train Model (same file)
# -------------------------------
data = {
    "text": [
        "Oh great, another Monday",
        "I love this product",
        "Yeah right, that was amazing",
        "This is fantastic",
        "I totally failed, awesome",
        "What a beautiful day",
        "Nice, my phone broke again"
    ],
    "label": [1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])

model = LogisticRegression()
model.fit(X, df["label"])

# -------------------------------
# Step 2: Flask Routes
# -------------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.json["text"]

    transformed = vectorizer.transform([text])
    prediction = model.predict(transformed)[0]

    result = "Sarcastic 😏" if prediction == 1 else "Not Sarcastic 🙂"
    return jsonify({"result": result})

# -------------------------------
# Run App
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
