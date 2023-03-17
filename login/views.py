from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, DocumentForm
from home.models import Documents
import os

def panel_admin(request):
    posts = Post.objects.all() 
    documents = Documents.objects.all()
    context = {'posts':posts, 'documents': documents}
    return render(request, 'panel_admin.html', context)

def create_post(request):
    form = PostForm()
    type_form = 1
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login:panel_admin')
        
    context={'form':form, "type_form": type_form}
    return render(request, 'post_form.html', context)

def delete_post(request,post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('login:panel_admin')
    
    return render(request, 'delete.html', {'post': post})

def update_post(request,post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(instance=post)
    update = 1
    type_form = 1
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance = post)
        form.save()
        return redirect('login:panel_admin')

    context = {"form":form, "update":update, "type_form": type_form}
    return render(request,'post_form.html', context)

def create_document(request):
    form = DocumentForm()
    type_form = 2
    extension = None
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login:panel_admin')
        
    extension = os.path.splitext(str(request.FILES.get('pdf')))[1]
    
    context = {"form":form, "type_form": type_form, "extension": extension}
    return render(request, 'post_form.html', context)

    





    

