from faker import Faker
import requests
import pandas as pd

fake = Faker()


def hello_user():
    return "Hello, User!"


def list_requirements():
    req_list = []
    count_lines = 0
    with open('requirements.txt') as f:
        for line in f:
            count_lines = count_lines + 1
            req_list.append(line)

    return req_list


def fake_names_emails():
    fake_name_email = []

    for i in range(100):
        fake_name_email.append(f'Name: {fake.name()};  Email: {fake.email()}')

    return fake_name_email


def people_space_count():
    r = requests.get('http://api.open-notify.org/astros.json').json()
    return r['number']


def mean_weight_height():
    data = pd.read_csv("hw (2) (1).csv")
    sum_weight = data.sum() / len(data)
    sum_dict = []

    for row in sum_weight:
        sum_dict.append(row)
    return sum_dict

