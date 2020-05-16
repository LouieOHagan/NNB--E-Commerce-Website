from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order

        fields = (
              'full_name',
              'email_address',
              'street_address1',
              'street_address2',
              'town_or_city',
              'county',
              'postcode',
              'country',
    )

    def __init__(self, *args, **kwargs):
        """ Used to customize form fields such as removing labels that are
        automatically created, adding placeholders and classes to inputs and
        also making it so that the first field is automatically selected when
        a page loads.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email_address': 'Email Address',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County',
            'postcode': 'Postal Code',
            'country': 'Country'
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-input'
            self.fields[field].label = False
