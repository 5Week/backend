from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from .models import Board
from .form import PostForm

# Create your views here.

def main_view(request):
    user_authenticated = request.session.get('user_authenticated', False)
    boards = Board.objects.all()
    if user_authenticated:
        print("로그인")
    else:
        print("로그아웃")
    return render(request, 'main.html', {'boards': boards})

def logout_view(request):
    logout(request)
    request.session['user_authenticated'] = False
    return redirect('mainapp:main')


def list_view(request):
    login_session = request.session.get('login_session','')
    context = {'login_session':login_session}

    if request.method == "GET":
        postForm = PostForm()
        context['forms'] = postForm
        return render(request, 'list.html', context)

    elif request.method == "POST":
        postForm = PostForm(request.POST)

        if postForm.is_valid():
            writer = User.objects.get(username=login_session)
            board = Board(
                title=postForm.cleaned_data['title'],
                content=postForm.cleaned_data['content'],
                writer=writer,
            )
            board.save()
            return redirect('mainapp:main')
        else:
            if postForm.errors:
                for value in postForm.errors.values():
                    context['error'] = value
            return render(request, 'list.html')

def mypage_view(request):
    return render(request, 'mypage.html')

def detail_view(request, board_id):
    board = get_object_or_404(Board, board_id=board_id)
    return render(request, 'detail.html', {'board': board})

