from .models import ContactWithUs, CallOrder, Subscribe
from django.forms import ModelForm, TextInput, Textarea


class ContactWithUsForm(ModelForm):
    class Meta:
        model = ContactWithUs
        fields = ['full_name', 'email', 'message']

        widgets = {
            "full_name": TextInput(attrs={
                'name': 'flname',
                'type': 'text',
                'placeholder': 'Անուն Ազգանուն'
            }),
            "email": TextInput(attrs={
                'name': 'email',
                'type': 'email',
                'placeholder': 'Էլ-փոստ'
            }),
            "message": Textarea(attrs={
                'name': 'message',
                'type': 'email',
                'placeholder': 'Հաղորդագրություն',
            })
        }


class CallOrderForm(ModelForm):
    class Meta:
        model = CallOrder
        fields = ['customer_name', 'call_date', 'customer_number']

        widgets = {
            'customer_name': TextInput(attrs={
                'class': 'name-username',
                'placeholder': 'Անուն Ազգանուն',
                'type': 'text'
            }),
            'call_date': TextInput(attrs={
                'class': 'inp-2',
                'placeholder': '+374',
                'type': 'text'
            }),
            'customer_number': TextInput(attrs={
                # 'class' : 'ira_classi_anuny',
                'placeholder': 'Հեռախոսահամար'
            })
        }


class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = ['email', ]

        widgets = {
            'email': TextInput(attrs={
                'type': 'text',
                'placeholder': 'Էլ․ փոստ"'
            }),
        }
