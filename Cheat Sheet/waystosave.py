# Assuming you already have a 'df' that you've been working with, here are the following ways to save the df...

# As a CSV:

df.to_csv('modified.csv')

# But this will save with an extra column for the indices. If you don't want this, run the following command: 

df.to_csv('modified.csv', index = False)

# For Excel files...

df.to_excel('modified.xlsx', index = False)

# For TXT files...

df.to_csv('modified.csv', index = False, sep = '\t') # where the '\t' indicates the seperation of a space, i.e. what you'd want in a TXT file.
