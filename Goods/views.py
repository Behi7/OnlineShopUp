from django.shortcuts import render
from . import models

def main(request):
    context = {}
    products = models.Product.objects.all()
    context['products'] = products
    context['banners']= models.Banner.objects.filter(is_active = True)[:5]
    context['info'] = models.Info.objects.last()
    try:
        wishProducts = models.WishList.objects.filter(user = request.user)
        for wish in wishProducts:
            for product in products:
                if wish.product.id == product.id:
                    product.is_active = True
    except:
        ...
    return render(request, 'index.html', context)

def createInfo(request):
    if request.method == 'POST':
        models.Info.objects.create(
        phone = request.POST['phone'],
        region = request.POST['region'],
        text = request.POST['text'],
        email = request.POST['email'],
        facebook = request.POST['facebook'],
        twitter =request.POST['twitter'],
        linking = request.POST['linking'],
        )
    return render(request, 'info.html')


