counties = ["Arapahoe","Denver","Jefferson"]
if counties[1]=="Denver":
    print(counties[1])



temperature = int(input("What is the temperature outside?"))

if temperature > 80:
    print("Turn on the AC.")

else:
    print("Open the window.")


#What is the score?
score = int(input("What is your test score? "))

#Determine the grade.

if score >= 90:
    print("Your grade is an A.")
elif score >= 80:
    print("Your grade is a B.")
elif score >= 70:
    print("Your grade is a C.")
elif score >= 60:
    print("Your grade is a D")
else:
    print("Your grade is an F.")


#x=0
#while x <= 5:
#    print(x)
#    x = x + 1
#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county in counties_dict:
#    print(county)
#type(county)
#print(county)
#for voters in counties_dict.values():
#    print(voters)
#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict['registered_voters'])



counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")


voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county_data in voting_data:
    print(f"{county_data['county']} county has {county_data['registered_voters']:,} registered voters.")


import datetime
now = datetime.datetime.now()
print("The time right now is ",now)
