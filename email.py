from datetime import date
import pprint


# 1. Создайте словарь email.

email = {
    "subject": "Quarterly Report",
    "from": "Alice.Cooper@Company. ",
    "to": " bob_smith@Gmail.com ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice"
}

# 2. Добавьте дату отправки(send_date как текущую дату в формате YYYY-MM-DD) и запишите её в email["date"].

send_date = str(date.today())
email["date"] = send_date

# 3. Нормализуйте e-mail адреса отправителя и получателя: приведите к нижнему регистру и уберите пробелы по краям.

email["from"] = email["from"].lower().strip()
email["to"] = email["to"].lower().strip()

# 4. Извлеките логин и домен отправителя в две переменные login и domain.

login = email["from"][:email["from"].find('@')]
domain = email["from"][email["from"].find('@')+1:]

# 5. Создайте сокращённую версию текста. Сохраните в новый ключ словаря: email["short_body"].

email["short_body"] = email["body"][:10] +'...'

# 6. Списки доменов: создайте список личных доменов

private_domains = list({'gmail.com','list.ru', 'yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru','mail.ru','list.ru','bk.ru','inbox.ru'})
corporate_domains = list({'company.ru', 'corporation.com', 'university.edu', 'organization.org', 'company.ru', 'business.net'})

# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений.

private_domains, corporate_domains = set(private_domains), set(corporate_domains)
private_domains.intersection(corporate_domains)

# 8. Проверьте «корпоративность» отправителя.

is_corporate = True if domain in corporate_domains else False

# 9. Соберите «чистый» текст сообщения без табов и переводов строк

email["clean_body"] = email["body"].replace('\t', '').replace('\n', '')

# 10. Сформируйте текст отправленного письма

email["sent_text"] = (f'Кому: {email["from"]}, '
                      f'от {email["to"]} '
                      f'Тема: {email["subject"]}, '
                      f'дата {email["date"]} '
                      f'{email["clean_body"]}')

# 11. Рассчитайте количество страниц печати для email["sent_text"]

pages = (len(email["sent_text"]) + 499) // 500

# 12. Проверьте пустоту темы и тела письма

is_subject_empty = True if len(email["subject"]) != 0 else False
is_body_empty = True if len(email["body"]) != 0 else False

# 13. Создайте «маску» e-mail отправителя

email["masked_from"] = login[:2] + '***@' + domain

# 14. Удалите из списка личных доменов
private_domains = list(private_domains)
private_domains.remove('list.ru')
private_domains.remove('bk.ru')

# Вывод результатов

pprint.pprint(email)
print()
print(f'login - {login}\ndomain - {domain}\nis_corporate - {is_corporate}')
print(f'pages - {pages}\nis_subject_empty - {is_subject_empty}\nis_body_empty - {is_body_empty}')