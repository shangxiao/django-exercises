import pytest

from .models import Setting
from .services import get_setting

pytestmark = pytest.mark.django_db


def test_get_setting__no_default():
    Setting.objects.create(name="Not a default")
    Setting.objects.create(name="Other setting")

    result = get_setting()

    assert result.name == "Not a default"


def test_get_setting__with_default():
    Setting.objects.create(name="Not a default")
    Setting.objects.create(name="A default", is_default=True)
    Setting.objects.create(name="Other setting")

    result = get_setting()

    assert result.name == "A default"
