from django.shortcuts import render
from django.http  import HttpResponse
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')
# Create your views here.
