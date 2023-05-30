#import carPrinter

class CarApp:
    def __init__ (self, name, distance, time, price):
        self.name = name
        self.distance=distance
        self.time=time
        self.price = price
    
    def carSpeed(self):
        return (self.distance)//(self.time)

    def carName(self):
        return self.name

    def carPrice(self):
        return self.price 
        
        
    
Ford    = CarApp("Ford", 120,1.75,30000)
Ferrari = CarApp("Ferrari", 100,1.20, 100000)
BMW     = CarApp("BMW", 205,2.35 , 60000)
Porsche = CarApp("Porsche", 155,1.85, 70000)
Audi    = CarApp("Audi",190,2.10,  40000)
Jaguar  = CarApp("Jaguar",255,2.45,  20000)

'''dict_carPrice = ({1:Ford})
dict_carPrice.update({2:Ferrari})

for car in dict_car:
    print(car.carPrice())'''

carList_dict = dict({})

        # add values to dict variable
carList_dict.update({1: Ford})
carList_dict.update({2: Ferrari})
carList_dict.update({3: BMW})
carList_dict.update({4: Porsche})
carList_dict.update({5: Audi})
carList_dict.update({6: Jaguar})

#cp=carPrinter.CarPrinter()
#cp.printCarList(carList_dict)
#The result of dict

def depositMoney(self, bankAccount, amount):
        if amount > 20000:
            bankAccount.accountBalance += amount
        else:
            print("you cannot add negative amounts to the balance")



#print(carList_dict)
#for key in carList_dict:
#    print(str(carList_dict[key].carName())+ " has price: "+str(carList_dict[key].carPrice()) + " Euro")
car_list = [Ford, Ferrari, BMW, Porsche, Audi, Jaguar]
print("#"*80)
#'''

#Print when price is less than 30k and the vehicle is not a BMW
print("Print when price is less than 30k and the vehicle is not a BMW")
print("#"*80)
for car in car_list:
    #print(car.carName() + " speed in MPH:" + str(car.carSpeed()))

    if car.carName() == "BMW":
        #print("if the car is a BMW don't print the information")
        continue
    elif car.carPrice() > 30000:
        continue
    else:
       #print("if the car is a BMW don't print the information")
       print(car.carName() + " speed in MPH:" + str(car.carSpeed()))

#'''
print("#"*80)
'''print("#"*80)
#print("Ford speed in MPH:", Ford.cspeed())
print("Ferrari speed in MPH:", Ferrari.carSpeed())
print("BMW speed in MPH:", BMW.carSpeed())
print("Porsche speed in MPH:", Porsche.carSpeed())
print("Audi speed in MPH:", Audi.carSpeed())
print("Jaguar speed in MPH:", Jaguar.carSpeed())
'''
a=Ford.carSpeed()
b=Ferrari.carSpeed()
c=BMW.carSpeed()
d=Porsche.carSpeed()
e=Audi.carSpeed()
f=Jaguar.carSpeed()

def max_of_speed (a,b,c,d,e,f):
    fastest=a
    if fastest<b:
        fastest=b
    if fastest<c:
        fastest=c
    if fastest<d:
        fastest=d
    if fastest<e:
        fastest=e
    if fastest<f:
        fastest=f
    return fastest

speedlist = [Ford.carSpeed(), Ferrari.carSpeed(), BMW.carSpeed() , Porsche.carSpeed(), Audi.carSpeed(), Jaguar.carSpeed()]
def maxSpeed(speedlist):
    return max(speedlist)

#print(speedlist)
#print("The brand with the highest MPH is:" + str(max_of_speed(a,b,c,d,e,f)))
print("The brand with the highest MPH is:" + str(maxSpeed(speedlist)))