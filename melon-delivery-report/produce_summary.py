def melon_count_amount(day, filename): #def the function that takes filename as an argument
    print("Day", day)
    for line in open(filename): #setting a for loop to loop over each line in the opened file
        
        line = line.rstrip() #removing all the whitespace from the document line
        words = line.split('|') #splitting the words by |
        
        
        melon_type = words[0] #variable initilized to hold the melon type found in words[0]
        melon_count = words[1] #variable initilized to hold the melon count found in words[1]
        melon_amount = words[2] #variable initilized to hold the melon cost found in words[2]
        print(f"Delivered {melon_count} {melon_type}s for total of ${melon_amount}")
        
melon_count_amount(1, "um-deliveries-day-1.txt")
melon_count_amount(2, "um-deliveries-day-2.txt")
melon_count_amount(3, "um-deliveries-day-3.txt")