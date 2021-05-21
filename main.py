stopper =True
dictionary = { }

n=1
while(stopper):
    inp = int(input("[1] add item \n[2]View an Item \n[3]View all Items \n[4]Delete all an item"
                    " \n[5]Delete all items\n [6]save to file\n[7]Load from Files \n[0] Exit \n"))
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
        
        trackingNumber = input("Enter Tracking number:")
        listOfItems = dictionary.get(trackingNumber)
        parsedItems = " - ".join(listOfItems[0:3])
        quantity = listOfItems[-1]
        viewItemString = "({0}) {1} ({2})".format(trackingNumber, parsedItems, quantity)
        # (P003) Grace Garden - Aglaonema - small ornamentals - in good condition (15 pcs)
        print(viewItemString)
        
     

    if(inp==3):
        print()


    if(inp==4):
        delview=input("Enter Tracking number: ")
        del dictionary[delview]
        print('Item',delview,'successfully deleted.')
        print(dictionary)

    if(inp==5):
        print()