# You can use the below code snippet to drop the column from the pandas dataframe.

df.drop("column_name", axis=1, inplace=True)

# where

# Column_name – Name of the column to be deleted
# axis=1 – Specifies the axis to be deleted. Axis 1 means column and 0 means rows.
# inplace=true specifies the drop operation to be in same dataframe rather creating a copy of the dataframe after drop.

# You can use df.columns[index] to identify the column name in that index position and pass that name to the drop method.
# An index is 0 based. Use 0 to delete the first column and 1 to delete the second column and so on.

df.drop(df.columns[2], axis=1, inplace=True)

# where

# df.columns[2] – specifies third column to be deleted
# axis=1 – specifies the column axis to be deleted
# inplace=True – specifies the drop operation should happen in same dataframe and no copy of the dataframe should be created.

# You can use the column name directly to the drop method.

# If the column is existing then, it’ll be dropped from the dataframe. If the column doesn’t exist, then the error will be raised.
# You can control the error behavior using the errors = ‘ignore’. You’ll see the error handling in detail at a later point in this tutorial.

df.drop("Difficulty_Score", axis=1, inplace=True)

# where

# Difficulty_Score – specifies the name of the column to be deleted
# axis=1 – specifies the column axis to be deleted
# inplace=True – specifies the drop operation should happen in same dataframe and no copy of the dataframe should be created.

# You can use df.columns[index1, index2, indexn] to identify the list of column names in that index positions and pass that list to the drop method.
# An index is 0 based. Use 0 to delete the first column and 1 to delete the second column and so on.

df.drop(df.columns[[1, 2]], axis = 1, inplace = True)

# where

# df.columns[[1, 2]] – specifies multiple column indexes to be deleted.
# axis=1 – specifies the column axis to be deleted
# inplace=True – specifies the drop operation should happen in same dataframe and no copy of the dataframe should be created.

# By default, during the drop operation if the column is not existing in the dataframe, then the error KeyError: "['Difficulty_Score' 'Type'] not found in axis" will be raised.
# To drop column only if exists without raising any error, then you can specify errors='ignore' in the drop method as shown below.

df.drop(["Difficulty_Score", "Type"], axis=1, inplace= True, errors='ignore')

# where

# ["Difficulty_Score", "Type"] – specifies names of columns to be deleted
# axis=1 – specifies the column axis to be deleted
# inplace=True – specifies the drop operation should happen in same dataframe and no copy of the dataframe should be created.
# errors='ignore' – To ignore the error while deleting the non existent columns.

# You can achieve this by using the df.loc function. loc function is used to select rows or columns by using the label name.

# Use 

df.loc[:, :'specific_column'] 

# to create a dataframe with the columns until the specific_column with all the rows.

# where

# First : in the loc function means, to select all the rows from the dataframe.
# :'specific_column' – means select columns from the first column until the specific_column.

# You may want to use this when you want to delete a column with a value that has a specific value so that you can ignore those values in the data analysis.
# You can evaluate the row value by using an IF statement.
# In the IF statement, you can pass the condition which needs to be evaluated.

# For example,

df["Difficulty_Score"] > 7).any() 
# will check if any value of the difficulty_score is greater than 7. If yes, returns True. Else False.

df["Difficulty_Score"] > 7).all() 
# means it’ll check if all values of the difficulty_score is greater than 7. If yes, returns True. Else False.

# Now, to drop the column if it has a value greater than 7, then use the below snippet.

if((df["Difficulty_Score"] > 7).any())

    df.drop("Difficulty_Score" , inplace=True, axis=1)

else:

    print("No row exists with difficulty value greater than 7. Hence this column will NOT be dropped")

# Since the column difficulty_score is greater than 7, it’ll delete the column from the dataframe. If it doesn’t have then the column will not be removed.
# You can achieve this by using the df.iloc function. iloc function is used to select rows or columns by using the index of the columns.
# Use df.iloc[:, 1:3] to select columns from positions 1 to 3. The index is 0 based. Hence it’ll select columns 2 to 4.
# When you use this in the drop method, then column 2 to 4 will be dropped.

df.drop(df.iloc[:, 1:3], inplace = True, axis = 1)

# Source: https://www.stackvidhya.com/drop-column-in-pandas/#:~:text=drop()%20method%20will%20return,column%20that%20is%20being%20deleted.
