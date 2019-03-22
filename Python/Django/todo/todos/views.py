from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    # todos에 있는 내용을 다 가져와 보여주기, 접속한 유저의 정보만 가져옴
    if request.user.is_authenticated:
        todos = request.user.todo_set.all()
    else:
        todos = ''
    return render(request, 'todos/home.html', {'todos':todos})

def create(request):
    # todos 작성하기
    content = request.POST.get('content')
    user_id = request.user.id
    # user_id = User.objects.first().id
    # completed = request.POST.get('completed')
    Todo.objects.create(content=content, user_id=user_id)

    return redirect('todos:home')

def check(request, id):
    # 특정 id를 가진 투두를 뽑아 completed = True
    todo = Todo.objects.get(pk=id)
    if todo.completed:
        todo.completed = False
    else:
        todo.completed = True
    todo.save()
    return redirect('todos:home')

def delete(request, id):
    Todo.objects.get(pk=id).delete()
    return redirect('todos:home')
