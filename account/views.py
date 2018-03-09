from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from account.forms import SignUpForm


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
