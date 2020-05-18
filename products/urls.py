from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_products, name='display_products'),
    path('<int:product_id>/', views.indiv_products, name='indiv_products'),
    path('add_review/<int:product_id>/', views.add_review, name='add_review'),
]