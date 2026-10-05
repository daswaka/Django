from django.urls import path
from organizer import views

urlpatterns = [
    path('tag-list/', views.tag_list, name='tag_list'),
    path('tag/<slug:slug>/',views.tag_detail, name='tag_detail'),
    path('startup-list/', views.startup_list, name='startup_list'),
    path('startup/<slug:slug>/', views.startup_detail, name='startup_detail'),
]