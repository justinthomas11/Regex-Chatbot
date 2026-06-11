from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# Import your existing modules
# from main import get_response   ← uncomment and adjust once you know the function name
# from matcher import match_intent
# from intent import get_intent

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"response": "Please enter a valid query."})

    # -------------------------------------------------------
    # TODO: Replace the line below with your actual bot call
    # response = get_response(user_message)
    # -------------------------------------------------------
    # Placeholder until integrated:
    response = f"[Bot] Received: '{user_message}' — connect main.py logic here."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
