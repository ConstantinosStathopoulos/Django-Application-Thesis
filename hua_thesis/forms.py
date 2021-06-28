from django import forms
from captcha.fields import CaptchaField

#contact form
class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Όνομα'}),label='Εισάγετε όνομα')
	last_name = forms.CharField(max_length = 50, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Επίθετο'}),label='Εισάγετε επίθετο')
	email_address = forms.EmailField(max_length = 50, widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@domain.com'}),label='Εισάγετε email')
	message = forms.CharField(max_length = 2000, widget = forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Κείμενο μηνύματος'}),label='Εισάγετε κείμενο μηνύματος')
	captcha = CaptchaField(label='Εισάγετε το κέιμενο της εικόνας')

	class Μeta:

		labels = {
        "first_name": "Όνομα",
        "last_name": "Επίθετο",
        "email_address": "Διεύθυνση Email",
		"message": "Μήνυμα"
        }
        
		