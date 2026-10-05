from django.urls import path
from blog.views import PostList, post_detail

urlpatterns = [
    path('post-list', PostList.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
]