from django import forms
from .models import ProductReview


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview

        fields = (
            'display_name',
            'rating',
            'title',
            'product_review',
        )

    def __init__(self, *args, **kwargs):
        """ Add form input classes and set autofocus on first field """
        super().__init__(*args, **kwargs)

        self.fields['display_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control review-form-item'
