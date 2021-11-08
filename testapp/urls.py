from django.urls import path
from . import views

app_name = "testapp"
urlpatterns = [
    path('home', views.index, name='index'),
    path('home/<int:index_id>/', views.about, name='about')
]
