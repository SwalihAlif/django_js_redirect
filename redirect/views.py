from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import json

# Create your views here.

@csrf_protect
def submit_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')

        response_data = {
            'message': 'Data received successfully!',
            'next_url': '/success/'
        }
        return JsonResponse(response_data)
    return JsonResponse({'error': 'Invalid request'}, status=400)


def show_form(request):
    return render(request, 'form.html')

def success_page(request):
    return render(request, 'success.html')