from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from authapp.models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs): # определяет класс в создаваемых полях
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = "userform-formblock-field"
            field.widget.attrs['placeholder'] = field_name
            field.help_text = '' # вспомогательный текст

class ShopUserRegisterForm(UserCreationForm):

    class Meta:
        model = ShopUser
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'avatar':
                field.widget.attrs['class'] = "file"
            else:
                field.widget.attrs['class'] = "userform-formblock-field"
                field.widget.attrs['placeholder'] = field_name

            field.help_text = ''

class ShopUserEditForm(UserChangeForm):

    class Meta:
        model = ShopUser
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar')

    def __init__(self, *args, **kwargs):
        super(ShopUserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'avatar':
                field.widget.attrs['class'] = "file"
            else:
                field.widget.attrs['class'] = "userform-formblock-field"
                field.widget.attrs['placeholder'] = field_name

            field.help_text = ''

            if field_name == 'password':
                field.widget = forms.HiddenInput()
