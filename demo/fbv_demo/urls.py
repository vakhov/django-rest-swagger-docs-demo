from django.urls import path
from .views import save_medical, get_medical

urlpatterns = [
    path('save_medical', save_medical, name='save_contact'),
    path('get_medical', get_medical, name='get_contact'),
]
