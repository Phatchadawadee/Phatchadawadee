# nested dictionary

car1 ={'brand':'Toyota','model':'Altis','price':800000}
car2 ={'brand':'Honda','model':'Civic','color':'Blue'}
car3 ={'brand':'M','model':'Altis','price':800000}

mycar = {'car1':car1,
         'car2':car2,
         'car3':car3}

print(mycar.get('car1'))
print(mycar.get('car2'))
print(mycar.get('car3'))

print(mycar['car1']['brand'])  # toyota

for x in mycar['car1']:
    print(x)
for x in mycar['car1']:
    print(mycar['car1'][x])