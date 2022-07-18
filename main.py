
from flask import Flask, request
from utils import hello_user, list_requirements, fake_names_emails, people_space_count, mean_weight_height
import sqlite3

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
    data_html = f'<br>Average height - {data[1] * 2.54} cm</br>' \
                f'<br>Average weight - {data[2] * 0.45359} kg</br>'
    return data_html


# """less 2"""


@app.route('/emails/create')
def email_create():
    email = request.args['email']
    name = request.args['name']

    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        INSERT INTO emails
        VALUES ('{name}', '{email}');
        '''
        cur.execute(sql)
        conn.commit()
    finally:
        conn.close()

    return 'Emails create'


@app.route('/emails/read')
def email_read():

    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        SELECT * FROM emails;
        '''
        cur.execute(sql)
        emails = cur.fetchall()
    finally:
        conn.close()

    return str(emails)


@app.route('/emails/delete')
def email_delete():
    email = request.args['email']

    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        DELETE FROM emails WHERE Email == '{email}';
        '''
        cur.execute(sql)
        conn.commit()
    finally:
        conn.close()

    return 'Email delete'


@app.route('/emails/update')
def email_update():
    email = request.args['email']
    name = request.args['name']

    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        UPDATE emails
        SET UserName = '{name}'
        WHERE Email = '{email}';
        '''
        cur.execute(sql)
        conn.commit()
    finally:
        conn.close()

    return 'Emails update'


# Homework less3


@app.route('/phones/create')
def phones_create():
    phone = request.args['phone']
    name = request.args['name']

    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        INSERT INTO phones
        VALUES ('{name}', '{phone}');
        '''
        cur.execute(sql)
        conn.commit()
    finally:
        conn.close()

    return 'Phones create/add'


@app.route('/phones/read')
def phones_read():

    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        SELECT * FROM phones;
        '''
        cur.execute(sql)
        phones = cur.fetchall()
    finally:
        conn.close()

    return str(phones)


@app.route('/phones/update')
def phones_update():
    phone = request.args['phone']
    name = request.args['name']

    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        UPDATE phones
        SET UserName = '{name}'
        WHERE Email = '{phone}';
        '''
        cur.execute(sql)
        conn.commit()
    finally:
        conn.close()

    return 'Phones update'


@app.route('/phones/delete')
def phones_delete():
    phone = request.args['phone']

    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        DELETE FROM phones WHERE Email == '{phone}';
        '''
        cur.execute(sql)
        conn.commit()
    finally:
        conn.close()

    return 'Phone delete'


if __name__ == '__main__':
    app.run()

