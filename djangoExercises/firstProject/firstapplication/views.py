from django.shortcuts import render
from .models import Name
# Create your views here.
def home(request):
    objs = Name.objects.all
    context = {'people' : objs}
    return render(request, 'firstapplication/home.html', context)    