from django.shortcuts import render, redirect
from .forms import SubscribeModelForm, ContactModelForm
from .models import Header, Footer, HomePage, HomePageContent, TrendingGame, TrendingGameContent, TopGame, TopGameContent, TopCategory, TopCategoryContent, HomePageLastGet, HomePageLastPost
from .models import ShopTitle, ShopContentGenre, ShopContent, ProductDetailInfo
from .models import ContactGet, ContactContent, ContactPost
from .models import SignIn, SignUp, Verific, ForGuestUser
from .models import WishlistInfo, Wishlist, WishlistItem
from .models import ProductReview
from .models import CartInfo, Cart, CartItem, UserOrder
import random
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse  
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  
from django.contrib.auth import get_user_model

# Create your views here.

def double_content():
    header = Header.objects.all()[0]
    footer = Footer.objects.all()[0]
    detail_page = random.choice(ShopContent.objects.all())
    for_guest_user = ForGuestUser.objects.all()[0]
    return [header, footer, detail_page.slug, for_guest_user]

def index(request):
    if request.method == 'POST':
        form = SubscribeModelForm(request.POST)
        if form.is_valid():
            HomePageLastPost.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = SubscribeModelForm()
    home_page = HomePage.objects.all()[0]
    home_page_content = HomePageContent.objects.all()
    trending_games = TrendingGame.objects.all()[0]
    trending_games_content = TrendingGameContent.objects.all()
    top_games = TopGame.objects.all()[0]
    top_games_content = TopGameContent.objects.all()
    top_categories = TopCategory.objects.all()[0]
    top_categories_content = TopCategoryContent.objects.all()
    home_page_last_get = HomePageLastGet.objects.all()[0]
    return render(request, 'main/index.html', context={
        'link':'index',
        'header':double_content()[0],
        'footer':double_content()[1],
        'home_page':home_page,
        'home_page_content':home_page_content,
        'trending_games':trending_games,
        'trending_games_content':trending_games_content,
        'top_games':top_games,
        'top_games_content':top_games_content,
        'top_categories':top_categories,
        'top_categories_content':top_categories_content,
        'home_page_last_get':home_page_last_get,
        'form':form,
        'detail_page':double_content()[2],
    })

def shop(request):
    shop_title = ShopTitle.objects.all()[0]
    shop_content_genre = ShopContentGenre.objects.all()
    shop_content = ShopContent.objects.all().order_by(random.choice(['category', 'img', 'price', 'name', 'slug', 'text', 'tags', 'description']))
    
    return render(request, 'main/shop.html', context={
        'link':'shop',
        'header':double_content()[0],
        'footer':double_content()[1],
        'shop_title':shop_title,
        'shop_content_genre':shop_content_genre,
        'shop_content':shop_content,
        'detail_page':double_content()[2],
    })

def product_detail(request, slug):
    one_game = ShopContent.objects.get(slug=slug)
    product_detail_info = ProductDetailInfo.objects.all()[0]
    shop_content = ShopContent.objects.all().order_by(random.choice(['category', 'img', 'price', 'name', 'slug', 'text', 'tags', 'description']))
    for_guest_user = ForGuestUser.objects.all()[0]

    return render(request, 'main/product-details.html', context={
        'link':'product_detail',
        'header':double_content()[0],
        'footer':double_content()[1],
        'one_game':one_game,
        'product_detail_info':product_detail_info,
        'shop_content':shop_content,
        'detail_page':double_content()[2],
        'for_guest_user':double_content()[3],
    })




def contact(request):
    contact_get = ContactGet.objects.all()[0]
    contact_content = ContactContent.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            ContactPost.objects.create(**form.cleaned_data)
            return redirect('contact')
    else:
        form = ContactModelForm()
    return render(request, 'main/contact.html', context={
        'link':'contact',
        'header':double_content()[0],
        'footer':double_content()[1],
        'contact_get':contact_get,
        'contact_content':contact_content,
        'detail_page':double_content()[2],
    })


def verific(request):
    verific = Verific.objects.all()[0]
    return render(request, 'main/verific.html', context={
        'header':double_content()[0],
        'footer':double_content()[1],
        'verific':verific,
        'detail_page':double_content()[2],
    })

def wishlist(request):
    if request.user.is_authenticated:
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        wishlistitems = wishlist.wishlistitems.all()
    else:
         wishlist = ''
         wishlistitems = ''
    wishlist_info = WishlistInfo.objects.all()[0]
    
    return render(request, 'main/wishlist.html', context={
        'link':'wishlist',
        'header':double_content()[0],
        'footer':double_content()[1],
        'detail_page':double_content()[2],
        'wishlist_info':wishlist_info,
        'wishlist':wishlist,
        'items':wishlistitems,
        'for_guest_user':double_content()[3],
    })

