log_file = open("src/Homework/intro-to-ubermelon/um-server-01.txt")
#initializing log_file to include text found in um-server-01.txt


# def generate_sales_reports(log_file):
#     #defining a function which takes log_file as a param
#     for line in log_file:
#     #for statement looping line in log_file
#         line = line.rstrip()
#         #setting line to equal the remainder of line.restrip()
#         day = line[0:3]
#         #day = to chars from 0-3
#         if day == "Tue":
#             #if day = TUE, print the line
#             print(line)




#Changing to display Monday
def generate_sales_reports(log_file):
    #defining a function which takes log_file as a param
    for line in log_file:
    #for statement looping line in log_file
        line = line.rstrip()
        #setting line to equal the remainder of line.restrip()
        day = line[0:3]
        #day = to chars from 0-3
        if day == "Mon":
            #if day = Mon, print the line
            print(line)
            
generate_sales_reports(log_file)