#for exception handling
import sys

#for additional function
import numpy as np
import matplotlib.pyplot as plt

class Medicine:
    def __init__(self, index, medname, supname, purpose, quantity, costprice):
        self.__index = index
        self.__medname = medname
        self.__supname = supname
        self.__purpose = purpose
        self.__quantity = quantity
        self.__costprice = "{:.2f}".format(costprice)

    def set_medname(self, medname):
        self.__medname = medname

    def set_supname(self, supname):
        self.__supname = supname

    def set_purpose(self, purpose):
        self.__purpose = purpose

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_costprice(self, costprice):
        self.__costprice = "{:.2f}".format(costprice)

    def get_medname(self):
        return self.__medname

    def get_supname(self):
        return self.__supname

    def get_purpose(self):
        return self.__purpose

    def get_quantity(self):
        return self.__quantity

    def get_costprice(self):
        return self.__costprice

    def get_index(self):
        return self.__index

inventory={}


def display_menu():
    print("\nSelect the program (1-8) to run:\n1. Add new medicine record\n2. Update medicine record\n3. Remove a medicine record\n4. Display all medicine records"
          "\n5. Sort medicine records\n6. Search medicine record\n7. Visualize quantity (Additional Feature)\n8. Exit application")
    cmd=input("Enter your command (1-8) : ")
    return int(cmd)


def add():
    if len(inventory)<20:
        quantity = 0
        costprice = 0
        index = ''
        while index=='':
            try:
                index = int(input("Enter medicine record index: "))
                if index in inventory:
                    print('The inventory already has a record with index %d.'%index )
                    index = -1
            except EOFError:
                print('\nYou have quit the program.')
                sys.exit()
            except:
                print('Please enter only numbers for the index.')
        if index!=-1:
            try:
                medname = input("Enter medicine name: ")
                supname = input("Enter supplier name: ")
                purpose = input("Enter purpose of the medicine: ")
                while quantity<=0:
                    try:
                        quantity = int(input("Enter the medicine quantity: "))
                        if quantity<=0:
                            print("Please enter a valid quantity.")
                    except EOFError:
                        print('\nYou have quit the program.')
                        sys.exit()
                    except:
                        print("Please enter only numbers.")
                while costprice<=0:
                    try:
                        costprice = float(input("Enter cost price ($): "))
                        if costprice<=0:
                            print("Please enter a valid cost price.")
                    except EOFError:
                        print('\nYou have quit the program.')
                        sys.exit()
                    except:
                        print("Please enter only numbers.")
                med = Medicine(index, medname, supname, purpose, quantity, costprice)
                inventory[index] = med
            except EOFError:
                print('\nYou have quit the program.')
                sys.exit()
    else:
        print('The inventory is full. Please delete an existing record to add a new record.')


def update():
    index = -1
    quantity = -1
    costprice = -1
    while index<0:
        try:
            index = int(input("Enter medicine record index to change: "))
            if index<0:
                print("Please enter a valid index.")
        except EOFError:
            print('\nYou have quit the program.')
            sys.exit()
        except:
            print("Please enter only numbers.")
    if index in inventory:
        try:
            medname = input("What is the new medicine name? (Leave empty to remain unchanged): ")
            supname = input("What is the new supplier name? (Leave empty to remain unchanged): ")
            purpose = input("What is the new purpose? (Leave empty to remain unchanged): ")
            while quantity<0:
                try:
                    quantity = int(input("What is the new quantity? (Enter 0 to remain unchanged): "))
                    if quantity<0:
                        print("Please enter a valid quantity.")
                except EOFError:
                    print('\nYou have quit the program.')
                    sys.exit()
                except:
                    print("Please enter only numbers.")
            while costprice<0:
                try:
                    costprice = float(input("What is the new cost price ($)? (Enter 0 to remain unchanged): "))
                    if costprice<0:
                        print("Please enter a valid cost price.")
                except EOFError:
                    print('\nYou have quit the program.')
                    sys.exit()
                except:
                    print("Please enter only numbers.")
            if len(medname)>0:
                inventory[index].set_medname(medname)
                print("Medicine",index,"name updated")
            if len(supname)>0:
                inventory[index].set_supname(supname)
                print("Medicine",index,"supplier updated")
            if len(purpose)>0:
                inventory[index].set_purpose(purpose)
                print("Medicine",index,"purpose updated")
            if quantity>0:
                inventory[index].set_quantity(quantity)
                print("Medicine",index,"quantity updated")
            if costprice>0:
                inventory[index].set_costprice(costprice)
                print("Medicine",index,"costprice updated")
        except EOFError:
            print('\nYou have quit the program.')
            sys.exit()
    else:
        print("Record index not found, try again!")


