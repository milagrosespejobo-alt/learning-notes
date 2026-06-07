import stripe
import os

stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

intent = stripe.PaymentIntent.create(
    amount=2000,
    currency="usd",
    customer="cus_Uf32v1uZmTUSmu",
    payment_method_types=["card"],
    metadata={
        "customer_name": "Milagros Espejo",
        "order_id": "ORD-002"
    }
)

print("Status:", intent.status)
print("Intent ID:", intent.id)
print("Customer:", intent.customer)
print("Client secret:", intent.client_secret)