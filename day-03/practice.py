#Lecturer-led 
from datetime import date

name= input ("Please enter your name: ")
year_born= input ("Please the year you were born: ")
#age= 2026- int(year_born)

today= date.today()
age = today.year - int(year_born)

#input (name, "Age is",age)
print(name, "Age is",age)