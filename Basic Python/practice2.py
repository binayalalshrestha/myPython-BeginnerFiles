# userName = input("Enter User Name : \n")
# greetingMessage = (", Good Afternoon !!")
# zxcv = userName + greetingMessage
# print(zxcv)

# letter = '''Dear <|NAME|>,
# Greetings from Grepsr Co Ltd. I am happy to tell you that:
# You are selected!
# More information will be given on-
# Date: <|DATE|>
# Have a great day!!
# '''
# name = input("Enter your name : \n")
# date = input("Enter the date : \n")
# letter = letter.replace("<|NAME|>", name)
# letter = letter.replace("<|DATE|>",date)
# print(letter)



letter = '''
Respected Sir/Madam,
<|Company Name|>,
<|Address|>.

HAPPY NEW YEAR 2023!!!
Wishing you a successful journey ahead!!!

Yours Sincerely,
<|Your Name|>
<|Post|>
'''
companyName = input("Enter Company Name: \n")
companyAddress = input("Enter Company Address: \n")
yourName = input("Enter Sender Name: \n")
yourPost = input("Enter Post in Company: \n")
letter = letter.replace("<|Company Name|>", companyName)
letter = letter.replace("<|Address|>", companyAddress)
letter = letter.replace("<|Your Name|>", yourName)
letter = letter.replace("<|Post|>", yourPost)
print(letter)



# st = "This is a string with double  spaces"
# doubleSpaces = st.find("  ")
# print(doubleSpaces)

# dbr = "Hakuna  Matata"
# dbr = dbr.replace("  "," ")
# print(dbr)



# letter =('''
# Dear Binay,\n This Python course is nice.\n \t Thanks!
# ''')
# print(letter)