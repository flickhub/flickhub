from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
from sqlalchemy.dialects.mysql.base import VARCHAR, LONGTEXT, INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from db_start import db_starter

def feed_back(feedback1):
    connection=db_starter()
    feedback2=feedback1
    email=feedback2["feedback"]["email"]
    first_name=feedback2["feedback"]["first_name"]
    last_name=feedback2["feedback"]["last_name"]
    question=feedback2["feedback"]["email"]
    feedback=feedback2["feedback"]["feedback"]
    quick_review=feedback2["feedback"]["quick_review"]
    
    sql="INSERT INTO feedback(email, first_name, last_name, question, feedback, quick_review) VALUES(:a,:b,:c,:d,:e,:f)"
    sql_query = sqlalchemy.text(sql)
    result = connection.execute(sql_query,a=str(email),b=str(first_name),c=str(last_name),d=str(question),e=str(feedback),f=str(quick_review))
    mail_content = "Name:-"+str(first_name)+" "+str(last_name)+"\nFeedback:-"+str(feedback)+"\nQuick Review:-"+str(quick_review)+"\nQuestion:-"+str(question)+"\nEmail:-"+str(email)
    #The mail addresses and password
    sender_address = 'info.flickhub@gmail.com'
    sender_pass = "buhkcilf20%"
    receiver_address = 'parth.verma96@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'FlickHub Feedback'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    connection.close()
    print('Mail Sent')
    
    
    