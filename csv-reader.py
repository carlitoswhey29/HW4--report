import csv 
import statistics
import matplotlib
import matplotlib.pyplot as plt 

# file location constant
FRIEND_COUNT_FILE = './sample_data/HW4-friend-count.csv'

# initializing the titles and rows list 
fields = [] 
rows = [] 

# reading csv file 
with open(FRIEND_COUNT_FILE, 'r') as csvfile:
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 

# initializing the list of friends the user has
mynums = []
# myfriends is a collection of tuples
myfriends = []

# make the list of number of friends
for row in rows[:]: 
    mynums.append( int (row[1]))
    myfriends.append((row[0], int (row[1])))