import csv
stopper =True
dictionary = { }

def saveToCSVFile():
    
    with open('items.csv', 'w', newline='') as items:
        item_writer = csv.writer(items, delimiter=',')

        

        for trackingNumber in dictionary:
            item_writer.writerow([trackingNumber] + dictionary.get(trackingNumber))
            
        


def loadCSVFile():
    with open('items.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        loadItems = list(csv_reader)
        if loadItems==0:
            print("No items")
        else:
            for item in loadItems:
                dictionary[item[0]]= [item[1], item[2], item[3], item[4], item[5]]
            print("Succesfully loaded")

        '''
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')
        '''


n=1
while(stopper):
    inp = int(input("[1] add item \n[2]View an Item \n[3]View all Items \n[4]Delete all an item"
                    " \n[5]Delete all items\n[6]save to file\n[7]Load from Files \n[0] Exit \nEnter choice: "))
    if(inp ==1):
        #ADD ITEM

        tracker= input("Input tracking number: ") #key
        supplier =input("Enter Supplier Name: ")  # values
        itemN= input("Enter Item Name: ")
        typeN = input("Enter type of item: ")
        condition= input("Enter Item Condition: ")
        stockN= input("How many in stocks")

        dictionary[tracker]= [supplier,itemN,typeN,condition,stockN]


        print("Successfuly Added")
        

    if(inp==2):
        if (len(dictionary)==0):
            print("No items")
        else:
            trackingNumber = input("Enter Tracking number:")
            if (trackingNumber not in dictionary):
                print("It don't exist")
            else:
                listOfItems = dictionary.get(trackingNumber)
                parsedItems = " - ".join(listOfItems[0:3])
                quantity = listOfItems[-1]
                viewItemString = "({0}) {1} ({2})".format(trackingNumber, parsedItems, quantity)
                # (P003) Grace Garden - Aglaonema - small ornamentals - in good condition (15 pcs)
                print(viewItemString)
            

        
        
     

    if(inp==3):
        print("=== List of items===")
        if (len(dictionary)==0):
            print("No Items")
        else:
            for trackingNumber in dictionary:
                listOfItems = dictionary.get(trackingNumber)
                parsedItems = " - ".join(listOfItems[0:3])
                quantity = listOfItems[-1]
                viewItemString = "({0}) {1} ({2})".format(trackingNumber, parsedItems, quantity)
                print(viewItemString)


    if(inp==4):
        delview=input("Enter Tracking number: ")
        del dictionary[delview]
        print('Item', delview, 'successfully deleted.')
        print(dictionary)

    if (inp == 5):        
        decision =input("Are you sure you want to remove all? Y or y to delete all ").upper()
        if (decision == "Y"):
            dictionary.clear()
            print("Succesfully Deleted")

    if (inp == 6):
        saveToCSVFile()
    if (inp == 7):
        loadCSVFile()

        

    
    if(inp==0):
        print("Thank you for using this program!")
        exit()

    