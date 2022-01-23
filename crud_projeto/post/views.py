from django.shortcuts import redirect, render
from .models import Post
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

def add(request):
    if request.method == "POST":
        title = request.POST['title']
        name = request.POST['name']
        detail = request.POST['detail']
        data = request.POST['data']
        status = request.POST['status']

        Post.objects.create(title=title, name=name, detail=detail, data=data, status=status)

        messages.success(request, "Tarefa adicionada com sucesso!")

    return render(request, 'add.html')

def update(request, id):
    if request.method == "POST":
        title = request.POST['title']
        name = request.POST['name']
        detail = request.POST['detail']
        data = request.POST['data']
        status = request.POST['status']

        Post.objects.filter(id=id).update(title=title, name=name, detail=detail, data=data, status=status)
        messages.success(request, "Tarefa atualizada com sucesso!")

    post = Post.objects.get(id=id)
    return render(request, 'update.html', {'post':post})

def delete(request, id):
    Post.objects.filter(id=id).delete()
    return redirect('/')