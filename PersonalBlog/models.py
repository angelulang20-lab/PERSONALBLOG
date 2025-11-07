from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 


class Category (models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    POST_TYPES = (
        ('PersonalBlog', 'Blog Post'),
        ('journal', 'Journal Entry'),
    )

    title = models.CharField(max_length=200)
    Content= models.TextField(null=True)
    post_type = models.CharField(max_length=50, choices=POST_TYPES, default='PersonalBlog')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
        
class Comment(models.Model):
    description =  models.CharField(max_length=250)
    