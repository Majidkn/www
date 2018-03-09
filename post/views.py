from django.shortcuts import render

# Create your views here.
from post.models import Post, Comment, Like, DisLike


def post(request, post_id):
    current_user = request.user
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post_id=post_id)
    likes = Like.objects.filter(post_id=post_id)
    dislikes = DisLike.objects.filter(post_id=post_id)
    post.comments = len(comments)
    post.likes = len(likes)
    post.dislikes = len(dislikes)
    return render(request, 'post/_post.html', {
        'user': current_user,
        'post': post,
    })