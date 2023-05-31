from typing import Any
from django.db import models
from django.contrib.auth.models import User  

# Create your models here.

class Header(models.Model):

    img = models.ImageField('Logo Image', upload_to='images')
    path1 = models.CharField('Path 1', max_length=50)
    path2 = models.CharField('Path 2', max_length=50)
    path3 = models.CharField('Path 3', max_length=50)
    path4 = models.CharField('Path 4', max_length=50)
    path5 = models.CharField('Path 5', max_length=50)
    path6 = models.CharField('Path 6', max_length=50)
    path7 = models.CharField('Path 7', max_length=50)

    class Meta:

        verbose_name = 'Header'
        verbose_name_plural = 'Header'

class Footer(models.Model):

    text = models.TextField('Copyright')
    name = models.CharField('Designer Name', max_length=50)
    name_link = models.URLField('Designer Name Link')
    
    class Meta:

        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'

class HomePage(models.Model):

    title = models.CharField('Title', max_length=50)
    subtitle = models.CharField('Subtitle', max_length=60)
    text = models.TextField('Text')
    btn_name = models.CharField('Button Name', max_length=30)
    price = models.CharField('Price', max_length=10)
    procent = models.CharField('Procent', max_length=10)
    img = models.ImageField('Image', upload_to='images')

    class Meta:

        verbose_name = 'Home Page'
        verbose_name_plural = 'Home Page'

class HomePageContent(models.Model):

    img = models.ImageField('Image', upload_to='images')
    title = models.CharField('Title', max_length=50)

class TrendingGame(models.Model):

    title = models.CharField('Title', max_length=50)
    subtitle = models.CharField('Subtitle', max_length=60)
    btn_name = models.CharField('Button Name', max_length=30)
    icon = models.CharField('Icon', max_length=50)

class TopGame(models.Model):

    title = models.CharField('Title', max_length=50)
    subtitle = models.CharField('Subtitle', max_length=60)
    btn_name1 = models.CharField('Button Name 1', max_length=30)
    btn_name2 = models.CharField('Button Name 2', max_length=30)

    
class TopCategory(models.Model):

    title = models.CharField('Title', max_length=50)
    subtitle = models.CharField('Subtitle', max_length=60)
    
    class Meta:

        verbose_name = 'TopCategory'
        verbose_name_plural = 'TopCategories'



class TopCategoryContent(models.Model):

    genre = models.CharField('Genre', max_length=50)
    img = models.ImageField('Image', upload_to='images')

class HomePageLastGet(models.Model):

    title1 = models.CharField('Title 1', max_length=50)
    subtitle1 = models.CharField('Subtitle 1', max_length=60)
    colored_word1 = models.CharField('Colored Word 1', max_length=40)
    text = models.TextField('Text')
    btn_name1 = models.CharField('Button Name 1', max_length=40)
    img = models.ImageField('Image', upload_to='images')
    title2 = models.CharField('Title 2', max_length=50)
    subtitle2 = models.CharField('Subtitle 2', max_length=60)
    colored_word2 = models.CharField('Colored Word 2', max_length=40)
    btn_name2 = models.CharField('Button Name 2', max_length=40)

    class Meta:

        verbose_name = 'Home Page Last GET'
        verbose_name_plural = 'Home Page Last GET'

class HomePageLastPost(models.Model):

    user_email = models.EmailField('User Email')
    
    class Meta:

        verbose_name = 'Home Page Last POST'
        verbose_name_plural = 'Home Page Last POST'

    def __str__(self) -> str:
        return self.user_email
    
class ShopTitle(models.Model):

    title = models.CharField('Title', max_length=40)
    subtitle = models.CharField('Subtitle', max_length=60)
        
    class Meta:

        verbose_name = 'Shop Title'
        verbose_name_plural = 'Shop Title'

class ShopContentGenre(models.Model):

    genre = models.CharField('Genre', max_length=50)
    tag = models.CharField('Filter Tag', max_length=30)

    def __str__(self) -> str:
        return self.genre


class ShopContent(models.Model):

    category = models.ForeignKey(ShopContentGenre, on_delete=models.CASCADE, related_name='cat_prod')
    img = models.ImageField('Image', upload_to='images')
    price = models.CharField('Price', max_length=10)
    new_price = models.CharField('New Price', max_length=10, blank=True)
    name = models.CharField('Name', max_length=50)
    to_check = models.BooleanField('For New Price', blank=True)
    slug = models.SlugField('Slug', unique=True, blank=True)
    text = models.TextField('About Game')
    tags = models.CharField('Game Tags', max_length=50)
    description = models.TextField('Description')

    def __str__(self) -> str:
        return self.name

class ProductDetailInfo(models.Model):

    cart_btn = models.CharField('Cart Button', max_length=40)
    wish_btn = models.CharField('WishList Button', max_length=40)
    subtitle1 = models.CharField('Subtitle 1', max_length=50)
    subtitle2 = models.CharField('Subtitle 2', max_length=50)
    title1 = models.CharField('Title 1', max_length=50)
    title2 = models.CharField('Title 2', max_length=50)
    subtitle3 = models.CharField('Subtitle 3', max_length=50)
    subtitle4 = models.CharField('Subtitle 4', max_length=50)
    btn_name = models.CharField('Button Name', max_length=40)
    review_btn = models.CharField('Review Button Name', max_length=40)


