# Create a graph of the number of friends (y-axis) and the friends (x-axis) themselves
# Sorted by number of friends (y-axis)
# Include the user in the graph (count the number of their friends) and label as U
x = []
y = []
count = []

counter = 1
for axis in myfriends:
  x.append('f'+ str (counter))
  y.append(axis[1])
  count.append(counter)
  counter = counter + 1
  
# Sort the nuber of friends for (y-axis)
y.sort()

# Include the user in the plots for the graph
x.append('U')
y.append(len(myfriends))
count.append(len(y)+1)
# set the image size of the graph
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(25, 10.5)
fig.savefig('./sample_data/friend_paradox_graph.png', dpi=100)

# plotting a bar chart 
#plt.scatter(x, y, label='friends', color='blue',
#        marker='*', s=30) 

plt.bar(count, y, tick_label = x, align='center',
        width = 0.95, color = ['blue', 'red']) 

# naming the x axis
plt.xlabel('friends')
# naming the y axis
plt.ylabel('number of friends')

# giving a title to my graph
plt.title('Friend Paradox Graph')

# function to show the plot
plt.show()