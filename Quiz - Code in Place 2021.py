
print("Hey Coders_in_Place!")

answer = input("Are you ready to test your knowledge? (yes/no) ")
score = 0


if answer.lower() == 'yes':
    answer = input("1. Well, hope you answer it correctly… You love it or hate it. ____, the robot:\n")
    if answer.lower() == "karel":
        score += 1
        print("Amazing. Great job!!! \n")
    else:
        print("Ohh no!! I personally liked Karel!")

    answer = input("2. The best discussion group ever:\n")
    if answer.lower() == "ed":
        score += 1
        print("I thank you for being part of this great group\n")
    else:
        print("Ohh no!!! Ed, Ed, Ed...")

    answer = input("3. Programming language you’ve learned in Code in Place course:\n")
    if answer.lower() == "python":
        score += 1
        print("Yep, you've learned a lot :) \n")
    else:
        print("Incorrect! We've learned Python!!!")

    answer = input("4. Sure, you remember this… Chris’ dog’s name:\n")
    if answer.lower() == "simba":
        score += 1
        print("Amazing. He's cute, isn't he? \n")
    else:
        print("Nooooooo!! It's Simba!")

    answer = input("5. Surely, you watched the lectures :D A lecturer’s name (“M” is his name’s first letter):\n")
    if answer.lower() == "mehran":
        score += 1
        print("haha great! Mehran and his lightsabers!!!!!!!\n")
    else:
        print("Ohh no!!!")

    answer = input("6. T-shirt design contest winner (First name):\n")
    if answer.lower() == "meeka":
        score += 1
        print("Congratutations, Meeka! Amazing design!\n")
    else:
        print("Come onnnn!!! Please go back to Ed and have a look at it!!\n ")

    answer = str(input("7. Number of sections we should have attended:\n"))
    if answer.lower() == "5":
        score += 1
        print("yessss, hope you enjoyed like I did!\n")
    else:
        print("Incorrect! We should have attended 5!\n ")

    answer = input("8. Explained the lectures about files (First name):\n")
    if answer.lower() == "brahm":
        score += 1
        print("Correct! An amazing lecture! \n")
    else:
        print("Ohh no!! Don't worry, you still have time to watch them!\n ")

    print("You got " + str(score) + " question(s) correct!\n")

    print("You got " + str((score / 8) * 100) + "%.")


    print("THANK YOU, Code in Place staff and Ed discussion group! "
              "I definitely loved to be part of this amazing learning progress")










