import os
from datetime import datetime

from celery import shared_task
from django.conf import settings

captcha_dir = getattr(settings, "CAPTCHA_DIR")


@shared_task
def remove_outdated_captcha_image():
    for this in captcha_dir.glob("*"):
        if this.is_file():
            created_time = os.path.getctime(this)  # 获取验证码图片创建的时间
            delta = datetime.now().timestamp() - created_time
            if delta >= 60:
                this.unlink()


@shared_task
def debug_periodic_task(args):
    print(args)
