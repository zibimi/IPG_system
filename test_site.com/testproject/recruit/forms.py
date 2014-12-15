from django import forms
from django.contrib.auth.models import User
import re
from django.core.exceptions import ObjectDoesNotExist
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput  


class RegistrationForm(forms.Form):
	username = forms.CharField(
		required = True,
		label = u'Username',
		error_messages = {'required' : u'Please input your username'},
		max_length = 30,
		widget = forms.TextInput(
			attrs = {
				'placeholder' : u'username',
			}
		),
	)

	email = forms.EmailField(
		required = True,
		label = u'Email',
		error_messages = {'required' : u'Please input your email'},
		max_length = 100,
		widget = forms.EmailInput(
			attrs = {
				'placeholder' : u'email',
			}
		),
	)

	password1 = forms.CharField(
		required = True,
		label = u'Password',
		error_messages = {'required' : u'Please input your password'},
		max_length = 30,
		widget = forms.PasswordInput(
			attrs = {
				'placeholder' : u'password',
			}
		),
	)

	password2 = forms.CharField(
		required = True,
		label = u'Password',
		error_messages = {'required' : u'Please input your password'},
		max_length = 30,
		widget = forms.PasswordInput(
			attrs = {
				'placeholder' : u'password',
			}
		),
	)
#BUG
	def clean_username(self):
		username = self.cleaned_data['username']
		if not re.search(r'\w+$', username):
			raise forms.ValidationError('Username can only contain letter, number and underline')
		try:
			User.objects.get(username=username)
		except ObjectDoesNotExist:
			return username
		raise forms.ValidationError('Username have been existed')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			User.objects.get(email=email)
		except ObjectDoesNotExist:
			return email
		raise forms.ValidationError('Email have been used')

	def clean_password2(self):
		if 'password1' in self.cleaned_data:
			password1 = self.cleaned_data['password1']
			password2 = self.cleaned_data['password2']
			if password1 == password2:
				return password2
		raise forms.ValidationError('Password does not match')


class LoginForm(forms.Form):
	username = forms.CharField(
		required = True,
		label = u'Username',
		error_messages = {'required' : u'Please input your username'},
		widget = forms.TextInput(
			attrs = {
				'placeholder' : u'username',
			}
		),
	)

	password = forms.CharField(
		required = True,
		label = u'Password',
		error_messages = {'required' : u'Please input your password'},
		widget = forms.PasswordInput(
			attrs = {
				'placeholder' : u'password',
			}
		),
	)

	def clean(self):
		if not self.is_valid():
			raise forms.ValidationError('Required username & password')
		else :
			cleaned_data = super(LoginForm, self).clean()


class ProfileForm(forms.Form):
	first_name = forms.CharField(
		required = True,
		label = u'First Name',
		error_messages = {'required' : u'Please input your first name'},
		widget = forms.TextInput(
			attrs = {
				'placeholder' : u'first name',
			}
		),
	)
	last_name = forms.CharField(
		required = True,
		label = u'Last Name',
		error_messages = {'required' : u'Please input your last name'},
		widget = forms.TextInput(
			attrs = {
				'placeholder' : u'last name',
			}
		),
	)
	email = forms.EmailField(
		required = True,
		label = u'Email',
		error_messages = {'required' : u'Please input your email'},
		max_length = 100,
		widget = forms.EmailInput(
			attrs = {
				'placeholder' : u'email',
			}
		),
	)
	phone = forms.CharField(
		required = True,
		label = u'Phone',
		error_messages = {'required' : u'Please input your username'},
		widget = forms.TextInput(
			attrs = {
				'placeholder' : u'username',
			}
		),
	)
	address = forms.CharField(
		required = True,
		label = u'Address',
		error_messages = {'required' : u'Please input your username'},
		widget = forms.TextInput(
			attrs = {
				'placeholder' : u'username',
			}
		),
	)
	city = forms.CharField(
		required = True,
		label = u'City',
		error_messages = {'required' : u'Please input your username'},
		widget = forms.TextInput(
			attrs = {
				'placeholder' : u'username',
			}
		),
	)
	state = forms.CharField(
		required = True,
		label = u'State',
		error_messages = {'required' : u'Please input your username'},
		widget = forms.TextInput(
			attrs = {
				'placeholder' : u'username',
			}
		),
	)
	zip = forms.IntegerField(
		required = True,
		label = u'Zip',
		error_messages = {'required' : u'Please input your username'},
		widget = forms.NumberInput(
			attrs = {
				'placeholder' : u'username',
			}
		),
	)
	visa_status = forms.CharField(
		required = True,
		label = u'Visa Status',
		error_messages = {'required' : u'Please input your username'},
		widget = forms.TextInput(
			attrs = {
				'placeholder' : u'username',
			}
		),
	)
	portfolio_link = forms.URLField(
		required = True,
		label = u'Portfolio Link',
		error_messages = {'required' : u'Please input your username'},
		widget = forms.URLInput(
			attrs = {
				'placeholder' : u'username',
			}
		),
	)
	linkedin = forms.URLField(
		required = True,
		label = u'Linkedin',
		error_messages = {'required' : u'Please input your username'},
		widget = forms.URLInput(
			attrs = {
				'placeholder' : u'username',
			}
		),
	)
	source = forms.CharField(
		required = True,
		label = u'Source',
		error_messages = {'required' : u'Please input your username'},
		widget = forms.URLInput(
			attrs = {
				'placeholder' : u'username',
			}
		),
	)
	resume_link = forms.URLField(
		required = True,
		label = u'Resume Link',
		error_messages = {'required' : u'Please input your username'},
		widget = forms.URLInput(
			attrs = {
				'placeholder' : u'username',
			}
		),
	)

# class ChangepwForm(forms.Form):
# 	old_password = forms.CharField(
# 		required = True,
# 		label = u'Old Password',
# 		error_messages = {'required' : u'Please input your old password'},
# 		widget = forms.TextInput(
# 			attrs = {
# 				'placeholder' : u'old password',
# 			}
# 		),
# 	)

# 	new_password = forms.CharField(
# 		required = True,
# 		label = u'New Password',
# 		error_messages = {'required' : u'Please input your new password'},
# 		widget = forms.TextInput(
# 			attrs = {
# 				'placeholder' : u'new password',
# 			}
# 		),
# 	)

# 	confirm_password = forms.CharField(
# 		required = True,
# 		label = u'Confirm Password',
# 		error_messages = {'required' : u'Please input your new password again'},
# 		widget = forms.TextInput(
# 			attrs = {
# 				'placeholder' : u'confirm password',
# 			}
# 		),
# 	)

# 	def clean(self):
# 		if not self.is_valid():
# 			raise forms.ValidationError('All field is required!')
# 		elif self.cleaned_data['new_password'] <> slef.cleaned_data['confirm_password']:
# 			raise forms.ValidationError('Your password is inconformity')
# 		else :
# 			cleaned_data = super(ChangepwForm, self).clean()
# 		return cleaned_data



