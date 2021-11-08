from django.urls import path
from . import views

app_name = "testapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('abouts/', views.abouts, name='abouts'),
    path('abouts/<int:index_id>/', views.about, name='about'),
]
