import stripe
import os

stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

# Step 1 - Attach a test payment method to the customer
payment_method = stripe.PaymentMethod.create(
    type="card",
    card={"token": "tok_visa"}
)

stripe.PaymentMethod.attach(
    payment_method.id,
    customer="cus_Uf32v1uZmTUSmu"
)

# Step 2 - Set it as default
stripe.Customer.modify(
    "cus_Uf32v1uZmTUSmu",
    invoice_settings={"default_payment_method": payment_method.id}
)

# Step 3 - Create a Product
product = stripe.Product.create(
    name="ReelWorks Monthly Plan"
)

# Step 4 - Create a Price
price = stripe.Price.create(
    product=product.id,
    unit_amount=2000,
    currency="usd",
    recurring={"interval": "month"}
)

# Step 5 - Create a Subscription
subscription = stripe.Subscription.create(
    customer="cus_Uf32v1uZmTUSmu",
    items=[{"price": price.id}]
)

print("Product:", product.name)
print("Price ID:", price.id)
print("Subscription ID:", subscription.id)
print("Status:", subscription.status)