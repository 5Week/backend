from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

def login_view(request):
    if request.method == "POST":
        #아이디, 비밀번호 값 얻어옴
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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        #데이터베이스에 정보 추가
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('accountapp:login')
    return render(request, 'signup.html')
