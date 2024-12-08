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
