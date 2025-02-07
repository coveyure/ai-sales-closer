from flask import Flask, request, jsonify
import os

# ✅ Define `app` first before using it
app = Flask(__name__)

# ✅ Root Route - Confirms App is Running
@app.route('/')
def home():
    return jsonify({"message": "AI Sales Bot is running!"})

# ✅ Chatbot API - Handles Sales Conversations
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

# ✅ Auto-Port for Render Deployment
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # Render auto-assigns the correct port
    app.run(host="0.0.0.0", port=port, debug=True)
