from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),

    path('create/', views.create, name='create'),

    path('<int:post_id>/comments/create', views.comments_create, name='comments_create'),
    path('<int:post_id>/comments/<int:id>/delete', views.comments_delete, name='comments_delete'),

]