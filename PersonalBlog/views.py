from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView

from .models import *
from .serializer import PostSerializer

# Create your views here.
class PostListView(ListCreateAPIView):
    queryset = Post.objects.filter(is_published=True, post_type='PersonalBlog').order_by('-created_at')
    serializer_class = PostSerializer 

