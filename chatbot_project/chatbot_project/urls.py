from django.contrib import admin
from django.urls import path
from core import views as core_views  # ✅ important!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.chatbot_form, name='chatbot_form'),
    path('generate/', core_views.generate_requirements, name='generate_requirements'),
]
