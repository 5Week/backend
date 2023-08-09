from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("로그인 성공")
        else:
            print("로그인 실패")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect("accountapp:login")
def signup_view(request):
    return render(request, 'signup.html')