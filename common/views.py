from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm


def signup(request):
    if request.method == "POST":  # POST 요청이면
        form = UserForm(request.POST)  # 요청한POST(화면에 저장된 내용)로 UserForm을 생성
        if form.is_valid():  # 폼이 유효하면
            form.save()  # 폼 내용 저장(회원가입 내용 저장)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증, 계정생성
            login(request, user)  # 자동 로그인
            return redirect('index')
    else:  # POST 요청이 아니면(GET 요청이면)
        form = UserForm()  # 회원가입 화면 보여주기
    return render(request, 'common/signup.html', {'form': form})