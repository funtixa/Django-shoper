from django.contrib.auth.models import User
from django.shortcuts import render

def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'userprofile/vendor_detail.html', context)
