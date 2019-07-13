# pickle
class Company(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

#or - less elegant:
#output = open('company_data.pkl', 'wb')
#company1 = ... WITHOUT INDENT

#no need for comments - code is self explaining <3
with open('company_data.pkl', 'wb') as output:
    company1 = Company('banana', 40)
    pickle.dump(company1, output, -1)

    company2 = Company('spam', 42)
    pickle.dump(company2, output, -1)

del company1
del company2

with open('company_data.pkl', 'rb') as input:
    company1 = pickle.load(input)
    print (company1.name)
    print (company1.value)

    company2 = pickle.load(input)
    print (company2.name)
    print (company2.value)


def save_object(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

#sample usage
#save_object(company1, 'company1.pkl')
