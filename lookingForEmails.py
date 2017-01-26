# This program filter email accounts

import re, pyperclip

emailRegex = re.compile(r'''(
[a-zA-Z0-9._+-]+        # username
@			            #  symbol
[a-zA-Z0-9.-]+		    # domain name
\.[a-zA-Z]{2,4} 	    # dot something
)''', re.VERBOSE)

text = str(pyperclip.paste())
addMails = ''

for mails in emailRegex.findall(text):
    addMails += mails + '\n'

try:
    emailDoc = open('C:\\Users\\All users\\Desktop\\List_Of_Mails.txt', 'w')
    emailDoc.write('%s' % (addMails))
    emailDoc.close()
except Exception:
    emailDoc = open('List_Of_Mails.txt', 'w')
    emailDoc.write('%s' % (addMails))
    emailDoc.close()
