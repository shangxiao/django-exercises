from datetime import datetime

import pytest

from .models import Activity
from .services import get_last_activity_per_person_per_day

pytestmark = pytest.mark.django_db


def test_get_last_activity_of_the_day():
    activities = [
        ("Bob", "2022-01-01 09:00:00+1100", "Comes to work"),
        ("Bob", "2022-01-01 12:00:00+1100", "Eats lunch"),
        ("Bob", "2022-01-01 17:00:00+1100", "Goes home"),
        ("Alice", "2022-01-01 09:30:00+1100", "Comes to work"),
        ("Alice", "2022-01-01 13:00:00+1100", "Eats lunch"),
        ("Alice", "2022-01-01 17:30:00+1100", "Goes home"),
    ]
    Activity.objects.bulk_create(
        Activity(
            who=who,
            when=datetime.strptime(when, "%Y-%m-%d %H:%M:%S%z"),
            what=what,
        )
        for (who, when, what) in activities
    )

    results = get_last_activity_per_person_per_day()

    assert results == [
        ("Alice", "2022-01-01 17:30:00", "Goes home"),
        ("Bob", "2022-01-01 17:00:00", "Goes home"),
    ]
