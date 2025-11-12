from rest_framework import serializers

from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.serializers import ModelSerializer

from .models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')