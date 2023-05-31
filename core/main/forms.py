from django import forms
from .models import HomePageLastPost
from .models import ContactPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class SubscribeModelForm(forms.ModelForm):

    class Meta:

        model = HomePageLastPost
        fields = ['user_email']

class ContactModelForm(forms.ModelForm):

    class Meta:

        model = ContactPost
        fields = ['user_name', 'user_surname', 'user_email', 'subject', 'message']






class NewUserForm(UserCreationForm):
	email = forms.EmailField(max_length=200, help_text='Required')
	captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user