import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("satnalikamayank12@gmail.com", "Anjuaarushi.11")
def msgme(msg):
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("satnalikamayank12@gmail.com", "Anjuaarushi.11")
    server.sendmail("satnalikamayank12@gmail.com", "satnalikamayank12@gmail.com", msg)
    server.quit()

server.quit()
