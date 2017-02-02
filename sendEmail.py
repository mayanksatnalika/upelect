import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("satnalikamayank12@gmail.com", "wkurfgeluqmcixlf")
def msgme(msg):
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("satnalikamayank12@gmail.com", "wkurfgeluqmcixlf")
    server.sendmail("satnalikamayank12@gmail.com", "satnalikamayank12@gmail.com", msg)
    server.quit()
    print 'email sent'

server.quit()
