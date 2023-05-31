from django.contrib import admin
from .models import Header, Footer, HomePage, HomePageContent, TrendingGame, TrendingGameContent, TopGame, TopGameContent, TopCategory, TopCategoryContent, HomePageLastGet, HomePageLastPost
from .models import ShopTitle, ShopContentGenre, ShopContent, ProductDetailInfo
from .models import SignIn, SignUp, Verific, ForGuestUser
from .models import CartInfo, Cart, CartItem, UserOrder
from .models import WishlistInfo, Wishlist, WishlistItem
from .models import ProductReview

from .models import ContactGet, ContactContent, ContactPost

# Register your models here.

admin.site.register(Header)
admin.site.register(Footer)
admin.site.register(HomePage)
admin.site.register(HomePageContent)
admin.site.register(TrendingGame)
admin.site.register(TrendingGameContent)
admin.site.register(TopGame)
admin.site.register(TopGameContent)
admin.site.register(TopCategory)
admin.site.register(TopCategoryContent)
admin.site.register(HomePageLastGet)
admin.site.register(HomePageLastPost)
admin.site.register(ShopTitle)
admin.site.register(ShopContentGenre)
admin.site.register(ProductDetailInfo)
admin.site.register(ContactGet)
admin.site.register(ContactContent)
admin.site.register(ContactPost)
admin.site.register(SignIn)
admin.site.register(SignUp)
admin.site.register(Verific)
admin.site.register(WishlistInfo)
admin.site.register(Wishlist)
admin.site.register(WishlistItem)
admin.site.register(CartInfo)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(ProductReview)
admin.site.register(ForGuestUser)

@admin.register(ShopContent)
class AdminShopContent(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    list_display_links = ['name', 'category']
    search_fields = ['name']

@admin.register(UserOrder)
class AdminUserOrder(admin.ModelAdmin):
    list_display = ['name', 'game', 'count', 'date']
    list_display_links = ['name', 'game']
    search_fields = ['name', 'game']
    ordering = ['date']