import csv
from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/<template_name>.html')
def render_templates(template_name):
    return render_template(f'{template_name}.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            save_to_database(data)
            return redirect('/thankyou.html')
        except Exception:
            return 'did not save to database'
    else:
        return 'nothing happened'


def save_to_database(data: dict[str, str]):
    with open('database.csv', newline='', mode='a') as csv_file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
