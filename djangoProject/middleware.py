import re
from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin

class CustomXFrameOptionsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Регулярное выражение для разрешенных доменов
        allowed_domains = re.compile(r'^https?:\/\/([^\/]+\.)?(djangoproject-gvn3.onrender\.com|webvisor\.com|metri[ck]a\.yandex\.(com|ru|by|com\.tr)|socpublic\.com)\/')

        # Получаем домен из заголовка Referer
        referer = request.META.get('HTTP_REFERER', '')

        # Если реферер не пустой и соответствует регулярному выражению, разрешаем встраивание
        if referer and allowed_domains.match(referer):
            response['X-Frame-Options'] = 'ALLOW-FROM ' + referer
        else:
            # Иначе ограничиваем встраивание
            response['X-Frame-Options'] = 'DENY'

        return response
