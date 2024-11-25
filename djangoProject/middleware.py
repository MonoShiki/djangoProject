from django.utils.deprecation import MiddlewareMixin

class CustomXFrameOptionsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        allowed_domains = ['example.com', 'another-example.com']
        referer = request.META.get('HTTP_REFERER', '')

        # Проверяем, если реферер соответствует одному из разрешенных доменов
        if any(domain in referer for domain in allowed_domains):
            response['X-Frame-Options'] = 'ALLOW-FROM {}'.format(referer)
        else:
            response['X-Frame-Options'] = 'DENY'

        return response
