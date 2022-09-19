from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import UserProfile


def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'userprofile/vendor_detail.html', context)

def myaccount(request):
    return render(request, 'userprofile/myaccount.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            userprofile = UserProfile.objects.create(user=user)
            return redirect('frontpage')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'userprofile/signup.html', context)
