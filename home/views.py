from django.shortcuts import render

# Create your views here.
from account.models import User
from post.models import Post, Comment, Like, DisLike


def home(request):
    posts = Post.objects.all().order_by('-date_created')
    for post in posts:
        comments = Comment.objects.filter(post_id=post.id)
        likes = Like.objects.filter(post_id=post.id)
        dislikes = DisLike.objects.filter(post_id=post.id)
        post.comments = len(comments)
        post.likes = len(likes)
        post.dislikes = len(dislikes)
        post.body = post.body[:25] + (post.body[25:] and '...')
    return render(request, 'account/_home.html', {'posts': posts})
