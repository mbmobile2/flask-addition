from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return '''
        <h2>Welcome to the Addition API</h2>
        <p>Send a POST request to <code>/add</code> with JSON: {"a": number, "b": number}</p>
        <p>Or try the <a href="/form">web form</a>.</p>
    '''

@app.route("/form")
def form():
    return '''
        <h2>Add Two Numbers</h2>
        <form action="/add" method="post">
            <label>A: <input name="a" type="number" step="any"></label><br><br>
            <label>B: <input name="b" type="number" step="any"></label><br><br>
            <button type="submit">Add</button>
        </form>
    '''

@app.route("/add", methods=["POST"])
def add():
    try:
        if request.is_json:
            data = request.get_json()
            a = float(data.get("a", 0))
            b = float(data.get("b", 0))
        else:
            a = float(request.form.get("a", 0))
            b = float(request.form.get("b", 0))
        return jsonify({"result": a + b})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
