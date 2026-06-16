from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from matcher_tamil import get_response

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index_tamil.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"response": "சரியான கேள்வியை உள்ளிடவும்."})

    response = get_response(user_message)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
