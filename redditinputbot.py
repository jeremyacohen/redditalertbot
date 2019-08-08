import praw
from config import responseconfig
from insertpostgres import insert_name, deleteuser, updateInfo, getInfo, insertPhrasesUsers, userExist, getAllEmails, getAllPhrases, updatephrase, deletephrase
import time

# create the objects from the imported modules

# reddit api login
params = responseconfig()
reddit = praw.Reddit(**params)

def getRedditText(message):
    body = post.body
    name = str(message.author)
    if (message.subject == "new" or message.subject == "update phrase"):
        phrase1index = body.find("phrase1(")
        phrase1endindex = body.find(")phrase1")
        phrase2index = body.find("phrase2(")
        phrase2endindex = body.find(")phrase2")
        phrase3index = body.find("phrase3(")
        phrase3endindex = body.find(")phrase3")

    if (message.subject == "new" or message.subject == "update email"):
        emailindex = body.find("email(")
        emailendindex = body.find(")email")
        if (emailindex == -1 or emailendindex == -1):
            reddit.redditor(name).message('Incorrect Input', 'You have inputted your email in an incorrect format. Please submit your email as such: email(example@example.com)email')
            return
        email = body[emailindex+6 : emailendindex]
        
    if (message.subject == "new"):
        if (userExist(name) == 1):
            reddit.redditor(name).message('User already exists', 'You have previously signed up. You can instead update your information.')
            return
        
        if (phrase1index == -1 or phrase1endindex == -1):
            reddit.redditor(name).message('Incorrect Input', 'You have not submitted any phrases or in incorrect format. Please submit as such: phrase1(example)phrase1')
            return;
        
        phrase1 = PhraseSetter(phrase1index, phrase1endindex, body)
        phrases = [phrase1]
        if phrase2index != -1 and phrase2endindex != -1:
            phrase2 = PhraseSetter(phrase2index, phrase2endindex, body)
            phrases.append(phrase2)
        if phrase3index != -1 and phrase3endindex != -1:
            phrase3 = PhraseSetter(phrase3index, phrase3endindex, body)
            phrases.append(phrase3)
 
        insert_name(name, email, phrases)
        insertPhrasesUsers(phrases, name)
    elif (message.subject == "delete"):
        if (UserNotExist(name)):
            return
        deleteuser(name)
    elif (message.subject == "update email"):
        if (UserNotExist(name)):
            return
        updateInfo(name, email, "email")
    elif (message.subject == "update phrase"):
        if (UserNotExist(name)):
            return
        phrases = {}
        if phrase1index == -1 and phrase1endindex == -1 and phrase2index == -1 and phrase2endindex == -1 and phrase3index == -1 and phrase3endindex == -1:
            reddit.redditor(name).message('No phrase', 'You have not submitted any phrases to update')
            return
        if phrase1index != -1 and phrase1endindex != -1:
            phrases[1] = PhraseSetter(phrase1index, phrase1endindex, body)
        if phrase2index != -1 and phrase2endindex != -1:
            phrases[2] = PhraseSetter(phrase2index, phrase2endindex, body)
        if phrase3index != -1 and phrase3endindex != -1:
            phrases[3] = PhraseSetter(phrase3index, phrase3endindex, body)
        updatephrase(name, phrases)
    elif (message.subject == "delete phrase"):
        if (UserNotExist(name)):
            return
        phrase1index = body.find("phrase1")
        phrase2index = body.find("phrase2")
        phrase3index = body.find("phrase3")
        phrases = []
        if phrase1index == -1 and phrase2index == -1 and phrase3index == -1:
            reddit.redditor(name).message('No phrase', 'You have not submitted any phrases to delete')
            return
        if phrase1index != -1:
            phrases.append(1)
        if phrase2index != -1:
            phrases.append(2)
        if phrase3index != -1:
            phrases.append(3)
        deletephrase(name, phrases)
    elif (message.subject == "get info"):
        if (UserNotExist(name)):
            return
        info = getInfo(name)
        reddit.redditor(name).message('Your Information', 'Username: ' + str(info[0]) + '\n\nEmail: ' + str(info[2]) + '\n\nPhrase 1: ' + str(info[3]) + '\n\nPhrase 2: ' + str(info[4]) + '\n\nPhrase 3: ' +str(info[5]))
    else:
        reddit.redditor(name).message('Invalid Command', 'You have not inputted a valid title command')
def UserNotExist(name):
    if (userExist(name) == 0):
        reddit.redditor(name).message('No User', 'Your account has not been found.')
        return True
    else:
        return False
def PhraseSetter(start, end, body):
    return body[start+8 : end]

while True:
    unread_messages = []
    for post in reddit.inbox.unread(): # messages or unread
        getRedditText(post)
        unread_messages.append(post)
    if len(unread_messages) == 0:
        print("No new messages")
    reddit.inbox.mark_read(unread_messages)
    time.sleep(15)





#!/usr/bin/python 


            
        
        

