from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse

from .forms import UserRegisterForm, LoginForm, DonationForm
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, redirect
from django.views import View
from donation.models import Donation, Institution, Category
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.sites.shortcuts import get_current_site


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
        foundation_list = Institution.objects.filter(type=1)
        foundation_paginator = Paginator(foundation_list, 1)
        non_gov_org_list = Institution.objects.filter(type=2)
        non_gov_org_paginator = Paginator(non_gov_org_list, 1)
        local_fundraiser_list = Institution.objects.filter(type=3)
        local_fundraiser_paginator = Paginator(local_fundraiser_list, 1)
        page = request.GET.get('page')
        foundations = foundation_paginator.get_page(page)
        non_gov_orgs = non_gov_org_paginator.get_page(page)
        local_fundraisers = local_fundraiser_paginator.get_page(page)

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
        form = DonationForm()
        ctx = {
            'form': form
        }
        return render(request, 'form.html', ctx)

    def post(self, request):
        form = DonationForm(request.POST)
        if form.is_valid():
            new_donation = form.save(commit=False)
            new_donation.user = request.user
            new_donation.save()
            form.save_m2m()
            return render(request, 'form-confirmation.html')
        return render(request, 'form.html', {'form': form})


class Login(LoginView):
    template_name = 'login.html'
    next_page = '/'
    authentication_form = LoginForm

    def form_invalid(self, form):
        return redirect('register')

    # def form_valid(self, form):
    #     login(self.request, form.get_user())
    #     if not self.request.user.is_email_verified:
    #         logout(self.request)
    #         messages.error(self.request, 'Zweryfikuj email w celu zalogowania')
    #         return redirect('login')
    #
    #
    #     return HttpResponseRedirect(self.get_success_url())


# def send_confirm_email(user, request):
#     current_site = get_current_site(request)
#     email_subject = 'Activate your acount'
#     email_body =




class Register(CreateView):
    template_name = 'register.html'
    success_url = '/login'
    form_class = UserRegisterForm

    # def form_valid(self, form):
    #     send_confirm_email()
    #     self.object = form.save()
    #     return super().form_valid(form)


class Logout(LogoutView):
    next_page = '/'


class UserDetails(View):
    def get(self, request):
        user_donations = Donation.objects.filter(user=request.user).order_by('is_taken')
        ctx = {
            'user_donations': user_donations
        }
        return render(request, 'user_details.html', ctx)


class ArchiveDonation(View):
    def get(self, request, donation_id):
        try:
            donation = Donation.objects.get(id=donation_id)
        except ObjectDoesNotExist:
            return redirect('/')
        donation.is_taken = True
        donation.save()
        return redirect('user_details')


class FormConfirmation(View):
    def get(self, request):
        return render(request, 'form-confirmation.html')


class EditUser(UpdateView):
    model = User
    template_name = 'user_edit.html'
    success_url = 'user_details'
