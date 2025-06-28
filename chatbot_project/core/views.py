from django.shortcuts import render
import openai
from django.views.decorators.csrf import csrf_exempt

openai.api_key = 'your-openai-api-key'  # Replace with your actual OpenAI key

@csrf_exempt
def page1(request):
    if request.method == 'POST':
        purpose = request.POST.get('purpose')
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use a different model if needed
            messages=[
                {"role": "system", "content": "You're an expert chatbot creator."},
                {"role": "user", "content": f"I want to make a chatbot for: {purpose}. What data do I need?"}
            ]
        )
        data_requirements = response['choices'][0]['message']['content']
        return render(request, 'page2.html', {'data_requirements': data_requirements})
    return render(request, 'page1.html')
