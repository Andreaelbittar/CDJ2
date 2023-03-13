from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

def news(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = PostForm()
            return redirect('news')
    else:
        form = PostForm()

    posts = Post.objects.all()
    context = {'posts': posts, 'form': form}
    return render(request, 'admin.html', context)
