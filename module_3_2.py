# Задача "Рассылка писем"

def test_domain(addr, domain):
    return str(addr).find(domain) == len(addr) - len(domain)

def test_addr(addr):
    all_right = True
    all_right &= str(addr).find('@') > -1
    all_right &= test_domain(addr, '.ru') or test_domain(addr, '.com') or test_domain(addr, '.net')
    return all_right

def send_email(message, recipient,*, sender = 'university.help@gmail.com'):
    if not test_addr(recipient):
        print(f'Невозможно отправить письмо на адрес {recipient}!')
    elif not test_addr(sender):
        print(f'Невозможно отправить письмо c адреса {sender}!')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
