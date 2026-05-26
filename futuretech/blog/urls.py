from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts_menu, name='menu'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('admin/posts/', views.admin_posts, name='admin_posts'),
    path('admin/posts/new/', views.admin_post_create, name='admin_post_create'),
    path('admin/posts/<int:post_id>/edit/', views.admin_post_edit, name='admin_post_edit'),
]
