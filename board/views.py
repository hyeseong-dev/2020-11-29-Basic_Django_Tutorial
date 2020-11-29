from django.shortcuts import render, redirect
from django.core.paginator import Paginator # 게시판 하단의 페이지 이동시 구현하기 위한 클래스
from django.http import Http404 # 요청에 대한 오류를 의도적으로 발생하기 위한 클래스
from myuser.models import MyUser
from tag.models import Tag
from .models import Board
from .forms import BoardForm # board_write메서드에 적용하기 위한 커스마이징한 폼

def board_write(request):
	if not request.session.get('user'): # 게시물 열람은 로그인할 필요없지만 게시물 작성은 로그인하여 session값을 받은 상태로 해야하기 때문
		return redirect('/myuser/login')
	
	if request.method == 'POST':
		form = BoardForm(request.POST)
		if form.is_valid():
			user_id = request.session.get('user') # 브라우저에서 session을 받아옴
			myuser = MyUser.objects.get(pk=user_id)

			tags = cleaned_data['tags'].split(',')

			board = Board()
			board.title = form.cleaned_data['title']
			board.contents = form.cleaned_data['contents']
			board.writer = myuser
			board.save()

			for tag in tags:
				if not tag:
					continue

				_tag, _ = Tag.objects.get_or_create(name=tag)
				board.tags.add(_tag)
			
			return redirect('/board/list')
	else:
		form = BoardForm()

	return render(request, 'board_write.html', {'form':form})




def board_detail(request, pk):
	try:
		board = Board.objects.get(pk=pk)
	except Board.DoesNotExist:
		raise Http404('게시글을 찾을 수 없습니다.')

	return(request, 'board_detail.html',{'borad':board})

def board_list(request):
	all_boards = Board.objects.all().order_by('-id') # Board 테이블에서 입력된 객체를 내림차순으로 가져와서 변수에 저장함
	page = int(request.GET.get('p',1)) # url의 query string에서 'p'에 해당하는 값을 가져오는데, p값이 없으면 1로 세팅함
	paginator = Paginator(all_boards, 3) # 한 페이지당 몇개을 글(contents)보여줄지 2번째 파라미터로 지정
	# Paginator란 게시판과 같은 목로깅 주어져있을때, 페이지 당 몇개의 글을 보여줄지 지정해줄 수 있도록 도와주는 모듈
	boards = paginator.get_page(page)
	return render(request, 'board_list.html', {'boards': boards})