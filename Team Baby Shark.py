print("Welcome to password generator!")
ans = "y"
while True:
    color = input("Enter your favorite colour : \n")
    job = input("Enter name of job : \n")
    nam = input("Enter the name : \n")
    leng = int(input("Enter the preferable size of the password : \n"))
    password = ''
    name = ''
    job = ''
    color = ''
    for i in range(leng // 3):
        if len(color) != len(col): color += col[i]
        if len(name) != len(nam): name += nam[i]
        if len(number) != len(num): number += num[i]
    password = name.title() + color.title() + number
    if len(password)<leng:
        difference = leng - len(password)
        characters = col + num + nam
        password+=''.join(choice(characters) for x in  range(difference))
    print(password)
    ans = input("Do you want to continue? (y/n)")
    if (ans == "n"):
        print("You exited the program succesfully!")