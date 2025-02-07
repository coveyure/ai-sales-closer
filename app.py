from flask import Flask, request, jsonify
import openai
import stripe
import os  # Import os to dynamically set port

app = Flask(__name__)

# Default homepage route (to confirm the app is live)
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "AI Sales Bot is running!"})

# Chatbot API endpoint
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data or "message" not in data:
            return jsonify({"error": "No message provided"}), 400

        user_message = data["message"]
        response = {"response": f"AI response to: {user_message}"}
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Stripe Payment API
@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': 'AI Sales Closer Subscription'},
                    'unit_amount': 4900,
                },
                'quantity': 1,
            }],
            mode='subscription',
            success_url='https://yourdomain.com/success',
            cancel_url='https://yourdomain.com/cancel',
        )
        return jsonify({'id': session.id})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Main entry point for Render (DO NOT manually set the port)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Automatically uses Render's assigned port
    app.run(host="0.0.0.0", port=port, debug=True)
