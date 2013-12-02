from django import forms

class PostForm(forms.Form):
	text = forms.CharField(max_length=200)
	image = forms.ImageField(required=False)
