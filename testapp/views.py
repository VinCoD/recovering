from django.shortcuts import render
from .models import Test

# Create your views here.

def abouts(request):
    tests = Test.objects.all()
    context = {'tests':tests}
    return render(request, 'testapp/abouts.html', context)

def index(request):
    return render(request, 'testapp/base.html')



def about(request, index_id):
    tests = Test.objects.get(id = index_id)
    news = tests.new_set.order_by('-time_added')
    context = {"news": news, "tests":tests}
    return render(request, 'testapp/about.html', context)


