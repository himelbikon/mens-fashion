import smtplib
from users.models import Email


def send_mail(to, subject, message):
    email = get_email()

    server = smtplib.SMTP_SSL(email.server, email.port)
    server.login(email.address, email.password)
    server.sendmail(email.address, to,
                    f"Subject: {subject}\n{message}")
    server.quit()


def get_email():
    email = Email.objects.all().last()

    if len(Email.objects.all()) > 1:
        email.delete()
        get_email()
    else:
        return email
