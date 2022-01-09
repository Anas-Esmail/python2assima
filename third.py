# Ask the user to enter the names of three people they want toinvite to a party
#  and store them in a list. After they have enteredall three names, ask them if they want to add another.
#   If they do,allow them to add more names until they answer “no”. Whenthey answer “no”, 
#   display how many people they have invited tothe party. and upload file to GitHub and
#    past the link down

users=[]
for x in range(3):
    user=input("enter the person to invite:\t")
    users.append(user)


user2=input("if want to add other choose y")

while (user2 =="y"):
 user=input("enter the person to invite")
 users.append(user)
 user2=input("if want to add other choose y")
 


print(f"you invite {users} thery are {len(users)} invited persons to party")
 