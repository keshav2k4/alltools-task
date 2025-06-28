from django.urls import path
from logic import views as logic_views

urlpatterns = [
    path('', logic_views.chatbot_form, name='form'),
    path('generate/', logic_views.generate_requirements, name='generate'),
]
