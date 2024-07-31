from django.shortcuts import render
from . import models

def main(request):
    context = {}
    products = models.Product.objects.all()
    context['products'] = products
    context['banners']= models.Banner.objects.filter(is_active = True)[:5]
    context['info'] = models.Info.objects.last()
    wishProducts = models.WishList.objects.filter(user = request.user)
    for wish in wishProducts:
        for product in products:
            if wish.product.id == product.id:
                product.is_active = True
    return render(request, 'index.html', context)


