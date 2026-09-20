from django.shortcuts import render, redirect
from .models import CartItem
from store.models import Product, Order

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    cart_item, created = CartItem.objects.get_or_create(
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


def cart(request):
    cart_items = CartItem.objects.all()

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total': total
    })


def increase_quantity(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')


def decrease_quantity(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()

    return redirect('cart')


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()

    return redirect('cart')


def checkout(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')

        print("NAME:", name)
        print("MOBILE:", mobile)
        print("ADDRESS:", address)
        print("CITY:", city)
        print("PINCODE:", pincode)

        Order.objects.create(
            name=name,
            mobile=mobile,
            address=address,
            city=city,
            pincode=pincode
        )

        return render(request, 'cart/order_success.html')

    return render(request, 'cart/checkout.html')