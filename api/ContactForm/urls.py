from django.urls import path

from .views import submit_contact_form

urlpatterns = [
    path(r'', submit_contact_form),
]