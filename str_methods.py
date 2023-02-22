
full_name = " Anna Sabadosh"
name_s = full_name.split()      # split returns list
print(full_name)
print(name_s)

ssn = "111-22-3333"
ssn_s = ssn.split('-')
print(ssn)
print(ssn_s)


full_name = "  Anna Sabadosh  = "
print(full_name)
name_clean = full_name.strip(' =')
print(name_clean)

print(full_name.upper())
print(full_name.lower())


url = "https://supersqa.com/"
is_home = url.endswith('.com/')
print(is_home)
is_absolute = url.startswith('https')
print(is_absolute)


info = "This%20is%20url%20encoded."
info.replace('%20' ,' ')
print(info)
info_rep = info.replace('%20' ,' ')
print(info_rep)

# formatting string
statement = f"there are {len('Python')} letters in Python word"
print(statement)

name = "Anya"
iam = f"My name is {name}"
print(iam)

age = 32
occupation = "software QA engineer"
print(f"I am {age} years old and work as {occupation}")
