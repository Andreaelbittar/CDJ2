from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from .forms import PostForm

def panel_admin(request):
    posts = Post.objects.all() 
    context = {'posts':posts}
    return render(request, 'panel_admin.html', context)

def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login:panel_admin')
        
    context={'form':form}
    return render(request, 'post_form.html', context)

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        post.delete()
        return redirect("login:panel_admin")
    





    

