import csv

username = input("Please create a username: ")
passwort = input("Please choose a passwort: ")

keep_running = True
asking_again = True

while asking_again:
    age = input("What is your age? ")

    try:
        age = int(age)
        asking_again = False

        if age < 18:
            print("Sorry, you are under 18.")
            keep_running = False

    except ValueError:
        print("You are too stupid to type your age, congratulations, please try again")


while keep_running:
    print("Cool, you are older than 18!")
    print("Here are all numbers from 1 to 999 for you")

    numbers_list = []
    for each_number in range(1, 1000, 1):
        numbers_list.append(each_number)
    print(numbers_list)

    file_name = "output/output_csv.csv"

    file_handle = open(file_name, 'w')
    file_writer = csv.writer(file_handle, lineterminator="\n")

    list_of_numbers = []
    for number in range(1, 100, 1):
        if number % 5 == 0:
            list_of_numbers.append([number])

    file_writer.writerows(list_of_numbers)

    asking = True

    while asking:
        print("Log in")
        username_asking = input("Username: ")
        passwort_asking = input("Passwort: ")

        if username_asking == username and passwort_asking == passwort:
            print("Username and passwort are correct")
            asking = False
        else:
            print("Username or passwort is incorrect.")

    print("You can now enter a random text and save it to a new file:")
    input_text = input("enter text: ")
    file_name = input("file name: ")

    file_path = "output/" + file_name + ".csv"

    file_handle_2 = open(file_path, 'w', newline='')
    file_writer_2 = csv.writer(file_handle_2)

    file_writer_2.writerow([input_text])

    keep_running = False





