## giải bài
# import xml.etree.ElementTree as ET

# def word_cnt(s):
#     '''return strintg'''
#     s = s.split(' ')
    
#     dicts = {}
#     for ele in s:
#         if ele in dicts:
#             dicts[ele] += 1
#         else:
#             dicts[ele] = 1
            
#     print(dicts)
    
#     root = ET.Element('words')
#     for word, count in dicts.items():
#         word_ele = ET.SubElement(root, "words")
#         word_ele.text = word
#         count_ele = ET.SubElement(root, "count")
#         count_ele.text = str(count)
    
#     tree = ET.ElementTree(root)
#     output_file = "order.xml"
#     tree.write(output_file, xml_declaration=True, encoding = 'utf-8', method='xml')

# s = "hello world hello"
# word_cnt(s)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Thông tin email gửi đi:
FROM_EMAIL_ADDRESS = "nkochuy24h@gmail.com"
PASSWORD = "mgarqwozfdkyqmnx"

# Muốn gửi đến email nào?:
TO_EMAIL_ADDRESSES = ["nkochuy2203@gmail.com"]

def send_email(subject, msg, to_email, attachment_path=None):
    try:
        msg = MIMEMultipart()
        msg['From'] = FROM_EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(msg, 'plain'))

        if attachment_path:
            with open(attachment_path, "rb") as attachment:
                part = MIMEApplication(attachment.read())
            part.add_header('Content-Disposition', 'attachment', filename=attachment_path)
            msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(FROM_EMAIL_ADDRESS, PASSWORD)

        server.sendmail(FROM_EMAIL_ADDRESS, to_email, msg.as_string())
        server.quit()
        print("Success: Email sent!")
    except Exception as e:
        print("Email failed to send. Error:", str(e))

# Thay phần tiêu đề và tin nhắn tại đây
subject = "Today subject"
msg = "Hello there, how are you today? \n Hello I'm Huy. Nice to meet you"
attachment_path = "D:\image\had.png" # Đường dẫn tới file bạn muốn gửi kèm

for email_address in TO_EMAIL_ADDRESSES:
    send_email(subject, msg, email_address, attachment_path)
