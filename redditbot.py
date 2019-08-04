import praw
from config import scannerconfig
from insertpostgres import getAllEmails, getAllPhrases
from redditemail import sendEmail
# create the objects from the imported modules

# reddit api login
params = scannerconfig()
reddit = praw.Reddit(**params)

# the subreddits you want your bot to live on
subreddit = reddit.subreddit('emailalertbot')  

phrases = getAllPhrases()
for post in subreddit.stream.submissions():
    for word in phrases:
        if word[0] in post.title:
            emails = getAllEmails(word[0])
            for item in emails:
                sendEmail(item[0], word[0], post.url)

#!/usr/bin/python 


            
        
        

