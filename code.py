import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('devyanshilko@gmail.com','password')
content = 'Hi! last minute submission , humour quotient =zero:) P.S: please take me in, just kidding(no i am not)'
s.sendmail('devyanshilko@gmail.com','kushgpt99@gmail.com', content)
s.quit()
