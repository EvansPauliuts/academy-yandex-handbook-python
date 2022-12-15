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


def month(month_number: int, month_name: str = 'ru') -> str:
    if month_name.lower() == 'en':
        return calendar.month_name[month_number]

    return rus_calendar[month_number - 1]
