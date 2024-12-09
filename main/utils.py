import re
from datetime import datetime
from urllib.parse import unquote, quote

def define_field_type(value):
  
    print(value)
    decoded_value = unquote(value)

    # Проверка на дату
    try:
    # Проверяем дату в формате YYYY-MM-DD
        datetime.strptime(decoded_value, '%Y-%m-%d')
        return 'date'
    except ValueError:
        try:
    # Проверяем дату в формате DD.MM.YYYY
            datetime.strptime(decoded_value, '%d.%m.%Y')
            return 'date'
        except ValueError:
            pass

    # Проверяем телефон 
    if re.match(r'^(?:\+7|7) \d{3} \d{3} \d{2} \d{2}$', decoded_value) : 
        return 'phone'

    # Проверяем email
    if re.match(r'[^@]+@[^@]+\.[^@]+', decoded_value):
        return 'email'

    return 'text'
