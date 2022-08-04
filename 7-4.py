import email
import profile
from faker import Faker

fake_data = Faker()

name = fake_data.name(); 
print(name)
address = fake_data.address(); 
print(address)
emial = fake_data.email(); 
print(emial)

print ("\n")

file = fake_data.simple_profile()
for k,v in file.items():
    print('{}, {}'.format(k,v))

print("\n")

print('Name: {}, \nAddress: {}, \nEmail: {}'.format(name,address,emial))
for _ in range (0,200):
        print(fake_data.name())

print ('\n')