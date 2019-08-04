import smtplib, ssl
from config import emailconfig
def sendEmail(receiver_email, phrase, link):
	message = """\
		Phrase %s found

		Post Title: %s""" % (phrase,link)
	params = emailconfig()
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(params[0], params[1], context=context) as server:
	    server.login(params[2], params[3])
	    server.sendmail(params[2], receiver_email, message)