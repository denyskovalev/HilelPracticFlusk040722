from flask import Flask
from utils import hello_user, list_requirements, fake_names_emails, people_space_count, mean_weight_height

app = Flask(__name__)


@app.route('/')
def hello():
    return hello_user()


@app.route('/requirements')
def requirements():
    req_list = list_requirements()
    req_html = ''

    for i in req_list:
        req_html += f'<br>{i}</br>'
    return req_html


@app.route('/generate-users')
def generate_users():
    new_generate = fake_names_emails()
    generate_html = ''

    for i in new_generate:
        generate_html += f'<br>{i}</br>'
    return generate_html


@app.route('/space')
def space():
    people_space_html = f'Now in space >{people_space_count()}< people!'
    return people_space_html


@app.route('/mean')
def mean():
    data = mean_weight_height()
    data_html = f'<br>Average height - {data[1] * 2.54}</br>' \
                f'<br>Average weight - {data[2] * 0.45359}</br>'
    return data_html


if __name__ == '__main__':
    app.run()

