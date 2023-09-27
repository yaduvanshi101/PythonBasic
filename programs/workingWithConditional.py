userReply = input("Do you need to ship a package? (Enter yes or no) ")
if userReply == "yes":
    print("we can help you ship that package")
else:
        print("Please come back when you need to ship a package. Thank you.")
        
        
        
        
        
userRply= input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userRply =="stamp":
    print("We have many stamp designs to choose from.")
elif userRply=="envelope":
    print("We have envelope design to choose from.")
elif userRply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.". format(copies))
else:
    print("Thank you, please come again.")
    
    