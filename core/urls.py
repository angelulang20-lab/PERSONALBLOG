"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static
from PersonalBlog import views

from PersonalBlog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    

    path('api/blogs/', BlogListView.as_view(), name='user-blogs'),
    path('api/blogs/create/', BlogListCreateView.as_view(), name='create-blogs'),
    path('api/blogs/<int:pk>/', BlogDetailView.as_view(), name='crud-blogs'),
    
    path('api/entries/', JournalListView.as_view(), name='user-entries'),
    path('api/entries/create/', JournalListCreateView.as_view(), name='create-entries'),
    path('api/entries/<int:pk>/', JournalDetailView.as_view(), name='crud-entries'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)