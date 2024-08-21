it_companies = {'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
length=len(it_companies)
it_companies.add('Twitter')
new_companies = {'Netflix','Adobe'}
it_companies.update(new_companies)
it_companies.remove('IBM')
print("Length of it_companies : ",length)
print("it_companies after adding Twitter : ",it_companies)
print("new_companies after updating : ",it_companies)
print("it-companies after removing : ",it_companies)