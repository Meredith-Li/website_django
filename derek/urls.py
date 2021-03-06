"""derek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path,re_path
from app01 import views
from app01.views import ActiveUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/',include('app01.urls')),
    path('register/', views.test_register, name='register'),
    path('under_construction/', views.under_construction, name='under_construction'),
    path('login/', views.login, name='login'),
    re_path('active/(?P<active_code>.*)/(?P<email>.*)/', ActiveUserView.as_view(), name="user_active"),
]


