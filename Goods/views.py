from django.shortcuts import render
from . import models

def main(request):
    context = {}
    products = models.Product.objects.all()
    context['products'] = products

    return render(request, 'index.html', context)
