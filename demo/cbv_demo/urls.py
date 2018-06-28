from django.urls import path
from .views import ContactData

urlpatterns = [
    path('contact', ContactData.as_view(), name='contact'),
]
