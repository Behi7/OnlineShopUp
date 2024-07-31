from django.shortcuts import render, redirect
from Goods import models

def wishList(request):
    wish_list = models.WishList.objects.filter(user=request.user)
    context = {}
    context['wish_list'] = wish_list
    return render(request, 'back-office/user/wishlist.html', context)

def addOrDelWish(request, id):
    product = models.Product.objects.get(id=id)
    wish, add = models.WishList.objects.get_or_create(product = product, user = request.user)
    if not add:
        wish.delete()
    return redirect('index')

def delWish(request, id):
    models.WishList.objects.get(id=id).delete()
    return redirect('wishList')





    
