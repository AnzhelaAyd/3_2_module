
def send_email(messange, reciplient, sender='university.help@gmail.com'):
    if ('@' not in sender and '.com' not in sender and '.ru' not in sender and '.net' not in sender) and ('@' not in reciplient and '.com' not in reciplient and '.ru' not in reciplient and '.net' not in reciplient) :
        print( 'Не возможно отправить письмо с адреса ', {sender},' на адрес', {reciplient})
    elif sender == reciplient :
        print('Нельзя отправить письмо самому себе')
    elif sender == "university.help@gmail.com":
        print('Письмо успешно отправлено с адреса ',{sender}, 'на адрес', {reciplient})
    elif sender != "university.help@gmail.com":
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', {sender}, ' на адрес', {reciplient})


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
