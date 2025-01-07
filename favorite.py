import csv

with open('note.csv', 'r') as file:
    
    count = {};
    reader = csv.DictReader(file)
    for row in reader:
        favorite = row["Language"]
        print(favorite);
        if favorite in count:
            count[favorite] += 1;
        else:
            count[favorite] = 1;
print()
for favorite in sorted(count, key=lambda language: count[language], reverse=True):
    print(f"{favorite}= {count[favorite]}", end =" ");

print()