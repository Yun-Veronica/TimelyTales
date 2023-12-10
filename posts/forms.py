from django.contrib.auth.models import User
from django import forms
from django import forms
from .models import PostModel


class PostCreationForm(forms.ModelForm):
    # user = forms.CharField(widget=forms.HiddenInput())
    # timestamp = forms.TimeField(widget=forms.HiddenInput())

    class Meta:
        model = PostModel
        fields = ["title","picture","text"]


        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  # Customizing the text field as a textarea
        }
        # You don't need to define a widget for 'picture' if it's just a standard image upload
        # The default widget for ImageField will be used automatically
        # widgets = {
        #     'picture': forms.ImageField(),
        # }
    # def __init__(self, *args, **kwargs):
    #     super(PostCreationForm, self).__init__(*args, **kwargs)
    #     self.fields['picture'].required = False

