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
        # values() + annotate() with aggregation creates a GROUP BY
        .values("when_date", "who")
        .annotate(max_when=Max("when"))
        .order_by("when_date", "who")
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
