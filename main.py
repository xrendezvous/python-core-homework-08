from datetime import date, timedelta
import calendar

def get_birthdays_per_week(users):
    today = date.today()
    current_year = today.year

    birthdays_per_week = {}
    for user in users:
        birthday = user["birthday"]
        birthday_year = birthday.year

        if birthday_year < current_year:
            if birthday.month <= today.month and birthday.day <= today.day:
                continue
            else:
                next_birthday = birthday.replace(year=current_year)
        else:
            next_birthday = birthday.replace(year=current_year)

        days_to_birthday = (next_birthday - today).days

        if days_to_birthday < 0:
            continue

        next_birthday_weekday = (today + timedelta(days_to_birthday)).weekday()
        weekday_name = calendar.day_name[next_birthday_weekday]

        if weekday_name not in birthdays_per_week:
            birthdays_per_week[weekday_name] = []

        birthdays_per_week[weekday_name].append(user["name"])

    return birthdays_per_week


if __name__ == "__main__":
    users = [
        {"name": "Masha", "birthday": date(2023, 11, 9)},
        {"name": "Olya", "birthday": date(2023, 11, 3)},
        {"name": "Kolya", "birthday": date(2023, 11, 4)},
        {"name": "Sophia", "birthday": date(2023, 11, 5)},
        {"name": "Solomia", "birthday": date(2023, 11, 6)},
        {"name": "Sasha", "birthday": date(2023, 11, 7)},
        {"name": "Pasha", "birthday": date(2023, 11, 8)},
        {"name": "Oksana", "birthday": date(2023, 11, 10)}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
