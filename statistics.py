def print_statistics(mynums):
  # Compute the Mean of number of friends that the user's friends have
  print("Mean: %d" % statistics.mean(mynums))

  # Compute the standard deviation
  print("Standard Deviation: %d" % statistics.stdev(mynums))

  # Compute the Median of number of friends that the user's friends have
  print("Median: %d" % statistics.median(mynums))