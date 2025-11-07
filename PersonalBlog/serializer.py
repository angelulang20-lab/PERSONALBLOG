from rest_framework import serializers

from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.serializers import ModelSerializer

from .models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        # template_name = 'post_list'
        # context_object_name = 'posts'
        # paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(is_published=True , post_type='PersonalBlog').order_by('-created_at')
    
# class PostDetailView(serializers.ModelSerializer):
#         class Meta:
#             model = Post
#             template_name = 'post_detail'
#             context_object_name = 'post'
        
# class PostCreateView(serializers.ModelSerializer):
#         class Meta:
#             model = Post
#             template_name = 'post_form'
#             fields = ['title', 'category', 'content', 'post_type', 'is_published']
            
#             def form_valid(self, form):
#                 form.instance.Author = self.request.user
#                 return super().form_valid(form)
        
# class PostUpdateView(serializers.ModelSerializer):
#         class Meta:
#             model = Post
#             template_name = 'post_form'
#             fields = ['title', 'category', 'content', 'post_type', 'is_published']
        
            
#             def test_func(self):
#                 post = self.get_object()
#                 return self.request.user == post.Author
        
# class PostDeleteView(serializers.ModelSerializer):
#         class Meta:
#             model = Post
#             template_name = 'post_confirm_delete.html'
#             success_url = '/'
            
#             def test_func(self):
#                 post = self.get_object()
#                 return self.request.user == post.Author

        