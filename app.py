import os

from flask import Flask, render_template, request

from wayscript import context

app = Flask(__name__)

@app.route('/404') 
def not_found():
    return render_template('404.html')

@app.route('/database_form')
def database_form():
    SELECTOR_OPTIONS = ['database_1', 'database_2', 'database_3', 'database_4']
    return render_template('index.html', selector_options = SELECTOR_OPTIONS )

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    database_name = request.form.get('database_selection')
    result = 'Success!'
    return render_template('submit_form.html', selected_database = database_name, result = result)

def get_current_user(request):
    application_key = request.headers.get('Authorization')[7:]
    user = context.get_user_by_application_key(application_key)
    return user

@app.route('/')
def index():
    user = get_current_user(request)
    first_name = user['first_name']
    return render_template('example.html',first_name=first_name)

if __name__ == '__main__':
    app.run()
