from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome! Use POST /add with JSON {'a': number, 'b': number} to add."

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    if a is None or b is None:
        return jsonify({"error": "Please provide numbers 'a' and 'b' in JSON"}), 400
    try:
        result = float(a) + float(b)
    except ValueError:
        return jsonify({"error": "Inputs must be numbers"}), 400
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
