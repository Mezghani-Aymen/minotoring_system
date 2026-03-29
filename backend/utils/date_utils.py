from datetime import datetime, timedelta

def now(format = "object"):
    currentDateTime= datetime.now()

    if format == "string":
        return currentDateTime.strftime("%Y-%m-%d %H:%M:%S")
    else:
        return currentDateTime


def current_date(format = "object"):
    currentDate = now("object").date()

    if format =="string":
        return currentDate.strftime("%Y-%m-%d")
    else:
        return currentDate



def get_previous_day(given_date=None):
    """
    Returns the previous calendar day from the given date.
    If no date is provided, uses today's date.
    """
    if given_date is None:
        given_date = current_date("object").today()
    elif not isinstance(given_date,  type(current_date())):
        raise TypeError("given_date must be a datetime.date object or None")

    return given_date - timedelta(days=1)