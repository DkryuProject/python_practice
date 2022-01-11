from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from os.path import basename
from smtplib import SMTP_SSL
from io import BytesIO
from openpyxl.writer.excel import save_virtual_workbook

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = '465'
SMTP_USER = 'system@v-go.io'
SMTP_PASSWORD = 'daehan1996@5'

today = datetime.today().strftime("%Y-%m-%d")

def send_po_list(wb=False):
    msg = MIMEMultipart('alternative')
    
    if wb:
        msg = MIMEMultipart('mixed')
        
    msg['From'] = 'V-GO Team <%s>'%SMTP_USER
    msg['To'] = 'dkryu@v-go.io, fathur@daehan.co.id'
    msg['Subject'] = 'Dasom PO List('+today+')'

    text = MIMEText('This is the'+today+' PO list.\nHave a nice day') 
    msg.attach(text)
    
    if wb:
        try:
            file_data = MIMEBase('application', 'octet-stream')
            file_data.set_payload(save_virtual_workbook(wb))
            encoders.encode_base64(file_data)
        except Exception as e:
            print(e)
            
        #filename = basename(attachment)
        file_data.add_header('Content-Disposition', 'attachment', filename='PO_'+today+'.xlsx')
        msg.attach(file_data)
        
    smtp = SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    smtp.sendmail("system@v-go.io", msg["To"].split(","), msg.as_string())
    smtp.quit()