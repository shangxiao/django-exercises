from .models import Setting


def get_setting():
    setting = Setting.objects.filter(is_default=True).first()

    if not setting:
        setting = Setting.objects.first()

    return setting
