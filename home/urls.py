"""wedding_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("venue/", views.venue, name="venue"),
    path("rsvp_start/", views.rsvp_start, name="rsvp_start"),
    path("rsvp/<int:id>", views.rsvp, name="rsvp"),
    path("log_rsvp/", views.log_rsvp, name="log_rsvp"),
    path("rsvp_success/", views.rsvp_success, name="rsvp_success"),
    path("accommodation/", views.accommodation, name="accommodation"),
    path("ceremony/", views.ceremony, name="ceremony"),
    path("day_2/", views.day_2, name="day_2"),
    path("faq/", views.faq, name="faq"),
    path("gifts/", views.gifts, name="gifts"),
    path("contact/", views.contact, name="contact"),
    path("send_contact/", views.send_contact, name="send_contact"),
    path("contact_success/", views.contact_success, name="contact_success"),
]