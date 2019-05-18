from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from comments.models import Comment
from .forms import AddPost

def all_posts(request):

    posts = Post.objects.filter(published_on__lte=timezone.now()).order_by('published_on')
    return render(request, 'blog/posts.html', {'posts': posts})

def single_post(request, post_id):

    if request.method == "POST":

        userid = request.user
        comment = request.POST['comment']
        post = get_object_or_404(Post, pk=post_id)

        if comment == '':
            messages.error(request, 'Comment message is required.')
            return redirect('/blog/post/'+post_id)

        comment = Comment(userid=userid, comment=comment, blog_post_id=post)
        comment.save()

        messages.success(request, 'Thanks for your comment.')
        return redirect('post', post_id)

    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.all().filter(blog_post_id=post_id)

    context = {
        'post' : post,
        'comments': comments
    }

    return render(request, 'blog/post.html', context)

def add_post(request):

    if request.method == "POST":

        form = AddPost(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            post.author = request.user
            post.save()

            messages.success(request, 'Your blog post has been published successfully.')
            return redirect('post', post.pk)

    else:

        form = AddPost()

    return render(request, 'blog/addpost.html', {'form':form})
