from flask import Flask, request
from flask_mail import Mail, Message
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'seu_email@gmail.com'  # Substitua pelo seu email
app.config['MAIL_PASSWORD'] = 'sua_senha'  # Substitua pela sua senha

mail = Mail(app)

emails_with_received_dates = {}


@app.route('/add-emails', methods=['POST'])
def add_emails():
    emails = request.form['emails'].split(',')
    for email in emails:
        if email in emails_with_received_dates:
            print(f"Email {email} already exists. Skipping.")
            continue

        received_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        emails_with_received_dates[email] = received_date

        print(f"Email {email} added with received date: {received_date}")

    return 'Emails adicionados com sucesso!'


scheduler = BlockingScheduler()


def schedule_email(email, received_date):
    # Altere a data
    send_date_time_obj = datetime.datetime.strptime(received_date, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(days=7)
    send_date_time = send_date_time_obj.strftime("%Y-%m-%d %H:%M:%S")

    scheduler.add_job(
        lambda: send_email_function(email),
        'date',
        run_date=send_date_time_obj
    )


for email, received_date in emails_with_received_dates.items():
    schedule_email(email, received_date)

scheduler.start()


def send_email_function(email):
    msg = Message('Assunto do Email', sender='seu_nome@gmail.com', recipients=[email])  # Substitua pelo seu email
    msg.body = 'Este é o corpo do email que será enviado automaticamente.'  # Substitua pelo conteúdo do email
    mail.send(msg)


if __name__ == '__main__':
    app.run(debug=True)
