from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.views.generic import View

class PostList(View):
    def get(self, request):
        plist = Post.objects.all()
        return render(request, 'blog/post_list.html', {'post_list': plist})

def post_detail(request, year, month, slug):
    post = get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})
