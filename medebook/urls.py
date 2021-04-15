"""medebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from users.views import leaderboard, register,profile,medinfo,blood_donation,profile_info,about, suggestion
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('home.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('register/',user_views.register,name='register'),
    path('profile/',user_views.profile,name='profile'),
    path('medinfo/',medinfo,name='medicalinfo'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('blood_donation/',blood_donation,name='blood_donation'),
    path('admin/', admin.site.urls),
    path('leaderboard/',leaderboard,name='leaderboard'),
    path('profile_info/',profile_info,name='profile_info'),
    path('about/',about,name='about'),
    path('suggestion/',suggestion,name='suggestion')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
