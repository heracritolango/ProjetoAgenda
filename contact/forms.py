from django.core.exceptions import ValidationError
from django import forms
from contact import models

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs= {
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',    
            }
        ),
        label='Primeiro nome',
        help_text='Texto de ajuda para seu usuário',
    ) 

    def __init__(self, *args, **kwaargs): # atualiza widgets
        super().__init__(*args, **kwaargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Aqui veio do init',
        # })

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )

        # widgets = {                                 # cria widgets
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui',
        #         }
        #     )
        # }

    def clean(self):
        # cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Veio do add_error',
                    code='invalid'
                )
            )

        return first_name