from django.urls import include, path
from app01 import views
from app01.views import ActiveUserView
urlpatterns = [
    path('home/', views.home,name='home'),
    path('introduction/', views.introduction,name='introduction'),
    path('introduction/coding/', views.coding,name='coding'),
    path('introduction/cgss/', views.cgss, name='cgss'),
    path('introduction/ele/', views.ele, name='ele'),


]