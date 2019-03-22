from django.shortcuts import render, redirect
from .models import Shout
from .forms import ShoutForm, ShoutModelForm

# Create your views here.
def home(request):
    shouts = Shout.objects.all()
    context = {
        'shouts': shouts,
    }
    return render(request, 'shouts/home.html', context)


def create(request):
    # POST 글을 DB에 저장
    if request.method == 'POST':
        # form = ShoutForm(request.POST)
        form = ShoutModelForm(request.POST)
        if form.is_valid():
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # Shout.objects.create(title=title, content=content)
            form.save()
            return redirect('shouts:home')
    # GET 글 작성하는 form
    else:
        form = ShoutModelForm()
        context = {
            'form': form
        }
        return render(request, 'shouts/form.html', context)

def update(request, id):
    shout = Shout.objects.get(pk=id)
    if request.method == 'POST':
        form = ShoutModelForm(request.POST, instance=shout)
        if form.is_valid():
            form.save()
            return redirect('shouts:home') 
    else:
        form = ShoutModelForm(instance=shout)
        context = {
            'form': form,
        }
        return render(request, 'shouts/form.html', context)