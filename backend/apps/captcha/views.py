from django.conf import settings
from django.http import HttpResponseNotAllowed
from django.http.response import JsonResponse
from django.middleware.csrf import get_token
from django.views.generic import View
from django.views.generic.base import ContextMixin

from .captcha import Captcha

from apps.core import cache  # noqa: isort:skip

captcha_cached_time = settings.CAPTCHA_CACHED_TIME or (30 * 60)


class CaptchaAPIView(ContextMixin, View):
    http_method_names = ("get", )

    def get(self, request, *args, **kwargs):
        captcha = Captcha()
        text, captcha_img_path, result_status, message = (
            captcha.generate_captcha()
        )
        cache.set(key=text.lower(), value=text, timeout=captcha_cached_time)
        return JsonResponse(
            {
                "captchaImgPath": captcha_img_path,
                "message": message,
                "resultStatus": result_status,
                "CSRFToken": get_token(request),
            }
        )

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse(
            {
                "captchaImgPath": None,
                "message": "Not allowed",
                "resultStatus": 2,
                "CSRFToken": None,
            },
            status=HttpResponseNotAllowed.status_code,
        )
