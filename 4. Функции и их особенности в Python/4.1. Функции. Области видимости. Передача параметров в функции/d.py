import calendar

rus_calendar = [
    'Январь',
    'Февраль',
    'Март',
    'Апрель',
    'Май',
    'Июнь',
    'Июль',
    'Август',
    'Сентябрь',
    'Октябрь',
    'Ноябрь',
    'Декабрь'
]


def month(month_number: int, month_name: str) -> str:
    if month_name.lower() == 'ru':
        return rus_calendar[month_number - 1]

    return calendar.month_name[month_number]
