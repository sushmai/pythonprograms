def main():
    print("Contacts Manager:")
    

    #initialize friends list
    friends = []
    infile = open("contacts.txt", "r")
    line = infile.readline()
    while line:
        friends.append(line.rstrip("\n").split(","))
        line = infile.readline()
    infile.close()

    choice = 0
    while choice != 4:
        print("1 Add a friend:")
        print("2 Lookup contacts")
        print("3 display all contacts")
        print("4 Quiit" )

        choice = eval(input())

        if choice == 1:
            print("Adding a friend")
            name = input("Enter a name:")
            email = input("enter email:")
            phone = input("enter phone:")
            friends.append([name, email, phone])
            
        elif choice == 2:
            print("Look up a friend ")
            keyword = input("Enter name to search: ")
            for friend in friends:
                if keyword in friend:
                    print(friend)
            
        elif choice == 3:
            print("Displaying all contacts")
            for i in range(len(friends)):
                print(friends[i])
        elif choice == 4:
            print("End the program")
        else:
            print("Invalid response..")
    outfile = open("contacts.txt", "w")
    for friend in friends:
        outfile.write(",".join(friend) + "\n")
    outfile.close()
        
        
main()








