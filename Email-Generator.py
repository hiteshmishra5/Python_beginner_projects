import random
first_name = ['hitesh', 'deepak', 'priyanshu', 'prasoon', 'kaushal', 'ayush', 'aditya']
f_name = random.choice(first_name)
last_name = ['mishra', 'mahaseth', 'chaudhary', 'thakur', 'jha', 'ranjan', 'ranjan']
l_name = random.choice(last_name)
numbers = str(random.randint(10, 1000))
domain_name = ['gmail.com', 'hubspot.com', 'outlook.com', 'yahoo.com', 'zoho.com']
d_name = random.choice(domain_name)
print(f_name+l_name+numbers+'@'+d_name)
