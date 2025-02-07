from flask import Flask, request, jsonify
import os

app = Flask(__name__)  # ✅ Define Flask app correctly

# ✅ Root Route - Confirms App is Running
@app.route('/')
def home():
    return jsonify({"message": "AI Sales Bot is running!"})

# ✅ Chatbot API - Fixing the 404 Issue
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data or "message" not in data:
            return jsonify({"error": "No message provided"}), 400

        user_message = data["message"]
        return jsonify({"response": f"AI response to: {user_message}"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Ensure the App Runs on the Correct Port in Render
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # Let Render auto-assign the port
    app.run(host="0.0.0.0", port=port, debug=True)
