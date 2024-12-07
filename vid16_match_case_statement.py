


day = input("Enter any day name between Monday to Sunday: ").capitalize()

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("It's a weekday, buddy!")

    case "Saturday" | "Sunday":
        print("It's an off day, buddy!")

    case _:
        print("Invalid input. Please enter a valid day name.")
# we can also use if else in case like
# case _ if x=90:
#print(""njxn)