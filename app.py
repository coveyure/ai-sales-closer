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

