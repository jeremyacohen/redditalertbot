# redditalertbot
This bot scans reddit and sends an email if a post has a matching phrase
The bot uses PRAW, a reddit API for python, and it connects to a postgres database. You can change your information by sending the bot a private message. You can create a new user with your email and input up to 3 phrases to track. You can delete your account or remove any of your phrases. You can update your phrases or your email. You can also request to see your information.

The avaiable commands:
Put the phrase next to title in the title of your personal message to https://reddit.com/u/emailalertbot
Put the input information inside the parentheses and do not add any spaces or quotes.

Function: Create new account, it gets your username from your message. Submit up to 3 phrases, and only the first is required. You must submit use the term phrase1 even if you are only submitting one phrase.
Title: new
Body:
email()email

phrase1()phrase1

phrase2()phrase2

phrase3()phrase3

Function: delete all records
Title: delete
Body:
Can be anything, the bot does not look at the body

Function: delete phrase, you do not have to include any formatting or input any personal text with this, just the terms "phrase1", "phrase2", or "phrase3"
Title: delete phrase
Body:
phrase1
phrase2
phrase3

Function: update phrase
Title: update phrase
Body:
phrase1()phrase1
phrase2()phrase2
phrase3()phrase3

Function: update email
Title: update email
Body:
email()email

Function: This sends you a personal message with your email and your phrases
Title: get info
Body:
Can be anything, the bot does not look at the body





