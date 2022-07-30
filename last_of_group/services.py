from zoneinfo import ZoneInfo

from django.db.models.expressions import RawSQL
from django.db.models.functions import Extract

from .models import Activity


def get_last_activity_per_person_per_day():
    """
    Lessons:
        - Use DISTINCT ON to keep the entire row that is first encountered, requires that ORDER BY be defined
          https://www.postgresql.org/docs/current/sql-select.html#SQL-DISTINCT
    """
    query = (
        Activity.objects.annotate(
            when_date=Extract("when", "day", tzinfo=ZoneInfo("Australia/Sydney"))
        )
        .order_by("who", "when_date", "-when")
        # ---> DISTINCT ON
        .distinct("who", "when_date")
        .annotate(
            when_str=RawSQL(
                "to_char(\"when\" at time zone 'Australia/Sydney', 'YYYY-MM-DD HH24:MI:SS')",
                params=[],
            )
        )
    )

    # Can't use values_list("who", "when_str", "what") here as it will erase when_date
    return [(activity.who, activity.when_str, activity.what) for activity in query]
