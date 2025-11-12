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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

class Profile(models.Model):
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    img = models.ImageField(upload_to='profile/', default='profile/default.jpg')

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self) -> str:
        return self.user.get_full_name()