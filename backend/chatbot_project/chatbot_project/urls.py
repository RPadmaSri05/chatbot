from django.contrib import admin
from django.urls import path
from chat.views import gemini_response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/gemini/', gemini_response),  # Gemini AI API endpoint
]
