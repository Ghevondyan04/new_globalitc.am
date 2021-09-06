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
                'class': 'inputtext _58mg p-cl',
                'placeholder': 'Անուն Ազգանուն'
            }),
            "email": TextInput(attrs={
                'name': 'email',
                'type': 'email',
                'class': 'inputtext _58mg p-cl',
                'placeholder': 'Էլ-փոստ'
            }),
            "message": Textarea(attrs={
                'name': 'message',
                'type': 'email',
                'class': 'inputtext _mg58 p-cl',
                'placeholder': 'Հաղորդագրություն',
                'cols': 100,
                'rows': 10
            })
        }


class CallOrderForm(ModelForm):
    class Meta:
        model = CallOrder
        fields = ['customer_name', 'call_date', 'customer_number']

        widgets = {
            'customer_name': TextInput(attrs={
                # 'class' : 'ira_classi_anuny',
                'placeholder': 'Անուն Ազգանուն'
            }),
            'call_date': TextInput(attrs={
                # 'class' : 'ira_classi_anuny',
                'placeholder': 'Օր/Ժամ'
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
                'class': 'inputtext _58mg p-cl',
                'placeholder': 'Էլ․ փոստ'
            }),
        }
