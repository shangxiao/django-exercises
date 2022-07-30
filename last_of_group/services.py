from zoneinfo import ZoneInfo

from django.db.models.aggregates import Max
from django.db.models.expressions import RawSQL
from django.db.models.functions import Extract

from .models import Activity


def get_last_activity_per_person_per_day():
    last_activities = []

    for activity in (
        Activity.objects.annotate(
            when_date=Extract("when", "day", tzinfo=ZoneInfo("Australia/Sydney"))
        )
        .values("who", "when_date")
        .order_by("who", "when_date")
        .annotate(max_when=Max("when"))
    ):
        last_activity = (
            Activity.objects.filter(who=activity["who"], when=activity["max_when"])
            .annotate(
                when_str=RawSQL(
                    "to_char(\"when\" at time zone 'Australia/Sydney', 'YYYY-MM-DD HH24:MI:SS')",
                    params=[],
                )
            )
            .values_list("who", "when_str", "what")[0]
        )
        last_activities.append(last_activity)

    return last_activities