def remove():
    index=-1
    while index<0:
        try:
            index = int(input("Enter medicine record index to remove: "))
            if index<0:
                print("Please enter a valid index.")
        except EOFError:
            print('\nYou have quit the program.')
            sys.exit()
        except:
            print("Please enter only numbers.")
    if index in inventory:
        inventory.pop(index, None)
        print("Medicine", index, "has been removed from inventory.")
    else:
        print("Record index not found, try again!")


def display_record(medicine):
    print('\nMedicine Record:', medicine.get_index())
    print('Medicine Name:', medicine.get_medname())
    print('Supplier Name:', medicine.get_supname())
    print('Purpose:', medicine.get_purpose())
    print('Quantity:', medicine.get_quantity())
    print('Cost Price ($):', medicine.get_costprice())


def display_inventory():
    if len(inventory)>0:
        for medicine in inventory.values():
            display_record(medicine)
    else:
        print('There are currently no medicine records.')


def medicine_insertion_sort(list, param):
    for i in range(1, len(list)):
        pos = i
        value = list[i]
        if param == 'i':
            while pos>0 and value.get_index() < list[pos-1].get_index():
                list[pos] = list[pos-1]
                pos-=1
        elif param == 'mn':
            while pos>0 and value.get_medname() < list[pos-1].get_medname():
                list[pos] = list[pos-1]
                pos-=1
        elif param == 'sn':
            while pos>0 and value.get_supname() < list[pos-1].get_supname():
                list[pos] = list[pos-1]
                pos-=1
        elif param == 'p':
            while pos>0 and value.get_purpose() < list[pos-1].get_purpose():
                list[pos] = list[pos-1]
                pos-=1
        elif param == 'q':
            while pos>0 and value.get_quantity() < list[pos-1].get_quantity():
                list[pos] = list[pos-1]
                pos-=1
        else:
            while pos>0 and value.get_costprice() < list[pos-1].get_costprice():
                list[pos] = list[pos-1]
                pos-=1
        list[pos] = value
    return list


def medicine_bubble_sort(list, param):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if param == 'i':
                if list[j].get_index() > list[j+1].get_index():
                    tmp = list[j]
                    list[j] = list[j + 1]
                    list[j + 1] = tmp
            elif param == 'mn':
                if list[j].get_medname() > list[j+1].get_medname():
                    tmp = list[j]
                    list[j] = list[j + 1]
                    list[j + 1] = tmp
            elif param == 'sn':
                if list[j].get_supname() > list[j+1].get_supname():
                    tmp = list[j]
                    list[j] = list[j + 1]
                    list[j + 1] = tmp
            elif param == 'p':
                if list[j].get_purpose() > list[j+1].get_purpose():
                    tmp = list[j]
                    list[j] = list[j + 1]
                    list[j + 1] = tmp
            elif param == 'q':
                if list[j].get_quantity() > list[j+1].get_quantity():
                    tmp = list[j]
                    list[j] = list[j + 1]
                    list[j + 1] = tmp
            else:
                if list[j].get_costprice() > list[j+1].get_costprice():
                    tmp = list[j]
                    list[j] = list[j + 1]
                    list[j + 1] = tmp
    return list


def medicine_selection_sort(list, param):
    for i in range(len(list)-1):
        min_index = i
        for j in range(i+1, len(list)):
            if param == 'i':
                if list[j].get_index() < list[min_index].get_index():
                    min_index = j
            elif param == 'mn':
                if list[j].get_medname() < list[min_index].get_medname():
                    min_index = j
            elif param == 'sn':
                if list[j].get_supname() < list[min_index].get_supname():
                    min_index = j
            elif param == 'p':
                if list[j].get_purpose() < list[min_index].get_purpose():
                    min_index = j
            elif param == 'q':
                if list[j].get_quantity() < list[min_index].get_quantity():
                    min_index = j
            else:
                if list[j].get_costprice() < list[min_index].get_costprice():
                    min_index = j
        tmp = list[i]
        list[i] = list[min_index]
        list[min_index] = tmp
    return list


def sort():
    medlist = [medicine for medicine in inventory.values()]
    type = ''
    param = ''
    choices = ['i', 'b', 's']
    parameters = ['i', 'mn', 'sn', 'p', 'q', 'cp']
    while type not in choices:
        try:
            type = input("\nEnter the type of sorting algorithm you want to use (Insertion:I / Bubble:B / Selection:S) : ").lower()
            if type not in choices:
                print("\nPlease enter a valid sorting algorithm.")
        except EOFError:
            print('\nYou have quit the program.')
            sys.exit()
    while param not in parameters:
        try:
            param = input("\nEnter the medicine attribute to be sorted (Index: I, Medicine Name:MN, Supplier Name:SN, Purpose:P, Quantity:Q, Cost Price: CP) : ").lower()
            if param not in parameters:
                print("\nPlease enter a valid medicine attribute.")
        except EOFError:
            print('\nYou have quit the program.')
            sys.exit()
    inventory.clear()
    if type == choices[0]:
        medlist = medicine_insertion_sort(medlist, param)
    elif type == choices[1]:
        medlist = medicine_bubble_sort(medlist, param)
    else:
        medlist = medicine_selection_sort(medlist, param)
    for medicine in medlist:
        inventory[medicine.get_index()] = medicine
    display_inventory()


