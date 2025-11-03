from django.http import HttpResponseForbidden
from .models import RequestLog, BlockedIP

class IPLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')

        # Check if blocked
        if BlockedIP.objects.filter(ip_address=ip).exists():
            return HttpResponseForbidden("Access Denied")

        # Log request
        RequestLog.objects.create(
            ip_address=ip,
            path=request.path,
        )

        return self.get_response(request)
