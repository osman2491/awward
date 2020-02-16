from django.shortcuts import render
from . models import *


def home(request):
    projects = Post.objects.all()
    return render(request,'myprojects/index.html',{"projects":projects})

