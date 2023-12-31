from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Task


def dashboard(request):
    user_count = User.objects.count()
    task_count = Task.objects.count()

    context = {'user_count': user_count, 'task_count': task_count}
    return render(request, 'dashboard.html', context)


