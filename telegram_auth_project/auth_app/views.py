
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
import uuid

def index(request):
    if request.user.is_authenticated:
        return render(request, 'auth_app/index.html', {'username': request.user.username})
    token = str(uuid.uuid4())
    return render(request, 'auth_app/index.html', {'token': token})

@csrf_exempt
def auth(request):
    telegram_id = request.POST.get('telegram_id')
    token = request.POST.get('token')
    print(f'Received telegram_id: {telegram_id}, token: {token}')  # Отладочное сообщение
    user, created = CustomUser.objects.get_or_create(telegram_id=telegram_id)
    if created:
        user.username = f'tg_{telegram_id}'
        user.set_unusable_password()
        user.save()
    login(request, user)
    return redirect('/')

def check_auth_status(request):
    is_authenticated = request.user.is_authenticated
    print(f'Check auth status: {is_authenticated}')  # Отладочное сообщение
    return JsonResponse({'is_authenticated': is_authenticated})
