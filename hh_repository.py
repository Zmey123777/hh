import requests as req
import os
import re


class HHRepository:

    def __init__(self) -> None:
        pass


    def get_data(self):
        url = 'https://api.hh.ru/vacancies?text=python&area=1&area=2'
        data = req.get(url)
        data = data.json()
        res = []
        for el in data['items']:
            requirement = el.get('snippet').get('requirement')
            responsibility = el.get('snippet').get('responsibility')
            if self.is_flask(requirement) or self.is_flask(responsibility):
                res.append({
                    'Название Компании': el.get('employer').get('name'),
                    'Город': el.get('area').get('name'),
                    'Вилка': {'от': el.get('salary').get('from'), 'до': el.get('salary').get('to')},
                    'Ссылка': el.get('url'),
                    'desc': el.get('snippet')
                    })
        print(res)


    def save_data(self, data) -> None:
        file_path = os.path.join(os.getcwd(), 'data.json')
        with open(file_path, 'w', encoding='utf-8') as f:
            for item in data:
                f.write(f"{item}\n")


    def is_flask(self, desc) -> bool:
         lower =  desc.lower()
         pattern = r'(?<!\w)(flask|django)(?!\w)'
         return bool(re.search(pattern, lower))

        