from .models import Setting


def get_setting():
    """
    Lessons:
        1. Use ORDER BY to return rows in a preferred order, eliminating unnecessary queries
    """
    return Setting.objects.order_by("-is_default").first()
