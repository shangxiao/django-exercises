from .models import Setting


def get_setting(setting):
    """
    Lessons:
        1. Use ORDER BY to return rows in a preferred order, eliminating unnecessary queries
    """
    return Setting.objects.filter(name=setting).order_by("is_default").first().value
