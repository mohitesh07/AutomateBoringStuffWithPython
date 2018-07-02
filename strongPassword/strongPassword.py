# STRONG PASSWORD DETECTION
#
# What is a strong password? >> It is one that both lowerCase and upperCase
#   >> Characters has atleast one digit. It has minimum 8 characters.


import re    # >> step 1

def strongPasswordDetector(string):
    passwordRegexDigit = re.compile(r'\d')
    passwordRegexAlph = re.compile(r'[a-z]')
    passwordRegexlowerAlpha = re.compile(r'[A-Z]')

    digitArray = passwordRegexDigit.findall(string)
    alphaArray = passwordRegexAlph.findall(string)
    lowerAlpha = passwordRegexlowerAlpha.findall(string)

    flag=0

    if len(string)>=8:
        if len(digitArray)>0 and len(alphaArray)>0 and len(lowerAlpha)>0:
            flag=1

    if flag==1:
        return 'Strong Password'
    else:
        return 'Password should have atleast 1 lowercase, 1 uppercase, 1 digit and length must be minimum eight'

# >> taking i/p from the user
print('Enter the password: ')
passkey = input()

# >> checking whether the password is strong or not
print(strongPasswordDetector(passkey))
    


