from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):
    context = {
        'dojos' : Dojo.objects.all()
    }
    return render(request, 'index.html', context)

def createDojo(request):
    Dojo.objects.create(
        name = request.POST['newDojo'],
        city = request.POST['city'],
        state =request.POST['state'],
        desc = request.POST['desc']
    )
    return redirect('/')

def createNinja(request):
    Ninja.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        dojo = request.POST['dojo.name']
    )