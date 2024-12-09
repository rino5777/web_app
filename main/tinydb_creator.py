from faker import Faker
from tinydb import TinyDB
from .utils import define_field_type






# Создаем базу
db = TinyDB('forms_db.json')
templates_table = db.table('templates')

fake = Faker()

# Генерируем шаблоны формы
def generate_form_item():
    form = {"name": fake.word()}  # создается случайное имя формы 
    for _ in range(fake.random_int(min=2, max=6)):  # рандом от 2 до 6 полей
        field_name = fake.word()  
        field_type = fake.random_element(["email", "phone", "date", "text"])  # Типы полей
        form[field_name] = field_type
    return form

# Заполняем базу данных шаблонами
def create_db(count=10):
    existing_data = templates_table.all()
    if not existing_data: 
        for _ in range(count):
            form_item = generate_form_item()
            templates_table.insert(form_item)
        print(f"{count} коллич. шаблонов форм ")
    else:
        print("уже заполнено.")

create_db()

# функция ищет шаблон формы в базе данных, который совпадает с переданными полями.
def find_matching_template(form_data):

    # получаем все шаблоны из базы данных
    templates = templates_table.all()

    for template in templates:
        template_name = template.get('name') #"имя шаблона 
        # получаем поля и их типы (исключая имя шаблона)
        template_fields = {key: val for key, val in template.items() if key != 'name'}

        # проверяем, что все поля шаблона присутствуют в запросе и имеют нужный тип
        match = True
        for k, value in template_fields.items():
            if k not in form_data:
                match = False
                break

            # определяем тип поля в данных формы
            field_value = form_data[k]
            determined_type = define_field_type(field_value)
            
            # проверяем, что типы совпадают
            if determined_type != value:
                match = False
                break
        
        # если все поля совпали, то возвращаем имя шаблона
        if match:
            return template_name
    
    # если подходящий шаблон не найден
    return None