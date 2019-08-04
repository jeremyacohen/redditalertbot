import praw
from config import responseconfig
from insertpostgres import insert_name, deleteuser, updateInfo, getInfo, insertPhrasesUsers, userExist, getAllEmails, getAllPhrases

# create the objects from the imported modules

# reddit api login
params = responseconfig()
reddit = praw.Reddit(**params)

def getRedditText(message):
    body = post.body
    name = str(message.author)
    if (message.subject == "new"):
        if (userExist(name) == 1):
            reddit.redditor(name).message('User already exists', 'You have previously signed up. You can instead update your information.')
            return
        emailindex = body.find("email(")
        emailendindex = body.find(")email")
        if (emailindex == -1 or emailendindex == -1):
            reddit.redditor(name).message('Incorrect Input', 'You have inputted your email in an incorrect format. Please submit your email as such: email(example@example.com)email')
            return

        phrase1index = body.find("phrase1(")
        phrase1endindex = body.find(")phrase1")
        if (phrase1index == -1 or phrase1endindex == -1):
            reddit.redditor(name).message('Incorrect Input', 'You have not submitted any phrases or in incorrect format. Please submit as such: phrase1(example)phrase1')
            return;

        email = body[emailindex+6 : emailendindex]
        phrase1 = body[phrase1index+8 : phrase1endindex]
        phrases = [phrase1]
        phrase2index = body.find("phrase2(")
        phrase2endindex = body.find(")phrase2")
        phrase3index = body.find("phrase3(")
        phrase3endindex = body.find(")phrase3")
        if phrase2index != -1 and phrase2endindex != -1:
            phrase2 = body[phrase2index+8 : phrase2endindex]
            phrases.append(phrase2)
        if phrase3index != -1 and phrase3endindex != -1:
            phrase3 = body[phrase3index+8 : phrase3endindex]
            phrases.append(phrase3)
 
        insert_name(name, email, phrases)
        insertPhrasesUsers(phrases, name)
    elif (message.subject == "delete"):
        deleteuser(name)
    elif (message.subject == "update email"):
        if (userExist(name) == 0):
            reddit.redditor(name).message('No User', 'Your account has not been found.')
            return
        emailindex = body.find("email(")
        emailendindex = body.find(")email")
        if (emailindex == -1 or emailendindex == -1):
            reddit.redditor(name).message('Incorrect Input', 'You have inputted your email in an incorrect format. Please submit your email as such: email(example@example.com)email')
            return
        email = body[emailindex+6 : emailendindex]
        updateInfo(name, email, "email")
    elif (message.subject == "get info"):
        if (userExist(name) == 0):
            reddit.redditor(name).message('No User', 'Your account has not been found.')
            return
        info = getInfo(name)
        reddit.redditor(name).message('Your Information', 'Username: ' + str(info[0]) + '\n\nEmail: ' + str(info[2]) + '\n\nPhrase 1: ' + str(info[3]) + '\n\nPhrase 2: ' + str(info[4]) + '\n\nPhrase 3: ' +str(info[5]))
    else:
        reddit.redditor(name).message('Invalid Command', 'You have not inputted a valid title command')

unread_messages = []
for post in reddit.inbox.unread(): # messages or unread
    getRedditText(post)
    unread_messages.append(post)
if len(unread_messages) == 0:
    print("No new messages")
reddit.inbox.mark_read(unread_messages)





#!/usr/bin/python 


            
        
        

