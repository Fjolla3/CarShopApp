import BaseModel
import csv
class CarAppNew:
    def __init__ (self, name, id, price):
        self.name = name
        self.id = id
        self.price = price
    
    def carId(self):
        return self.id

    def carName(self):
        return self.name

    def carPrice(self):
        return self.price 

class CarPrinter:
    # create the method that prints the carList_dict 
    def printCarList(self, carList):
        for car in carList:
             print(str(carList[car].carName())+ " has price: "+str(carList[car].carPrice()) + " Euro")

    #print objects from list/array from csv file
    def printCarInfo(self, carList):
        for car in carList:
             print("ID: "+ str(car.carId())+" "+str(car.carName())+ " has a price: "+str(car.carPrice()) + " Euro")
    
             

class carImporter:
    def importCarListFromFile(self):
        # prepare csv file reading
        file = open('carList.csv')
        csvReader = csv.reader(file)
        
        cp = CarPrinter()
        carArray = []
        
        # for each row of csvReader read the data direct into car 
        for row in csvReader:
            car_id = row[0]
            car_type = row[1]
            car_price = row[2]

            car_obj = CarAppNew(car_type,car_id, car_price)

            carArray.append(car_obj)
        
        #call method for List
        cp.printCarInfo(carArray)

                     

ci = carImporter()
ci.importCarListFromFile()   