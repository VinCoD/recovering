from django.shortcuts import redirect, render
from .models import Test
from .forms import TestForm

# Create your views here.

def abouts(request):
    abouts = Test.objects.all()
    context = {'abouts':abouts}
    return render(request, 'testapp/abouts.html', context)

def index(request):
    return render(request, 'testapp/base.html')



def about(request, about_id):
    about = Test.objects.get(id=about_id)
    news = about.new_set.order_by('-time_added')
    context = {"about":about, "news": news}

    return render(request, 'testapp/about.html', context)

def new_test(request):
    if request.method != 'POST':
        form = TestForm()
    else:
        form = TestForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('testapp:abouts')
    context = {'form': form}
    
    return render(request, 'testapp/new_test.html', context)


