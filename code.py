import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('devyanshilko@gmail.com','password')
matter = 'Hi! last minute submission, I so really want to get selected in this project as it is a really great learning opportunity.Humour was also asked for, but right now my humour quotient = zero, so here is a lame joke: Q. Why did a coder quit his job? A. because he was not getting arrays(a raise!XD Shit! I just reduced my chances of selection); P.S: please take me in, I promise i will work hard!! Just kidding XD(no i am not)'
s.sendmail('devyanshilko@gmail.com','kushgpt99@gmail.com', matter)
s.quit()
