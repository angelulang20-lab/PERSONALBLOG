from rest_framework import serializers

from django.shortcuts import render
from rest_framework.serializers import ModelSerializer

from .models import *


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True, allow_null=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'Content', 'created_at', 'updated_at', 'category_name', 'author_username', 'image']
        read_only_fields = ['author', 'created_at', 'updated_at']
        extra_kwargs = {
            'category': {'required': False, 'allow_null': True}
        }