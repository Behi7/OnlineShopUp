# list ---
# detail ---
# create ---
# update ---
# delete ---

from Goods import models
from django.shortcuts import render, redirect


def listProduct(request):
    queryset = models.Product.objects.all()
    context = {}
    context['queryset'] = queryset
    return render(request, 'back-office/product/list.html',context)


def detailProduct(request, id):
    queryset = models.Product.objects.get(id=id)
    context = {}
    print(models.ProductImg.objects.filter(product=queryset))
    context['queryset'] = queryset
    context['images'] = models.ProductImg.objects.filter(product=queryset)
    return render(request, 'back-office/product/detail.html',context)


def createProduct(request):
    context = {}
    context['categorys'] = models.Category.objects.all()
    if request.method == 'POST':
        # way 1
        # category_id = request.POST['category_id']
        # category = models.Category.objects.get(id=category_id)
        # product = models.Product.objects.create(
        #     name = request.POST['name'],
        #     quantity = request.POST['quantity'],
        #     price = request.POST['price'],
        #     category = category, 
        #     description = request.POST['description']
        # )
        # way 2
        product = models.Product.objects.create(
            name = request.POST['name'],
            quantity = request.POST['quantity'],
            price = request.POST['price'],
            category_id = request.POST['category_id'], 
            description = request.POST['description']
        )

        images = request.FILES.getlist('images')

        for image in images:
            models.ProductImg.objects.create(
                img = image,
                product = product
            )
    return render(request, 'back-office/product/create.html', context)


def deleteProduct(request, id):
    models.Product.objects.get(id=id).delete()
    return redirect('listProduct')

def productlists(request):
    alls = models.Product.objects.all()
    context = {}
    context['products'] = alls
    try:
        wishProducts = models.WishList.objects.filter(user = request.user)
        for wish in wishProducts:
            for product in alls:
                if wish.product.id == product.id:
                    product.is_active = True
    except:
        ...
    return render(request, 'shop.html', context)

def storyEnter(request):
    list_e = models.EnterProduct.objects.all()
    context = {'list_e': list_e}
    return render(request, 'back-office/product/storyenter.html', context)

def createEnter(request):
    queryset = models.Product.objects.all()
    context = {}
    context['queryset'] = queryset
    if request.method == "POST":
        models.EnterProduct.objects.create(
            product = request.POST['product'],
            enter_quantity = request.POST['enter_quantity'],
            old_quantity = models.Product.objects.get(id = request.POST['product']).quantity,
            info = request.POST['info']
        )

    return render(request, 'back-office/product/createenter.html', context)

def updateEnter(request):
    if request.method == "POST":
        models.EnterProduct.objects.update(
            product = request.POST['product'],
            enter_quantity = request.POST['enter_quantity'],
            old_quantity = models.Product.objects.get(id = request.POST['product']).quantity,
            info = request.POST['info']
        )

    return render(request, 'back-office/product/updateenter.html')

def enterDelete(request, id):
    models.EnterProduct.objects.get(id=id).delete()
    return redirect('enter')

def addProductToCart(request, id):
    quantity = request.GET.get('quantity', 1)
    product = models.Product.objects.get(id=id)
    cart, _ = models.Cart.objects.get_or_create(author=request.user, is_active=True)
    try:
        cart_product = models.CartProduct.objects.get(cart=cart.id, product=product.id)
        cart_product.quantity+=quantity
        cart_product.save()
    except:
        cart_product = models.CartProduct.objects.create(
            product=product, 
            cart=cart,
            quantity=quantity
        )
    return redirect('/main/back-office/product/shop')

