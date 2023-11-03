from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    now = datetime.today().date()
    current_week_day = now.weekday()
    if current_week_day >= 5:
        start_date = now - timedelta(days=(7 - current_week_day))
    elif current_week_day == 0:
        start_date = now - timedelta(days=2)
    else:
        start_date = now
    days_ahead = 4 - current_week_day
    if days_ahead < 0:
        days_ahead += 7
    end_date = now + timedelta(days=days_ahead)

    result = []
    for user in users:
        birthday = user.get('birthday').replace(year=now.year)
        if start_date <= birthday <= end_date:
            result.append(user)

    weekday = None
    for user in sorted(result, key=lambda x: x['birthday'].replace(year=now.year)):
        user_birthday = user.get('birthday').replace(year=now.year).weekday()

        # try:
        #
        # except IndexError:
        if weekday != user_birthday:
            weekday = user_birthday
            print(weekday)
        print(user.get('name'))
    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
