from flask import Flask, request, jsonify
import os  # Import os to handle dynamic port assignment

app = Flask(__name__)

# ✅ Confirm the app is running
@app.route('/')
def home():
    return jsonify({"message": "AI Sales Bot is running!"})

# ✅ Chatbot API
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400
    
    user_message = data["message"]
    return jsonify({"response": f"AI response to: {user_message}"})

# ✅ Render Deployment (Uses auto-assigned port)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Default to 10000, but Render assigns its own port
    app.run(host="0.0.0.0", port=port, debug=True)
