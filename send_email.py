import os
import smtplib
from email.mime.text import MIMEText

def send_email():
    destinatario = os.getenv("EMAIL_DESTINO")
    if not destinatario:
        raise ValueError("Variável de ambiente EMAIL_DESTINO não configurada.")

    corpo = "Pipeline executado com sucesso no GitHub Actions!"
    msg = MIMEText(corpo)
    msg["Subject"] = "Notificação CI/CD"
    msg["From"] = "no-reply@github.com"
    msg["To"] = destinatario

    # Aqui estamos apenas simulando o envio (print).
    # Para envio real: configure servidor SMTP e use smtplib.SMTP(...)
    print(f"E-mail (simulado) enviado para {destinatario}: {corpo}")

if __name__ == "__main__":
    send_email()
