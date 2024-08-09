from django.urls import path
from . import views

urlpatterns = [
    path('root/', views.root, name='root'),
    path('chatbot-response/', views.chatbot_response, name='chatbot_response'),
]
