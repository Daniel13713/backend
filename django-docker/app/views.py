from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from app.models import Question, Post
import json

# Create your views here.
def home(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'app/home.html', {'posts': posts})

def user(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'app/user.html', context)

def questions(request):
    all_questions = Question.objects.all()
    response = [{obj.text: obj.text} for obj in all_questions]
    print(response)
    return JsonResponse(response, safe=False)
