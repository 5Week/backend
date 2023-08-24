from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import User

from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib import messages

from django.template.loader import render_to_string
# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("로그인 성공")
            login(request, user)
            request.session['user_authenticated'] = True
            return redirect('mainapp:main')
        else:
            print("로그인 실패")
    return render(request, 'login.html')

def signup_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            messages.warning(request, "이미 사용 중인 아이디입니다.")
            return render(request, 'signup.html')
        elif password != re_password:
            messages.warning(request, "비밀번호가 일치하지 않습니다.")
            return render(request, 'signup.html')

        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('accountapp:login')
    return render(request, 'signup.html')

def find_view(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            if user is not None:
                context = {'name':user.name, 'username': user.username}
                template = render_to_string('email_templates.html', context)
                method_email = EmailMessage(
                    template,
                    settings.EMAIL_HOST_USER,
                    [email],
                )
                method_email.send(fail_silently=False)
                return render(request, 'send_id.html', context)
        except:
            messages.info(request, '저장된 아이디 없음')
    return render(request, 'find.html', context)