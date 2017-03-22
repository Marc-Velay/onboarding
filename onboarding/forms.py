from django import forms

class ImageUploadForm(forms.Form):
    """Image upload form."""
    print("image upload form")
    image = forms.ImageField(label="Select")

