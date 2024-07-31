import requests as req
from hh_repository import HHRepository

if __name__ == '__main__':
    repository = HHRepository()
    repository.get_data()