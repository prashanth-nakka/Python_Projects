import smtplib as sm

ob = sm.SMTP('smtp.gamil.com', 535)  # port of gmail = 587

ob.ehlo()
ob.starttls()
ob.login('prashanth041997@gmail.com', 'password')
subject = "Test Python"
body = "I love Python"
msg = "subject: {}\n\n{}".format(subject, body)
print(msg)
listadd = ['prashanth041997@gmail.com', 'prasanthnakka97@gmail.com']

# To Send mail to receivers
ob.sendmail('prashanth041997@gmail.com', listadd, msg)
print("Mail Sent Successfully!")

# To Close Server
ob.quit()
