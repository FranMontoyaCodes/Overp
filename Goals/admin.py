from django.contrib import admin
from Goals.models import Goals
from personal.models import Users
from account.models import Account
# Register your models here.
admin.site.register(Goals)
admin.site.register(Users)
admin.site.register(Account)		