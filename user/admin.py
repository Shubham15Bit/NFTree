from django.contrib import admin

from .models import Account, Organization, UserEmail, KYC

admin.site.register(Account)
admin.site.register(UserEmail)
admin.site.register(Organization)
# admin.site.register(Approver)
# admin.site.register(Issuer)
admin.site.register(KYC)
