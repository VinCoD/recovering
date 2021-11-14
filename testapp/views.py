from django.shortcuts import render
from .models import Test

# Create your views here.

def abouts(request):
    tests = Test.objects.all()
    context = {'tests':tests}
    return render(request, 'testapp/abouts.html', context)

def index(request):
    return render(request, 'testapp/base.html')



def about(request, about_id):
    about = Test.objects.get(id=about_id)
    news = about.new_set.order_by('-time_added')
    context = {"about":about, "news": news}

    return render(request, 'testapp/about.html', context)


