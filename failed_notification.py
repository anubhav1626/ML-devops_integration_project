import smtplib 
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
s.starttls()   
# Authentication 
s.login("anubhavpahwa2608@gmail.com", "ayaehshcvikmnjgi") 
# message to be sent 
message = "Hey Developer, you need to check your code once. Might be this have some error. "
# sending the mail 
s.sendmail("anubhavpahwa007@gmail.com", "anubhavpahwa2608@gmail.com", message) 
# terminating the session 
s.quit()
