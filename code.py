import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('devyanshilko@gmail.com','password')
content = ''
s.sendmail('devyanshilko@gmail.com','kushgpt99@gmail.com', content)
s.quit()
