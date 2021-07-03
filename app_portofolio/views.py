from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import CommentForm
from .models import Post



# Create your views here.


def index_view(request):
    return render(request, "index.html", {})


def aboutme_page(request):
    return render(request, 'aboutme.html', {})


def contact_page(request):
    return render(request, 'contact.html', {})


def portofolio_page(request):
    posts = Post.objects.all()
    return render(request, 'portofolio.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    form = CommentForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',slug=post.slug)
        else:
            form = CommentForm()

    return render(request, 'post_detail.html', {'post':post, 'form':form})

