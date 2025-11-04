from .models import RequestLog
from django.utils.timezone import now
from django.utils.deprecation import MiddlewareMixin

class IPLoggingMiddleware(MiddlewareMixin):
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')

    def process_request(self, request):
        ip = self.get_client_ip(request)
        path = request.path

        RequestLog.objects.create(
            ip_address=ip,
            path=path,
            timestamp=now()
        )
