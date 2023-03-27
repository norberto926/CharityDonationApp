"""Portfolio_lab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from donation.views import LandingPage, Register, AddDonation, Login, Logout, UserDetails, ArchiveDonation, \
    FormConfirmation, EditUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', Logout.as_view()),
    path('', LandingPage.as_view(), name='landing_page'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('add_donation', AddDonation.as_view(), name='add_donation'),
    path('user_details', UserDetails.as_view(), name='user_details'),
    path('archive_donation/<int:donation_id>', ArchiveDonation.as_view(), name='archive_donation'),
    path('form_confirmation', FormConfirmation.as_view(), name="form_confirmation"),
]
