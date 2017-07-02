from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^invoices/(\d+)/$', views.line_items, name='line_items'),
    url(r'^invoices/', views.invoices, name='invoices'),
    url(r'^seed_invoice_model/', views.seed_invoice_model, name='seed_invoice_model'),
    url(r'^seed_lineitem_model/', views.seed_lineitem_model, name='seed_lineitem_model')
]
