import pytest

from .models import Setting
from .services import get_setting

pytestmark = pytest.mark.django_db


def test_get_setting__no_default():
    Setting.objects.create(name="Foo", value="Bar")
    Setting.objects.create(name="Other setting", value="Other Value")

    value = get_setting("Foo")

    assert value == "Bar"


def test_get_setting__with_default():
    Setting.objects.create(name="Foo", value="Bar")
    Setting.objects.create(name="Other setting", value="Other Value")
    Setting.objects.create(name="Foo", value="Baz", is_default=False)

    value = get_setting("Foo")

    assert value == "Baz"
