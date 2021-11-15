from django.urls import path
from . import views

app_name = "testapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('abouts/', views.abouts, name='abouts'),
    path('abouts/<int:about_id>/', views.about, name='about'),
    path('new_test/', views.new_test, name="new_test")
]
