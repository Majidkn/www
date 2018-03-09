from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from account.forms import SignUpForm
from account.models import User
from post.models import Post, Comment, Like, DisLike


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_ = form.save(commit=False)
            user_.is_active = True
            user_.save()
            created_user = authenticate(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password1'])
            login(request, created_user)
            return redirect('profile')
    else:
        form = SignUpForm()

    return render(request, 'account/_signup.html', {'form': form})


def profile(request, username):
    # current_user = request.user
    user = User.objects.get(username=username)
    posts = Post.objects.filter(user_id=user.id)
    for post in posts:
        comments = Comment.objects.filter(post_id=post.id)
        likes = Like.objects.filter(post_id=post.id)
        dislikes = DisLike.objects.filter(post_id=post.id)
        post.comments = len(comments)
        post.likes = len(likes)
        post.dislikes = len(dislikes)
    return render(request, 'account/_profile.html', {
        'user': user,
        'posts': posts,
    })
