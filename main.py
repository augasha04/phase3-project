def main():
    
    #initialize carlist
    carlist = []
    
    infile = open("AugashaMotors.txt", "r")
    line = infile.readline()
    while line:
        carlist.append(line.rsplit("\n").split(","))
        line = infile.readline()
    infile.close()    
    
    # creating the car dealership menu
    choice = 0
    while choice != 4:
        print("*** CARS MENU ***")
        print("1. Order a car")
        print("2. Check a car")
        print("3. Print all cars")
        print("4. Exit")
        choice = int(input())
        
        if choice == 1:
            print("You are ordering at Augasha Motors")
            nbrand = input ("Brand of car: ")
            nhorsepower = input ("HorsePower of car: ")
            nwheels = input ("No of wheels of car: ")
            ncolor = input ("Color of car: ") 
            carlist.append([nbrand, nhorsepower, nwheels, ncolor])
            
        elif choice == 2:
            print("You are checking a car at Augasha Motors")
            keyword = input("search for a car: ")
            for car in carlist:
                if keyword in car:
                    print(car)
                    
        elif choice == 3:
            print("You are printing all cars at Augasha Motors")
            for i in range(len(carlist)):
                print(carlist[i])
                
        elif choice == 4:
            print("You are exiting the car dealership")
    print("Programme terminated, Thank you.")
    
    #saving to an extenal file.
    outfile = open("AugashaMotors.txt", "w")
    for car in carlist:
        outfile.write(",".join(car) + "\n")
    outfile.close()
    
                    
           
if __name__ == "__main__":
    main()
