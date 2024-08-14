import re




#validate email address
#with this if sucks
#if "@" in email and "." in email:
#    print("valid")
#else:
#    print("invalid")

#this is a bit better
#username,domain = email.split("@")

#if username and "." in domain:
#if username and domain.endswith("nl"):
#    print ("valid")
#else:
#    print ("Invalid")

#regex

#. any char except a newline
#* 0 or more chars repetitions
#+ 1 or more chars repetitions
#? 0 or 1 repetition of a char
#{m} m repetitions of a char
#{m,n} m to n repetitions of a char
#^ matches the start of a string 
#$ matches the end of a string just before the new lines at the end of the string
#[] set of chars
#[^] complementing the set, cannot match any of these chars
#\w word every char a-z A-Z 0-9 and _
#\W not word
#\d decimal digit
#\D not a decimal digit
#\s whitespace 
#\S not whitespace
# A|B can be A or B
# (...) a group
# (?:...) non-capturing version

#re.IGNORECASE
#re.MULTILINE 
#re.DOTALL -> . will be all char incl. newline

email = input("What's your email?").strip()

#if re.search(r"^[^@]+@[^@]+\.nl$",email):
#if re.search(r"^[a-zA-Z0-9_\.]+@[a-zA-Z0-9_]+\.nl$",email):
#? in het tweede gedeelte heeft aan dat alles ervoor tussen haakjes
# er wel of niet kan zijn

#^(\w|\.)+ => voor de @ 
# ^ begin van string
# (\w|\.) iedere chars of .
#  (\w+\.)?\w+\.(nl|com|edu|gov)$ => na de @
# Optioneel (\w+\.)? meerder chars en een punt (subdomain)
# \w+\. domain
#(extnesion)
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(nl|com|edu|gov)$",email,flags=re.IGNORECASE):
    print("valid")
else:
    print("invalid")


