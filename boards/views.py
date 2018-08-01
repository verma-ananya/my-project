from django.shortcuts import render, get_object_or_404
from .models import Board
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .forms import NewTopicForm


def home(request):
	boards = Board.objects.all()
	return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
	board = Board.objects.get(pk=pk)
	return render(request, 'topics.html', {'board': board})


def new_topic(request, pk):
	board=get_object_or_404(Board, pk=pk)
	user=User.objects.first() #get the logged in user
	if request.method == 'POST':
		form=NewTopicForm(request.POST)
		if form.is_valid():
			topic=form.save()
			topic.board=board
			topic.starter=user
			topic.save()
			post=Post.objects.create(
				message=form.cleaned_data['message'],
				topic=topic,
				created_by=user
			)
			return redirect('board_topics', pk=board.pk)
	else:
		form = NewTopicForm()
	
	return render(request, "new_topic.html", {'board': board, 'form':form})
