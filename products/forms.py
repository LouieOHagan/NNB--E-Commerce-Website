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
