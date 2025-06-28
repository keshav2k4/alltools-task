from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Setup Groq-compatible OpenAI client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def chatbot_form(request):
    return render(request, 'core/form.html')

@csrf_exempt
def generate_requirements(request):
    if request.method == 'POST':
        purpose = request.POST.get('purpose')
        prompt = f"Given a chatbot for {purpose}, what data is needed to build it with 99% accuracy?"

        try:
            response = client.chat.completions.create(
                model="llama3-70b-8192",  # ✅ Updated model
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that designs chatbots."},
                    {"role": "user", "content": prompt}
                ]
            )
            output = response.choices[0].message.content
        except Exception as e:
            output = f"An error occurred while contacting Groq: {str(e)}"

        return render(request, 'core/result.html', {'response': output})

    return render(request, 'core/form.html')
