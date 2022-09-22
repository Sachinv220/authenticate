from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

redirect_url = "authenticate:root"

@login_required
def empty(request):
    pass

def login_user(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
    return render(request, "auth.html", context={"title":"Login", "message":"login"})


def signup_user(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        if user:
            login(request, user)
    return render(request, "auth.html", context={"title":"Signup", "message":"Signup"})