class ContactGet(models.Model):

    general_title = models.CharField('General Title', max_length=40)
    general_subtitle = models.CharField('General Subtitle', max_length=50)
    title = models.CharField('Content Title', max_length=50)
    subtitle = models.CharField('Subtitle', max_length=50)
    text = models.TextField('Text')
    inp1 = models.CharField('Placeholder 1', max_length=50)
    inp2 = models.CharField('Placeholder 2', max_length=50)
    inp3 = models.CharField('Placeholder 3', max_length=50)
    inp4 = models.CharField('Placeholder 4', max_length=50)
    inp5 = models.CharField('Placeholder 5', max_length=50)
    btn_name = models.CharField('Button Name', max_length=50)

    class Meta:

        verbose_name = 'Contact GET'
        verbose_name_plural = 'Contact GET'

class ContactContent(models.Model):

    title = models.CharField('Title', max_length=50)
    subtitle = models.CharField('Subtitle', max_length=200)

    def __str__(self) -> str:
        return self.title

class ContactPost(models.Model):

    user_name = models.CharField('Username', max_length=50)
    user_surname = models.CharField('Surname', max_length=50)
    user_email = models.EmailField('Email')
    subject = models.CharField('Subject', max_length=100)
    message = models.TextField('Message')
    
    class Meta:

        verbose_name = 'Contact POST'
        verbose_name_plural = 'Contact POST'

    def __str__(self) -> str:
        return self.user_name


class TrendingGameContent(models.Model):

    trending_game = models.ForeignKey(ShopContent, on_delete=models.CASCADE)

class TopGameContent(models.Model):

    top_games = models.ForeignKey(ShopContent, on_delete=models.CASCADE)

class SignIn(models.Model):

    title = models.CharField('Title', max_length=50)
    subtitle1 = models.CharField('Subtitle 1', max_length=50)
    subtitle2 = models.CharField('Subtitle 2', max_length=50)
    btn_name = models.CharField('Button Name', max_length=40)
    text = models.TextField('Text')
    link_name = models.CharField('Link Name', max_length=50)

    class Meta:

        verbose_name = 'Sign In'
        verbose_name_plural = 'Sign In'

class SignUp(models.Model):
    
    title = models.CharField('Title', max_length=50)
    subtitle1 = models.CharField('Subtitle 1', max_length=50)
    subtitle2 = models.CharField('Subtitle 2', max_length=50)
    subtitle3 = models.CharField('Subtitle 3', max_length=50)
    subtitle4 = models.CharField('Subtitle 4', max_length=50)
    subtitle5 = models.CharField('Subtitle 5', max_length=50)
    subtitle6 = models.CharField('Subtitle 6', max_length=50)
    btn_name = models.CharField('Button Name', max_length=40)
    text = models.TextField('Text')
    link_name = models.CharField('Link Name', max_length=50)
    rule1 = models.CharField('Rule 1', max_length=100)
    rule2 = models.CharField('Rule 2', max_length=100)
    rule3 = models.CharField('Rule 3', max_length=100)
    rule4 = models.CharField('Rule 4', max_length=100)
    rule5 = models.CharField('Rule 5', max_length=100)
    
    class Meta:

        verbose_name = 'Sign Up'
        verbose_name_plural = 'Sign Up'

class Verific(models.Model):

    img = models.ImageField('Image', upload_to='images')
    title1 = models.CharField('Title 1', max_length=100)
    title2 = models.CharField('Title 2', max_length=100)
    text = models.TextField('Text')

    class Meta:

        verbose_name = 'Verific'
        verbose_name_plural = 'Verific'

class WishlistInfo(models.Model):

    title1 = models.CharField('Title 1', max_length=50)
    title2 = models.CharField('Title 2', max_length=50)
    del_btn = models.CharField('Delete Button', max_length=40)
    cart_btn = models.CharField('Cart Button', max_length=40)

class Wishlist(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

class WishlistItem(models.Model):

    products = models.ForeignKey(ShopContent, on_delete=models.CASCADE, related_name='wish_items')
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name='wishlistitems')

class CartInfo(models.Model):

    title1 = models.CharField('Title 1', max_length=50)
    title2 = models.CharField('Title 2', max_length=50)
    count_title = models.CharField('Count Title', max_length=50)
    price_title = models.CharField('Price Title', max_length=50)
    del_btn = models.CharField('Delete Button', max_length=40)
    btn_name1 = models.CharField('Button Name 1', max_length=40)
    btn_name2 = models.CharField('Button Name 2', max_length=40)

class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=False, null=True, blank=True)

class CartItem(models.Model):

    product = models.ForeignKey(ShopContent, on_delete=models.CASCADE, related_name='items')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitems')
    count1 = models.PositiveIntegerField('Count', blank=True)

class ProductReview(models.Model):

    user_review = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    user_product = models.ForeignKey(ShopContent, on_delete=models.CASCADE, related_name='reviews')
    user_text = models.TextField('User Text')
    review_date = models.DateField('Review Date', auto_now=True)
    to_check = models.BooleanField('Accept / Reject')

    class Meta:
        ordering = ['-review_date']

class UserOrder(models.Model):

    name = models.CharField('Ordered Username', max_length=50)
    game = models.CharField('Ordered Game', max_length=50)
    count = models.PositiveIntegerField('Ordered Game Count')
    date = models.DateTimeField('Ordered Game Date', auto_now=True)

class ForGuestUser(models.Model):

    text = models.CharField('Text', max_length=100)
    btn_name1 = models.CharField('Button Name 1', max_length=40)
    btn_name2 = models.CharField('Button Name 2', max_length=40)