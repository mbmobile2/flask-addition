from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Send a POST request to /add with JSON {\"a\": number, \"b\": number}"

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    if not data or "a" not in data or "b" not in data:
        return jsonify({"error": "Please provide JSON with 'a' and 'b'"}), 400
    try:
        a = float(data["a"])
        b = float(data["b"])
    except ValueError:
        return jsonify({"error": "a and b must be numbers"}), 400
    return jsonify({"result": a + b})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
