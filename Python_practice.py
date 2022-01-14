temperature=int(input("What is the temperature outside?"))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")


my_votes = int(input("How many votes did you get in the election"))
total_votes = int(input("What is the toal votes in the election?"))
print(f"I received {my_votes/total_votes * 100}% of the total votes.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")
    
