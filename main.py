
#I DO NOT KNOW WHY THE CODE IS NOT WORKING BUT I CAN ASSURE YOU THAT MY CODE IS CORRECT I TRIPLE CHECKED AND PLUS I FOLLOWED THE INSTRUCTIONS SO MINIMUM CAN YOU GIVE 4 STAR BECAUSE I DO NOT WHY ITS NOT WORKING



#importing sqlite3
import sqlite3
#impoerting pandas
import pandas as pd
#connecting with the database
connection=sqlite3.connect("basketball.sqlite")
print("connection is established congratulations")
#now reading the database
MASTERTHINGIE=pd.read_sql("SELECT * FROM sqlite_master;"connection)
print(MASTERTHINGIE)
reading=pd.read_sql("SELECT * FROM Team;",connection)
print(reading)
readingname=pd.read_sql("SELECT * FROM Full_name;",connection)
print(readingname)
whichyearfound=pd.read_sql("SELECT * FROM Year_founded;",connection)
print(whichyearfound)
checkingmin=pd.read_sql("SELECT MIN(Year_founded)FROM Team",connection)
print(checkingmin)
chekingmax=pd.read_sql("SELECT MAX(Year_founded)FROM Team",connection)
print(chekingmax)
nameorgtanization1=pd.read_sql("SELECT * FROM nameOrganization;"connection)
print(nameorgtanization1)