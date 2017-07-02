from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^seed_invoice_model/', views.seed_invoice_model, name='seed_invoice_model'),
    url(r'^seed_lineitem_model/', views.seed_lineitem_model, name='seed_lineitem_model')
]
