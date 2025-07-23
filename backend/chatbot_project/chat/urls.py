print("✅ chat.urls is loaded")

from django.urls import path
from .views import ChatBotAPIView
from django.http import JsonResponse

def test(request):
    return JsonResponse({"msg": "working"})

urlpatterns = [
    path("chat/", ChatBotAPIView.as_view()),  # http://127.0.0.1:8000/api/chat/
    path("ping/", test),                      # http://127.0.0.1:8000/api/ping/
]
