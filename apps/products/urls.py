from django.urls import path
from .views import (
    home,
    single_product,
    product_info_2,
    product_info,
    blog,
    about_us,
    wishlist,
    contact,
    shoppingcart,
    posts,
    delete,
    update,
    delete_wishlist,
    user_profile,
    user_edit_page,
    checkout
)

urlpatterns = [
    path('', home, name='home'),
    path('<int:pk>/', single_product, name='single_product'),
    path('shopleftcolumn/', product_info , name='shopleftcolumn'),
    path('shopcolumn/', product_info_2 , name='shopcolumn2'),
    path('blog/', blog , name='blog'),
    path('about/', about_us , name='about_us'),
    path('wishlist/', wishlist , name='wishlist'),
    path('contact/', contact , name='contact'),
    path('shoppingcart/', shoppingcart , name='shoppingcart'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('delete_wishlist/<int:pk>/', delete_wishlist, name='delete_wishlist'),
    path('userprofile/', user_profile, name='userprofile'),
    path('userinfoedit/<int:pk>/', user_edit_page, name='userinfoedit'),
    path('checkout', checkout, name='checkout'),



    path('posts/', posts , name='posts'),
    
]

