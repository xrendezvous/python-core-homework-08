from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    now = datetime.today().date()
    end_of_week = now + timedelta(days=(4 - now.weekday() + 7) % 7)
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    result = {day: [] for day in weekdays}

    for user in users:
        user_birthday = user.get('birthday').replace(year=now.year).date()
        if now <= user_birthday <= end_of_week:
            day_name = weekdays[user_birthday.weekday()]
            user_name = user.get('name').split()[0]
            result[day_name].append(user_name)
        elif user_birthday.year > now.year and user_birthday <= end_of_week:
            day_name = weekdays[user_birthday.weekday()]
            user_name = user.get('name').split()[0]
            result[day_name].append(user_name)

    return result


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
