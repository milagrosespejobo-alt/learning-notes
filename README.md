\# Stripe API Integration — Python Portfolio



Built by Milagros Espejo | MBA Candidate @ Pace University

Fintech \& Payments background | Targeting Solutions Architect roles



\## What this project does

A complete Stripe payment integration built from scratch in Python,

covering the full payment lifecycle from one-time payments to 

recurring subscriptions and real-time webhook event handling.



\## Scripts



\### 1. create\_payment.py

Creates a Stripe PaymentIntent via the API.

Concepts: REST API, test vs live keys, amounts in cents, livemode flag.



\### 2. create\_customer.py

Creates a Customer object and links it to a payment.

Concepts: customer profiles, payment history, cus\_ ID.



\### 3. create\_subscription.py

Builds a full subscription flow: Product → Price → Subscription.

Concepts: recurring billing, payment method attachment, active status.



\### 4. webhook\_listener.py

A Flask server that receives and handles live Stripe events.

Concepts: webhooks, event types, two-way communication, idempotency.



\## Setup

1\. Install dependencies: pip install stripe flask

2\. Set your Stripe test key: export STRIPE\_SECRET\_KEY=sk\_test\_...

3\. Run any script: python create\_payment.py



\## Background

I come from a payments background at Izipay (Peru) where I managed

100+ B2B integrations across LATAM. This project deepens my technical

fluency with modern payment APIs as I transition toward a Solutions

Architect role in the US fintech market.

