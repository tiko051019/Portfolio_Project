from django.forms import ModelForm
from .models import *

class ContactMessageForm(ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'