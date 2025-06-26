import smtplib
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, corpo):
    msg = MIMEText(corpo)
    msg['Subject'] = assunto
    msg['From'] = 'projeto.rpa@impacta.com'
    msg['To'] = destinatario

    try:
        smtp_server = 'sandbox.smtp.mailtrap.io'
        smtp_port = 587
        smtp_user = '226b46bc9d5b29'
        smtp_pass = 'SUA_SENHA_DO_MAILTRAP_AQUI'

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)

        print('✅ E-mail enviado com sucesso (via Mailtrap)!')

    except Exception as e:
        print('❌ Erro ao enviar e-mail:', e)
