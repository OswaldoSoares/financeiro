from datetime import datetime
from dateutil.relativedelta import relativedelta


def start_end_dates(month_year):
    """
        Returns the first and last day of the month from a month and year
        string.
    Args:
        month_year: String composed of month and year in mm/yyyy format.

    Returns:
        datetime first_day and datetime last_day

    """
    month, year = detach_month_year(month_year)
    first_day = datetime.strptime(f"1-{month}-{year}", "%d-%m-%Y")
    last_day = first_day + relativedelta(months=+1, days=-1)
    return first_day, last_day