def linear_search(list, target):
    indexes = []
    for i in range(len(list)):
        if list[i][1] == target:
            indexes.append(list[i][0])
    return indexes


def binary_search(list, target):
    indexes = []
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (high + low) // 2
        if list[mid][1] == target:
            first_occurrence = mid
            cont = True
            while first_occurrence > 0 and cont:
                if list[first_occurrence - 1][1] == target:
                    first_occurrence -=1
                else:
                    cont = False
            last_occurrence = mid
            cont = True
            while last_occurrence < len(list)-1 and cont:
                if list[last_occurrence + 1][1] == target:
                    last_occurrence +=1
                else:
                    cont = False
            for medicine in list[first_occurrence:last_occurrence + 1]:
                indexes.append(medicine[0])
            return indexes
        elif target < list[mid][1]:
            high = mid - 1
        else:
            low = mid + 1
    return []

def search():
    indextosupname = [(medicine.get_index(), medicine.get_supname()) for medicine in inventory.values()]
    indextosupname = sorted(indextosupname, key = lambda item:item[1])
    indextomedname = [(medicine.get_index(), medicine.get_medname()) for medicine in inventory.values()]
    indextomedname = sorted(indextomedname, key = lambda item:item[1])
    type = ''
    choices = ['b', 'l']
    supname = ''
    medname = ''
    while type not in choices:
        try:
            print('Binary search uses supplier name as the search key. Linear search uses medicine name as the supplier key.')
            type = input("Enter the type of search algorithm you want to use (Binary:B / Linear:L) : ").lower()
            if type not in choices:
                print("Please enter a valid search algorithm.")
        except EOFError:
            print('\nYou have quit the program.')
            sys.exit()
    if type == choices[0]:
        while supname == '':
            try:
                supname = input("Enter the supplier name to search (case-sensitive): ")
                if supname == '':
                    print('Please enter a valid supplier name.')
            except EOFError:
                print('\nYou have quit the program.')
                sys.exit()
        result = binary_search(indextosupname, supname)
        if len(result)!=1:
            print("\nTHERE ARE %d MEDICINE RECORDS WITH THE SUPPLIER NAME '%s'."%(len(result), supname))
        else:
            print("\nTHERE IS 1 MEDICINE RECORD WITH THE SUPPLIER NAME '%s'."%supname)
    else:
        while medname == '':
            try:
                medname = input("Enter the medicine name to search (case-sensitive): ")
                if medname == '':
                    print('Please enter a valid medicine name.')
            except EOFError:
                print('\nYou have quit the program.')
                sys.exit()
        result = linear_search(indextomedname, medname)
        if len(result)!=1:
            print("\nTHERE ARE %d MEDICINE RECORDS WITH THE MEDICINE NAME '%s'."%(len(result), medname))
        else:
            print("\nTHERE IS 1 MEDICINE RECORD WITH THE MEDICINE NAME '%s'."%medname)
    for index in result:
        display_record(inventory[index])

#additional function
def visualize():
    height = [medicine.get_quantity() for medicine in inventory.values()]
    bars = [medicine.get_medname() for medicine in inventory.values()]
    x_pos = np.arange(len(bars))
    plt.bar(x_pos, height)
    plt.xticks(x_pos, bars)
    plt.title('Quantity for each Medicine')
    plt.xlabel('Medicine')
    plt.ylabel('Quantity')
    plt.show()

if __name__ == '__main__':
    def fill_inventory():
        mednamelist = ['Tamiflu', 'Labetalol', 'Paracetamol', 'Ibuprofen', 'Acetaminophen', 'Humalog']
        supnamelist = ['Aa', 'Bb', 'Cc', 'Dd', 'Bb', 'Ff']
        purpose = ['flu', 'high blood pressure', 'fever', 'sore throat', 'headache', 'diabetes']
        quantity = [10, 20, 15, 60, 5, 7]
        cost = [70, 80, 10, 20, 30, 10]
        for i in range(6):
            med = Medicine(i+1, mednamelist[i], supnamelist[i], purpose[i], quantity[i], cost[i])
            inventory[i+1] = med
    fill_inventory()
    while True:
        try:
            val=display_menu()
        except EOFError:
            print('\nYou have quit the program.')
            sys.exit()
        except:
            print('\nPLEASE ENTER A VALID CHOICE.')
            continue
        if val==8:
            print('\nYou have quit the program.')
            break
        elif val==1:
            add()
        elif val==2:
            update()
        elif val==3:
            remove()
        elif val==4:
            display_inventory()
        elif val==5:
            sort()
        elif val==6:
            search()
        #additional function
        elif val==7:
            visualize()
        else:
            print('Please choose a number from 1 to 7.')



