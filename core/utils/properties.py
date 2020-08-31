import re 
 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def check_email(email): 
    print(email)
    if(re.search(regex,email)):
        print("entro")
        return True
    else:
        return False
