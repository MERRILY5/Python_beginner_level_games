name1 = input("Enter name one: ").lower().replace(" ","")
name2 = input("Enter name two: ").lower().replace(" ","")

flames  = ["Friend", "Lover", "Affection", "Life partner", "Enemy", "Sibilings"]

for i in name1:
    if i in name2:
        name1 = name1.replace(i,"",1)
        name2 = name2.replace(i,"",1)
 
new_name = name1+name2     
        
length = len(new_name)

if length == 0:
    print("Both the names are matching")

while(len(flames) > 1):
   index = (length %len(flames)-1)
   if index >= 0:
       right = flames[index + 1:]
       left = flames[:index]
       flames = right + left
   else:
       flames = flames[:len(flames)-1]
       
print(f"You and your {flames[0]} will be together") 
    