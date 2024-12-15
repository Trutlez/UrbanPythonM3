# Задача "Распаковка"

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# Функция с параметрами по умолчанию
print_params()
print_params('one')
print_params('один', 'два')
print_params(1, 2, 3)

print_params(b = 25)
print_params(c = [1,2,3])

# Распаковка параметров
values_list = [True, 'это правда', 1]
values_dict  = {'a': 3, 'b':False, 'c':'Ok'}

print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры
values_list_2 = [17, 'Ответ на вопрос']
print_params(*values_list_2, 42)


# и еще чего-нибудь
def append_to_list(item, list_my=None): # по сути list_my является обязательным параметром и непонятно зачем передавать ему значение по умолчанию None
    if list_my is None:
        list_my = []
    list_my.append(item)
    print(list_my)

list_new = []
append_to_list(1, list_new)
append_to_list(2, list_new)
append_to_list(3, list_new)

# а здесь бессмысленно передавать не переменную
append_to_list(7, [])
append_to_list(6, [])
append_to_list(5, [])
