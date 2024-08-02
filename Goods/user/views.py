from django.shortcuts import render, redirect
from Goods import models


def myCart(request):
    cart, _ = models.Cart.objects.get_or_create(
        author=request.user, 
        is_active=True)
    context = {}
    cart_products = models.CartProduct.objects.filter(cart = cart)
    context['cart']=cart
    context['cart_products'] = cart_products
    return render(request, 'back-office/user/cart.html', context)

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
    return redirect('/main/')

def substractProductFromCart(request, id):
    code = id
    quantity = request.GET['quantity']
    product_cart = models.CartProduct.objects.get(id=code)
    product_cart.quantity -= quantity
    product_cart.save()
    if not product_cart.quantity:
        product_cart.delete()
    return redirect('/')


def deleteProductCart(request, id):
    product_cart = models.CartProduct.objects.get(id=id)
    product_cart.delete()
    return redirect('/main/cart/list/')


def createOrder(request, id):
    cart = models.Cart.objects.get(
        id = id
        )
    
    cart_products = models.CartProduct.objects.filter(cart=cart)

    done_products = []

    for cart_product in cart_products:
        if cart_product.quantity <= cart_product.product.quantity:
            cart_product.product.quantity -= cart_product.quantity
            cart_product.product.save()
            done_products.append(cart_product)
        else:
            for product in done_products:
                product.product.quantity += product.quantity
                product.product.save()
            raise ValueError('Qoldiqda kamchilik')

    models.Order.objects.create(
        cart=cart,
        full_name = f"{request.user.first_name}, {request.user.last_name}",
        email = request.user.email,
        phone = request.GET['phone'],
        address = request.GET['address'],
        status = 1
        )
    cart.is_active = False
    cart.save()
    
    return redirect('/')
