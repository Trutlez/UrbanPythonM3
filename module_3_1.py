# Задача "Счётчик вызовов"

calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(s):
    count_calls()
    result = (len(s), s.upper(), s.lower())
    return result

def is_contains(s, lst):
    count_calls()
    match = False
    for x in lst:
        if x.lower == s.lower:
            match = True
    return match

print(string_info('Urban'))
print(string_info('КулеБяка'))
print(is_contains('Ich', ['Dich', 'ich', 'Urban']))
print(is_contains('Я', ['Я', 'ты', 'Она']))

if calls == 0:
    print('Не было вызов функций.')
if calls == 1:
    print('Был', calls, 'вызов функции.')
elif calls < 5:
    print('Было', calls, 'вызова функций.')
else:
    print('Было', calls, 'вызовов функций.')