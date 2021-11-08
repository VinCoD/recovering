from django.shortcuts import render
from .models import Test

# Create your views here.

def index(request):
    tests = Test.objects.all()
    context = {'tests':tests}
    return render(request, 'testapp/index.html', context)

def about(request):
    return render(request, 'testapp/about.html')
