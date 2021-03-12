from django.shortcuts import render

from .models import Property

# Create your views here.
def index(request):
    return render(request, 'property_website/index.html', {
        "properties": Property.objects.all()
    })