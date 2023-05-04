from django.urls import path
from .views import (
    BlogListView, 
    BlogDetailView, 
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView
)

app_name = 'pages'

urlpatterns = [
    path('',BlogListView.as_view(), name='bloglist'),
    path('blog/detail/<int:pk>/',BlogDetailView.as_view(), name='blogdetail'),
    path('blog/create/',BlogCreateView.as_view(), name='blogcreate'),
    path('blog/update/<int:pk>',BlogUpdateView.as_view(), name='blogupdate'),
    path('blog/delete/<int:pk>',BlogDeleteView.as_view(), name='blogdelete'),
]