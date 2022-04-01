log_file = open("um-server-01.txt")
#this line is opening a file so that python can use the data in the file

def sales_reports(log_file):
#this is a function, sales_reports acts as the name and log_file acts as the parameter
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)
#this is a for loop that is saying for every line in the log file, it wants to .rstrip the white space. it also wants to only print the lines with Monday in it so it it makes day = line[0:3] and says that if that day is equal to "Mon" it will print that line. Otherwise, it wont print that line


sales_reports(log_file)
#this is the function we defined in the last line invoked with log_file as the parameter
