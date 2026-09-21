from flask import Flask, render_template, request, jsonify
from src.recommendation import get_recommendations

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return jsonify({
        "status": "online",
        "model": "Sentence Transformer",
        "faiss": "loaded"
    })

@app.route("/recommend", methods=["POST"])
def recommend():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No input provided"}), 400

        query = data.get("query")
        top_n = int(data.get("top_n", 5))

        if not query:
            return jsonify({"error": "Query is required"}), 400

        top_n = max(1, min(top_n, 20))

        result = get_recommendations(query, top_n)

        if "error" in result:
            return jsonify(result), 400

        return jsonify(result)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)