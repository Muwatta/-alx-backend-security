from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden
from .models import RequestLog, BlockedIP
from django.utils import timezone


class IPTrackingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get("REMOTE_ADDR")

        # Block if IP is blacklisted
        if BlockedIP.objects.filter(ip_address=ip).exists():
            return HttpResponseForbidden("Forbidden: Your IP has been blocked.")

        # Log request
        RequestLog.objects.create(
            ip_address=ip,
            timestamp=timezone.now(),
            path=request.path,
        )
