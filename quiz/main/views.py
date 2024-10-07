from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def print_hello(request):
    return render (request,
                    'index.html',
                    context = {
                        'questions': QuizQuestion.objects.all()
                    })