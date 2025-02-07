from flask import Flask, request, jsonify
import openai
import stripe

app = Flask(__name__)

# Default homepage route (to check if the app is running)
@app.route('/')
def home():
    return "AI Sales Bot is running!"

# Chat endpoint
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    response = {"response": f"AI response to: {user_message}"}
    return jsonify(response)

# Stripe API Key (Replace with your actual API Key)
STRIPE_SECRET_KEY = "your_stripe_secret_key"
stripe.api_key = STRIPE_SECRET_KEY

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
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(debug=True)
import openai
from flask import Flask, request, jsonify
import stripe

app = Flask(__name__)

# OpenAI API Key (Replace with your actual API Key)
OPENAI_API_KEY = "your_openai_api_key"

def generate_ai_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "You are a sales AI assistant."},
                  {"role": "user", "content": user_input}]
    )
    return response['choices'][0]['message']['content']

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    ai_response = generate_ai_response(user_message)
    return jsonify({"response": ai_response})

# Stripe API Key (Replace with your actual API Key)
STRIPE_SECRET_KEY = "your_stripe_secret_key"
stripe.api_key = STRIPE_SECRET_KEY

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
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(debug=True)
