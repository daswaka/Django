from django.shortcuts import redirect
from django.urls import reverse

def redirect_root(request):
    return redirect(reverse('post_list'))