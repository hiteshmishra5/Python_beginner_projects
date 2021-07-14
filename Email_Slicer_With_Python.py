email = input('Enter Your Email ID:')
user_name = email[:email.index('@')]
host_name = email[email.index('@')+1:]
print(f"Your User Name is '{user_name}' and Host Name is '{host_name}'")