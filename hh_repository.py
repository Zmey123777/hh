import requests as req
import os
import re


# Класс для работы с API HH
class HHRepository:

    # Не стал прятать т.к. эти методы API не требуют токена для авторизации - общедоступный URL.
    # Я взял первых 100 записей, по видимому будем считать что нам нужны свежие записи, при желании можно обработать пагинацию.
    URL = 'https://api.hh.ru/vacancies?text=python&area=1&area=2&per_page=100'


    def __init__(self) -> None:
        pass


    # Метод для парсинга данных по API HH
    def get_data(self) -> dict:
        data = req.get(self.URL)
        data = data.json()
        res = []
        for el in data['items']:
            if el.get('snippet'):
                requirement = el.get('snippet').get('requirement')
                responsibility = el.get('snippet').get('responsibility')
            else:
                requirement = ""
                responsibility = ""

            if self.seqrch_frame_work(requirement) or self.seqrch_frame_work(responsibility):
                if el.get('salary'):
                    salary_from = el.get('salary', {}).get('from')
                    salary_to = el.get('salary', {}).get('to')
                else:
                    salary_from = None
                    salary_to = None
                res.append({
                    'Название Компании': el.get('employer').get('name'),
                    'Город': el.get('area').get('name'),
                    'Вилка': {'от': salary_from, 'до': salary_to},
                    'Ссылка': el.get('url')
                    })
        return res

    
    # Метод для записи данных в файл
    def save_data(self, data: dict) -> None:
        file_path = os.path.join(os.getcwd(), 'data.json')
        with open(file_path, 'w', encoding='utf-8') as f:
            for item in data:
                f.write(f"{item}\n")


    # Метод для поиска необходимых фреймворков в описании вакансии
    def seqrch_frame_work(self, desc: str) -> bool:
         if desc:
            lower =  desc.lower()
            pattern = r'(?<!\w)(flask|django)(?!\w)'
            return bool(re.search(pattern, lower))
         else:
             return False


        