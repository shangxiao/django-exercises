from .models import Setting


def get_setting(setting):
    settings = Setting.objects.filter(name=setting)

    if not (setting := settings.filter(is_default=False).first()):
        setting = settings.first()

    return setting.value
