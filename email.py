from datetime import date
from math import ceil
import pprint


# 1. Создайте словарь email, содержащий следующие поля:
# "subject" (тема письма), "from" (адрес отправителя), "to" (адрес получателя), "body" (текст письма).

email = {
    "subject": "Quarterly Report",
    "from": "Alice.Cooper@Company. ",
    "to": " bob_smith@Gmail.com ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice"
}
pprint.pprint(email)
print()

# 2. Добавьте дату отправки: создайте переменную send_date как текущую дату в формате YYYY-MM-DD и запишите её в email["date"].

send_date = str(date.today())
email["date"] = send_date

# 3. Нормализуйте e-mail адреса отправителя и получателя: приведите к нижнему регистру и уберите пробелы по краям.
# Запишите обратно в email["from"] и email["to"].

email["from"] = email["from"].lower().strip()
email["to"] = email["to"].lower().strip()

# 4. Извлеките логин и домен отправителя в две переменные login и domain.

login = email["from"].split('@')[0]
domain = email["from"].split('@')[1]
print(f'login отправителя - {login}\ndomain отправителя - {domain}')
print()

# 5. Создайте сокращённую версию текста: возьмите первые 10 символов email["body"] и добавьте многоточие "...".
# Сохраните в новый ключ словаря: email["short_body"].

email["short_body"] = email["body"][:10] +'...'

# 6. Списки доменов: создайте список личных доменов и список корпоративных доменов с учетом того что там должны быть только уникальные значение

private_domains = list({'gmail.com','list.ru', 'yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru','mail.ru','list.ru','bk.ru','inbox.ru'})
corporate_domains = list({'company.ru', 'corporation.com', 'university.edu', 'organization.org', 'company.ru', 'business.net'})

# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений:
# ни один домен не должен входить в оба списка одновременно.

private_domains, corporate_domains = set(private_domains), set(corporate_domains)
intersection_domains = private_domains.intersection(corporate_domains)
if intersection_domains:
    print("в списке личных и корпоративных доменов есть пересечения:", list(intersection_domains))
else:
    print("пересечений в списке личных и корпоративных доменов нет")
print()

# 8. Проверьте «корпоративность» отправителя: создайте булеву переменную is_corporate,
# равную результату проверки вхождения домена отправителя в список корпоративных доменов.

is_corporate = domain in corporate_domains
print(f'is_corporate - {is_corporate}')

# 9. Соберите «чистый» текст сообщения без табов и переводов строк: замените "\t" и "\n" на пробел.
# Сохраните в email["clean_body"].

email["clean_body"] = email["body"].replace('\t', '').replace('\n', '')

# 10. Сформируйте текст отправленного письма многострочной f-строкой и сохраните в email["sent_text"]:
# Кому: {получатель}, от {отправитель} Тема: {тема письма}, дата {дата} {чистый текст сообщения}

multi_text = f'''Кому: {email["from"]}
от {email["to"]}
Тема: {email["subject"]}
дата {email["date"]}
{email["clean_body"]}'''
email["sent_text"] = multi_text

# 11. Рассчитайте количество страниц печати для email["sent_text"], если на 1 страницу помещается 500 символов.
# Сохраните результат в переменную pages. Значение должно быть округленно в большую сторону.

pages = ceil(len(email["sent_text"])/ 500)
print(f'pages - {pages}')

# 12. Проверьте пустоту темы и тела письма: создайте переменные is_subject_empty,
# is_body_empty в котором будет хранится что тема письма содержит данные.

is_subject_empty = not email["subject"].strip()
is_body_empty = not email["body"].strip()
print(f'is_subject_empty - {is_subject_empty}\nis_body_empty - {is_body_empty}')
print()

# 13. Создайте «маску» e-mail отправителя: первые 2 символа логина + "***@" + домен.
# Запишите в email["masked_from"].

email["masked_from"] = login[:2] + '***@' + domain

# 14. Удалите из списка личных доменов значения "list.ru" и "bk.ru".
private_domains = list(private_domains)
private_domains.remove('list.ru')
private_domains.remove('bk.ru')

pprint.pprint(email)
