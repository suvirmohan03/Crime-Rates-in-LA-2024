import pandas as p
import matplotlib.pyplot as plt

data = p.read_csv("data.csv")

communities = ["Wilshire", "Central", "Southwest", "Van Nuys", "Hollywood","Southeast", "Mission", "Newton", "Westvalley", "Olympic", "Hollenback", "Northeast", "WestLA", "nHollywood", "Rampart", "77 Street", "Devonshire", "Harbor", "Foothill","Pacific"]
list_of_areas = list(data["AREA NAME"])

amount = [ 
          list_of_areas.count('Wilshire'), 
          list_of_areas.count('Central'), 
          list_of_areas.count('Southwest'), 
          list_of_areas.count('Van Nuys'), 
          list_of_areas.count('Hollywood'), 
          list_of_areas.count('Southeast'), 
          list_of_areas.count('Mission'), 
          list_of_areas.count('Newton'), 
          list_of_areas.count('West Valley'), 
          list_of_areas.count('Olympic'), 
          list_of_areas.count('Hollenbeck'), 
          list_of_areas.count('Northeast'), 
          list_of_areas.count('West LA'), 
          list_of_areas.count('N Hollywood'), 
          list_of_areas.count('Rampart'), 
          list_of_areas.count('77th Street'), 
          list_of_areas.count('Devonshire'),
          list_of_areas.count('Harbor'),
          list_of_areas.count('Foothill'),
          list_of_areas.count('Pacific')]
gender = ["Men", "Women", "Unknown"]
list_of_genders = list(data["Vict Sex"])
amount1 = [
              list_of_genders.count("M"),
              list_of_genders.count("F"),
              list_of_genders.count("X")]

ethnicity = ["White", "Black", "Other Asian", "Hispanic", "Other", "Unknown"]
list_of_ethnicities = list(data["Vict Descent"])
amount2 = [
              list_of_ethnicities.count("W"),
              list_of_ethnicities.count("B"),
              list_of_ethnicities.count("A"),
              list_of_ethnicities.count("H"),
              list_of_ethnicities.count("O"),
              list_of_ethnicities.count("X")

]

fig, axs = plt.subplots(1, 3, figsize = (20,10))
axs[0].pie(amount, labels = communities, autopct="%1.1f%%")
axs[0].set_title('Crime rates in different areas in LA (2020-Present)')

axs[1].pie(amount2,labels = ethnicity, autopct="%1.1f%%")
axs[1].set_title('Crime rates in different areas in LA based on ethnicity')

axs[2].bar(gender,amount1, color=["blue", "pink", "grey"])
axs[2].set_title("Crime rates based on Gender in LA areas")
axs[2].xlabel = ("Gender")
axs[2].ylabel = ("Crime rate")



plt.tight_layout()
plt.show()

Wilshire = 0
Central = 0
Southwest = 0 
Vannuys = 0
Hollywood = 0
Southeast = 0
Mission = 0
Newton = 0
Westvalley = 0
Olympic = 0
Topango = 0
Hollenback = 0
Northeast = 0
WestLA = 0
nHollywood = 0
Rampart = 0
seven_seven_street = 0
Devonshire = 0
M= 0
F = 0
THEFT_OF_IDENTITY = 0
STOLEN = 0
CHILD = 0
THEFT = 0
ASSAULT = 0
G_THEFT = 0
ROB = 0
T  = 0

#CRIME COUNT
la =  len(data["Crm Cd Desc"])
for index, row in data.iterrows():
    if row['Crm Cd Desc'] == "THEFT OF IDENTITY":
        THEFT_OF_IDENTITY += 1 
    if "STOLEN" in row['Crm Cd Desc']:
        STOLEN += 1 
    if "ASSAULT" in row['Crm Cd Desc']:
        ASSAULT += 1 
    if "CHILD" in row['Crm Cd Desc']:
        CHILD += 1 
    if "THEFT" in row['Crm Cd Desc'] and row['Crm Cd Desc'] != "THEFT OF IDENTITY" and row['Crm Cd Desc'] != "GRAND  THEFT":
        THEFT += 1 
    if "GRAND THEFT" in row['Crm Cd Desc']:
        G_THEFT += 1
    if "ROBBERY" in row['Crm Cd Desc']:
        ROB += 1
    if "TRESPASSING" in row['Crm Cd Desc']:
        T += 1


#GENDER COUNT
user_input = input("Are you a M , F  or other: ")

gender =  len(data["Vict Sex"])
for index, row in data.iterrows():
    if row['Vict Sex'] == "M":
        M += 1 
    if row['Vict Sex'] == "F":
        F += 1 

if user_input == "M"  or user_input ==  "M".lower():
    print("You are more likely to commit a crime.")
if user_input != "M" and user_input != "M".lower():
        print("You are less  likely to commit  a  crime.")

intro = "IN LA"
print(f"{M} males commited crimes.")
print(f"{F} females commited crimes.")

user_input2 =  input("Do  you want to know the crime rates in LA? Y OR N: ")


if user_input2 == "Y" or user_input2 ==  "Y".lower():
    print(f"{intro} there were {THEFT} thefts.")
    print(f"{intro} there were {STOLEN} stolen auto mobile or belongings.")
    print(f"{intro} there were {ASSAULT}  assault crimes.")
    print(f"{intro} there were {CHILD}  crimes against children.")
    print(f"{intro} there were {G_THEFT} grand theft crimes.")
    print(f"{intro} there were {THEFT_OF_IDENTITY} identity theft crimes.")
    print(f"{intro} there were {ROB} roberies.")
    print(f"{intro} there were {T} trespassing crimes.")
elif user_input2 != "Y"  and user_input2 != "Y".lower():
        print("damn")



user_input3 = input("Do you want to  see their ethnicitys? Y OR N: ")

B = 0
H  = 0
O = 0
W = 0

descent =  len(data["Vict Descent"])
for index, row in data.iterrows():
    if row['Vict Descent'] == "W":
        W += 1 
    if row['Vict Descent']== "B":
        B += 1 
    if row['Vict Descent'] == "H":
        H += 1 
else:
    O +=1


        

if user_input3 == "Y" or user_input3 == "Y".lower():
    print(f"{W} criminals were white")
    print(f"{H} criminals were hispanic")
    print(f"{B} criminals were black")
    print(f"{O} criminals were unkown")
elif user_input3 != "Y"  and  user_input3 !=  "Y".lower():
    print("damn")
        

user_input4 =  input("What is your ethnical background?(W, B, O, H): ")

if user_input4 == "W" or user_input4 == "W".lower():
    print("COOL")
elif user_input4 == "H" or  user_input4 == "H".lower():
    print("COOL")
elif user_input4 == "B" or user_input4 == "B".lower():
    print("COOL")
elif user_input4 == "O" or user_input4 == "O".lower():
    print("COOL")
else:
    print("COOL")


















