import stripe
import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

@app.route("/webhook", methods=["POST"])
def webhook():
    payload = request.get_data(as_text=True)
    
    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        print("Invalid payload:", e)
        return jsonify(success=False), 400

    if event.type == "payment_intent.succeeded":
        payment_intent = event.data.object
        print(f"✅ Payment succeeded! Amount: {payment_intent.amount} cents")
        print(f"✅ Customer: {payment_intent.customer}")

    elif event.type == "payment_intent.created":
        payment_intent = event.data.object
        print(f"🔔 Payment intent created! ID: {payment_intent.id}")

    elif event.type == "customer.subscription.created":
        subscription = event.data.object
        print(f"🔔 New subscription! ID: {subscription.id}")

    elif event.type == "invoice.paid":
        invoice = event.data.object
        print(f"✅ Invoice paid! Amount: {invoice.amount_paid} cents")

    else:
        print(f"Unhandled event: {event.type}")

    return jsonify(success=True), 200

if __name__ == "__main__":
    app.run(port=4242, debug=True)