from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

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


def like_post(request, post_id):
    current_user = request.user
    post = Post.objects.get(pk=post_id)
    # like = Like.objects.get(user_id=current_user.id, post_id=post_id)
    like = Like.objects.filter(user=current_user, post=post)
    if len(like) > 0:
        like.delete()
    else:
        like = Like(post=post, user=current_user)
        like.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def dislike_post(request, post_id):
    current_user = request.user
    post = Post.objects.get(pk=post_id)
    # like = Like.objects.get(user_id=current_user.id, post_id=post_id)
    dislike = DisLike.objects.filter(user=current_user, post=post)
    if len(dislike) > 0:
        dislike.delete()
    else:
        dislike = DisLike(post=post, user=current_user)
        dislike.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_post(request, post_id):
    current_user = request.user
    post = Post.objects.get(pk=post_id)
    if current_user.id == post.user_id:
        post.delete()
        return redirect('home')
