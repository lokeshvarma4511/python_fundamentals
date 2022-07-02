import smtplib

ser=smptlib.SMPT("smpt.gmail.com",portnum475)

ser.starttlp()

login('sendmail1@gmail.com',"passwd")

sendmail('sendmail@gmail.com','receivemail@gmail.com','msg')

print("mail sent")
