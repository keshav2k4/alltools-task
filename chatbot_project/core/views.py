from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import openai

openai.api_key = 'your_openai_api_key'  # Replace with your actual API key

def chatbot_form(request):
    return render(request, 'core/form.html')

@csrf_exempt
def generate_requirements(request):
    if request.method == 'POST':
        purpose = request.POST.get('purpose')

        prompt = f"Given a chatbot for {purpose}, what data is needed to build it with 99% accuracy?"

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )

            output = response['choices'][0]['message']['content']
        except Exception as e:
            output = f"An error occurred while contacting ChatGPT: {str(e)}"

        return render(request, 'core/result.html', {'response': output})
    else:
        return render(request, 'core/form.html')
