from django import forms

from advanced_tactics.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['hair_color', 'birthdate', 'favorite_hobby', 'created'] # only show these fields
        # fields = '__all__' # default behavior
        # exclude = ['birthdate', 'favorite_hobby',] # don't show these fields