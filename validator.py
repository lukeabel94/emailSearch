import sys
import re
import smtplib
import socket
from email_validator import validate_email, EmailNotValidError

def main(argv):

    # get the first argument as an email
    
    emailDict = isValidEmail(argv[0])

    email = emailDict["email"]
    mx = emailDict["mx"][0][1]

    print(pingEmail(email, mx))



def isValidEmail(email):

    try:
        # validate and get info
        v = validate_email(email)

        # replace with normalised
        #print(v)
        return v

    except EmailNotValidError as e:
        # email is not valid   
        return(str(e))

def pingEmail(email,mxRecord):

    host = socket.gethostname()

    server = smtplib.SMTP()
    server.set_debuglevel(0)

    #SMTP Conversation
    server.connect(mxRecord)
    server.helo(host)
    server.mail('me@domain.com')

    code, message = server.rcpt(str(email))
    server.quit()

    return(code)


if __name__ == "__main__":
    main(sys.argv[1:])