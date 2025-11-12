from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .models import *
from .serializer import PostSerializer


# Create your views here.
# Blog views (public posts)
class BlogListView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Post.objects.filter(
            post_type='PersonalBlog'
        ).order_by('-created_at')

class BlogListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Post.objects.filter(
            author=self.request.user,
            post_type='PersonalBlog'
        ).order_by('-created_at')
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post_type='PersonalBlog')

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Post.objects.filter(
            author=self.request.user,
            post_type='PersonalBlog'
        )

# Journal views (private posts)
class JournalListView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Post.objects.filter(
            author=self.request.user,
            post_type='journal'
        ).order_by('-created_at')

class JournalListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Post.objects.filter(
            author=self.request.user,
            post_type='journal'
        ).order_by('-created_at')
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post_type='journal')

class JournalDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Post.objects.filter(
            author=self.request.user,
            post_type='journal'
        )