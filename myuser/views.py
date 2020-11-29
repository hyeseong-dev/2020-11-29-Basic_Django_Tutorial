from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import MyUser
from .forms import LoginForm


def home(request):
	return render(request, 'home.html')

def logout(request):
	if request.session.get('user'):
		del(request.session['user'])
	return redirect('/')

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			request.session['user'] = form.user_id
			return redirect('/')
	else:
		form = LoginForm()

	return render(request, 'login.html', {'form': form})

def register(request):
	if request.method == 'GET':
		return render(request, 'register.html')
	elif request.method == 'POST':
		username = request.POST.get('username', None)
		useremail = request.POST.get('useremail', None)
		password = request.POST.get('password', None)
		re_password = request.POST.get('re-password', None)

		res_data = {}

		if not(username and useremail and password and re_password): # 하나도 빠짐없이 3가지에 입력했는지 확인함(입력하지 않은 경우 로직 정의)
			res_data['error'] = '모든 값을 입력해주세요'
		elif password != re_password: # 입력한 비번1, 비번2가 다른 경우의 로직
			res_data['error'] = '비밀번호가 달라요'
		else:
			myuser = MyUser(
			username=username,
			useremail=useremail,
			password=make_password(password)
			)

			myuser.save() # db에 저장함

		return render(request, 'register.html', res_data)