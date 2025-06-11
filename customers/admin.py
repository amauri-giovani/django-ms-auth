from django.contrib.admin import AdminSite
from django_otp.decorators import otp_required


class OTPAdminSite(AdminSite):
    @otp_required
    def has_permission(self, request):
        return super().has_permission(request)
