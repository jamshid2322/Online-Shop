from audioop import reverse
import decimal
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from apps.users.models import User
from apps.users.views import user_login

# Internal modules
from apps.products.abstract_base import CustomAbstactBase

from apps.products.models import (
    Category,
    Color,
    Product,
    CardItem,
    Like,
    StarToProduct
)

def home(request):
    products = Product.objects.order_by('-id')
    # carditem = CardItem.objects.filter(user=request.user)
    shopping_card = CardItem.objects.filter(user_id=request.user.id)
        


    if request.method == 'POST':
        post_action = request.POST.get('post_action')
        if post_action == 'like':
         add_like(request.user)


    context = {
        'products': products,
        # 'carditem': carditem,
        'total_price' : sum([(card.product.price * card.qty) for card in shopping_card])
        
    }
    return render(request, 'index.html', context)


def single_product(request, pk):
    carditem = CardItem.objects.filter(user=request.user)
    product = Product.objects.filter(id=pk).last()
    if not product:
        raise Http404
    
    user_star = StarToProduct.objects.filter(user_id=request.user.id , product_id=pk).last()
    shopping_card = CardItem.objects.filter(user_id=request.user.id)




    if request.method == 'POST':
        post_action = request.POST.get('post_action')
        if post_action == 'star':
            qty = request.POST.get("qty")
            add_star(request.user, pk ,qty=1)
            
        elif post_action == 'card':
            qty = request.POST.get("qty")
            add_cart(request.user, int(qty), pk)
        elif post_action == 'like':
            add_like(request.user, pk)

    context = {
        'product': product,
        'star' : user_star,
        'total_price' : sum([(card.product.price * card.qty) for card in shopping_card]),
        'carditem': carditem,
    }
    return render(request, 'single-product.html', context)




def add_cart(user, qty, pk ):
    if not user.is_authenticated:
        print(True)
        return redirect('user_login')
    else:
        user_card, _ = CardItem.objects.get_or_create(user_id=user.id, product_id=pk)
        user_card.qty += qty
        user_card.save()
        return redirect('single_product', pk=pk)


def add_like(user, pk):
    if not user.is_authenticated:
        pass
    user_card, _ = Like.objects.get_or_create(user_id=user.id, product_id=pk)
    user_card.liked = not user_card.liked
    user_card.save()
    return redirect('single_product', pk=pk)

def add_star(user, pk, qty):
    if not user.is_authenticated:
        pass
    user_star, _ = StarToProduct.objects.get_or_create(user_id=user.id, product_id=pk)
    user_star.star = qty
    user_star.save()
    return redirect('single_product', pk=pk)


def product_info_2(request):
    return render(request , 'shop-4-column.html')

def blog(request):
    return render(request , 'blog-details-left-sidebar.html')

def about_us(request):
    return render(request , 'about-us.html')

def contact(request):
    return render(request , 'contact.html')

def wishlist(request):
    wishlist = Like.objects.filter(user=request.user)
    carditem = CardItem.objects.filter(user=request.user)
    shopping_card = CardItem.objects.filter(user_id=request.user.id)

    context = {
            'wishlist': wishlist,
            'carditem': carditem,
            'total_price' : sum([(card.product.price * card.qty) for card in shopping_card]),
            
        }

    
    return render(request ,'wishlist.html' , context)

def product_info(request):

    products = Product.objects.all()
        
    context = {
        'products': products,
    }
    return render(request , 'shop-left-sidebar.html' , context)

def shoppingcart(request):
  
    carditem = CardItem.objects.filter(user=request.user)
    shopping_card = CardItem.objects.filter(user_id=request.user.id)
    # if not product:
    #     raise Http404

   
    context = {
        'carditem': carditem,
        'total_price' : sum([(card.product.price * card.qty) for card in shopping_card])
        
    }

    return render(request, 'shopping-cart.html', context)


def delete(request, pk):
    items = CardItem.objects.get(id=pk)

    context = {
        'items' : items
    }

    if request.method == 'POST':
        items.delete()
        return redirect("shoppingcart")
 
    return render(request, 'delete.html', context)
    
def posts(request):

    
    category = Category.objects.all()
    color = Color.objects.all()

    context = {
            
            'category' : category,
            'color' : color       
        }

    if request.method == 'POST':
        category = request.POST.get("category")
        productname = request.POST['productname']
        productprice = request.POST['productprice']
        productprice = request.POST['productprice']
        discountprice = request.POST['discountprice']
        description = request.POST['description']
        color = request.POST.get('color')

        new = Product.objects.create(
            name=productname,
            price=productprice,
            discount=discountprice,
            description=description,
            
            

        )

        new = Product.objects.set(
            colors=color,
            category=category
            
        )
        return redirect('home')
    
    
    return render(request, 'posts.html', context)

def update(request, pk):


    items = CardItem.objects.get(id=pk)
    context = {
        'items': items
    }

    if request.method == 'POST':
        data = request.POST
        qty1 = data.get('qty')
        items.qty = qty1
        items.save()
        return redirect('shoppingcart')
    

    return render(request, 'edit.html', context)



def delete_wishlist(request, pk):
    items = Like.objects.get(id=pk)

    context = {
        'items' : items
    }

    if request.method == 'POST':
        items.delete()
        return redirect("wishlist")
 
    return render(request, 'delete.html', context)


def user_profile(request):
    carditem = CardItem.objects.filter(user=request.user)
    shopping_card = CardItem.objects.filter(user_id=request.user.id)


    context = {
       
        'carditem': carditem,
        'total_price' : sum([(card.product.price * card.qty) for card in shopping_card])
        
    }


    return render(request , 'user-profile.html', context)


def user_edit_page(request, pk):

    user_info = User.objects.get(id=pk)


    context = {
        'user_info': user_info
    }


    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        phone_number = data.get('phone_number')

        user_info.first_name = first_name
        user_info.last_name = last_name
        user_info.phone_number = phone_number
        user_info.save()
        
        return redirect('home')






    return render(request , 'user-edit-page.html' , context)



def checkout(request):

    

   
    return render(request , 'checkout.html')