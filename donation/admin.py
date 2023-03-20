from django.contrib import admin

from donation.models import Institution, Donation, Category

# Register your models here.

admin.site.register(Institution)
admin.site.register(Donation)
admin.site.register(Category)