from hh_repository import HHRepository


if __name__ == '__main__':
    repository = HHRepository()
    # Парсим данные по API hh.ru
    print(f'Получаем данные по API')
    hh_data = repository.get_data()
    # Записываем получаенные данные в файл
    repository.save_data(hh_data)
    print(f'Данные успешно записаны в файл data.json')
