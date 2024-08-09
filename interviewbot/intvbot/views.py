from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# from .chatbot import respuesta  # Importa la función desde chatbot.py
# Create your views here.

def root(request):
    return render(request, 'intvbot/root.html')

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message', '')
        # response = respuesta(message)
        response = "respuesta"
        return JsonResponse({'response': response})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)