from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegisterForm, LoginForm
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.views import View
from donation.models import Donation, Institution, Category
from django.contrib.auth.views import LoginView, LogoutView


class LandingPage(View):
    def get(self, request):
        all_donations = Donation.objects.all()
        bags_count = 0
        institution_list = []
        for donation in all_donations:
            bags_count += donation.quantity
            if donation.institution not in institution_list:
                institution_list.append(donation.institution)
        institution_count = len(institution_list)
        foundations = Institution.objects.filter(type=1)
        non_gov_orgs = Institution.objects.filter(type=2)
        local_fundraisers = Institution.objects.filter(type=3)

        ctx = {
            'bags_count': bags_count,
            'institution_count': institution_count,
            'foundations': foundations,
            'non_gov_orgs': non_gov_orgs,
            'local_fundraisers': local_fundraisers
        }
        return render(request, 'index.html', ctx)


class AddDonation(LoginRequiredMixin, View):
    login_url = '/login'
    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        ctx = {
            'categories': categories,
            'institutions': institutions
        }
        return render(request, 'form.html', ctx)


class Login(LoginView):
    template_name = 'login.html'
    next_page = '/'
    authentication_form = LoginForm


class Register(SuccessMessageMixin, CreateView):
    template_name = 'register.html'
    success_url = '/login'
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"


class Logout(LogoutView):
    next_page = '/'

