from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tinydb_creator import find_matching_template
from .utils import define_field_type




# функия которая переводит словарь QueryDict в словарь со значениями key : value где value не список так как это в QueryDict
def clean_dict_data(data): return {key: val.strip() for key, val in data.items()}



class GetFormView(APIView):
    def post(self, request):
        form_data = request.data
        print("полученая дата:", form_data)

        # проверяем, являются ли значения списками
        if all(hasattr(value, '__iter__') for value in form_data.values()):
        # перводим в словарь если значения списки
            clean_data_dict = clean_dict_data(form_data)
            print("Обработанная дата:", clean_data_dict)
        else:
        # если значения не списки,  то используем их напрямую
            print("полученая дата без списка:", form_data)
            clean_data_dict = form_data

        # обработка данных
        matching_template = find_matching_template(clean_data_dict)
        if matching_template:
            return Response({"Имя": matching_template}, status=status.HTTP_200_OK)

        # Определяем типы полей, если шаблон не найден
        response_data = {
            field: define_field_type(value) for field, value in clean_data_dict.items()
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)
