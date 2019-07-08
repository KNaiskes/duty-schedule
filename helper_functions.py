# Basic encryption method of admin's password
# It is not super secure but it is good enough for our case
def encrypt_password(encrypt):
    import hashlib
    password = hashlib.sha256()
    password = hashlib.sha256(encrypt.encode("utf8")).hexdigest()
    return password

def current_month_days():
    import calendar
    from datetime import date

    today = date.today()
    current_month = today.month
    current_year = today.year
    month_days = calendar.monthrange(current_year, current_month)[1]
    return month_days

def calculateDateQuery(option):
    from datetime import timedelta
    from  datetime import date

    available_options = {
            "today": date.today(),
            "tomorrow": date.today() + timedelta(days=1),
            "week": date.today() + timedelta(days=7),
            "month": date.today() + timedelta(days=current_month_days()),
    }
    return available_options[option]

def generateDuties(users_list, option):
    from itertools import cycle
    from datetime import datetime
    from datetime import timedelta

    days_list = []
    start = calculateDateQuery("today")
    end = calculateDateQuery("week")
    step = timedelta(days=1)

    if option == "month":
        end = calculateDateQuery("month")

    while start <= end:
        days_list.append(start)
        start += step

    duties_list = list(zip(users_list, cycle(days_list)) if len(users_list) > len(days_list) else zip(cycle(users_list), days_list))

    return duties_list
