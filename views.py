# real_estate/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

class Chatbot(APIView):
    def post(self, request):
        user_message = request.data.get("message")
        conversation_history = request.data.get("history", [])

        # Prepare the conversation for GPT
        gpt_prompt = "The following is a conversation about luxury real estate:\n"
        for turn in conversation_history:
            gpt_prompt += f"User: {turn['user']}\nBot: {turn['bot']}\n"
        gpt_prompt += f"User: {user_message}\nBot:"

        # Call GPT-4 API
        try:
            response = openai.Completion.create(
                engine="gpt-4",
                prompt=gpt_prompt,
                max_tokens=150,
                temperature=0.7,
            )
            bot_reply = response.choices[0].text.strip()
            return Response({"reply": bot_reply})
        except Exception as e:
            return Response({"error": str(e)}, status=500)
import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSession(APIView):
    def post(self, request):
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[
                    {
                        "price_data": {
                            "currency": "usd",
                            "product_data": {"name": "Premium Platinum Listing"},
                            "unit_amount": 100000,  # Amount in dollars
                        },
                        "quantity": 1,
                    }
                ],
                mode="payment",
                success_url="https://your-site.com/success",
                cancel_url="https://your-site.com/cancel",
            )
            return Response({"url": session.url})
        except Exception as e:
            return Response({"error": str(e)}, status=500)

