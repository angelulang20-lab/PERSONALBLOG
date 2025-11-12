from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import DjangoModelPermissions
from rest_framework import generics

from .models import *
from .serializer import PostSerializer


# Create your views here.
class PostListView(ListCreateAPIView):
    queryset = Post.objects.filter(is_published=True, post_type='PersonalBlog').order_by('-created_at')
    serializer_class = PostSerializer 
    permission_classes = [DjangoModelPermissions]

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