def add_to_wishlist(request):
	if request.method == 'POST':
		prod_id = request.POST.get('id')
		product = ShopContent.objects.get(id=prod_id)
		if request.user.is_authenticated:
			wishlist, created = Wishlist.objects.get_or_create(user=request.user)
			wishlistitem, created = WishlistItem.objects.get_or_create(wishlist=wishlist, products=product)
			wishlistitem.save()
	return redirect('index')

def wishlist_product(request):
    if request.method == 'POST':
        prod_id = request.POST.get('id')
        products = ShopContent.objects.get(id=prod_id)
        WishlistItem.objects.filter(products=products).delete()
    return redirect('wishlist')


def cart(request):
    cart_list_sum = 0
        
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cartitems = cart.cartitems.all()
    else:
         cart = ''
         cartitems = ''
    cart_info = CartInfo.objects.all()[0]
    for i in cartitems:
        if i.product.to_check:
            cart_list_sum += int(i.count1) * int(i.product.new_price)
        else:
            cart_list_sum += int(i.count1) * int(i.product.price)
            
    return render(request, 'main/cart.html', context={
        'link':'cart',
        'header':double_content()[0],
        'footer':double_content()[1],
        'cart_info':cart_info,
        'detail_page':double_content()[2],
        'carts':cart,
        'items':cartitems,
        'cart_list_sum':cart_list_sum,
        'for_guest_user':double_content()[3],
    })

def add_to_cart(request):
    if request.method == 'POST':
        count2 = request.POST.get('amount')
        prod_id = request.POST.get('id')
        product = ShopContent.objects.get(id=prod_id)
        # if CartItem.objects.filter(have='True'):
        #     CartItem.objects.filter(have='True').update(count1=count2)
        #     cartitem = CartItem.objects.all()

        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
            try:
                cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product, have='True')
                cartitem.count1 += int(count2)
                if cartitem.count1 > 20:
                    cartitem.count1 = 20
                cartitem.save()
            except:
                cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product, count1=int(count2))
                cartitem.save()


    return redirect('index')

def cart_product(request):
    if request.method == 'POST':
        prod_id = request.POST.get('id')
        products = ShopContent.objects.get(id=prod_id)
        prod_count = request.POST.get('count')
        if int(prod_count) == CartItem.objects.get(product=products).count1:
            CartItem.objects.filter(product=products).delete()
        else:
            cart, created = Cart.objects.get_or_create(user=request.user)
            cartitem, created = CartItem.objects.get_or_create(cart=cart, product=products)
            cartitem.count1 -= int(prod_count)
            cartitem.save()
       
    return redirect('cart')

def cart_all_product(request):
    if request.method == 'POST':
        func = request.POST.get('all_product')
        cart, created = Cart.objects.get_or_create(user=request.user)
        items = cart.cartitems.all()
        if func == 'Remove':
            items.delete()
        elif func == 'Checkout':
            for i in items:
                UserOrder.objects.create(name=request.user.username, game=i.product.name, count=i.count1)
            items.delete()

    return redirect('cart')


def product_review(request):
    if request.method == 'POST':
        game_review = request.POST.get('game_review_text')
        prod_id = request.POST.get('game_product')
        product = ShopContent.objects.get(id=prod_id)
        ProductReview.objects.get_or_create(user_review=request.user, user_product=product, user_text=game_review, to_check=False)

    return redirect('shop')









def signup(request):
    sign_up = SignUp.objects.all()[0]
    if request.method == 'POST':  
        form = NewUserForm(request.POST)  
        if form.is_valid():  
            user = form.save(commit=False)  
            user.is_active = False  
            user.save()  
            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('main/acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send() 
            return redirect('verific')
    else:  
        form = NewUserForm()  
    return render(request, 'main/register.html', {
         'form': form,
         'header':double_content()[0],
         'footer':double_content()[1],
         'sign_up':sign_up,
         'detail_page':double_content()[2],
         })  


def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return redirect('index') 
    else:  
        return HttpResponse('Activation link is invalid!')  



def login_request(request):
    
    
 sign_in = SignIn.objects.all()[0]
 if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect("index")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        messages.error(request,"Invalid username or password.")
 form = AuthenticationForm()
 return render(request=request, template_name="main/login.html", context={
 "login_form":form,
 'header':double_content()[0],
 'footer':double_content()[1],
 'sign_in':sign_in,
 'detail_page':double_content()[2],
})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")