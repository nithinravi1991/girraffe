from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to force</h1>")
def about(request):
    return HttpResponse("<h1>About Us</h1>")