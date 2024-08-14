import re
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

name = input("What is your name?").strip()
#if "," in name:
#    last,first = name.split(", ")
#    name = f"{first} {last}"
#print(f"Hello, {name}")

#matches geeft groepen tussen () terug als list
#groups 0 geeft hele string terug
#matches = re.search(r"^(.+), *(.+)$", name)
#if matches:
#    last,first = matches.groups()
#    name = f"{first} {last}"

#:= use in if to assign and evaluate boolean
if matches := re.search(r"^(.+), *(.+)$", name):
    last,first = matches.groups()
    name = f"{first} {last}"

print(f"Hello, {name}")