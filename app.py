from flask import Flask, request, jsonify
import os  # Handles automatic port assignment

app = Flask(__name__)

# ✅ Root Route - To Check if App is Running
@app.route('/')
def home():
    return jsonify({"message": "AI Sales Bot is running!"})

# ✅ Chatbot API - Main AI Response Route
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

# ✅ Ensure Render Detects the Correct Port
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Default to 5000, but Render will assign its own
    app.run(host="0.0.0.0", port=port, debug=True)
