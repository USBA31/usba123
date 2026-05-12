try:
    with open("library.txt", "x") as file:
        print("File successfully created")

except FileExistsError:
    print("File Alregit ady Exists")

except:
    print("An error occured")


def addBook():
    with open("library.txt", "a") as file:
        book = input("Enter book to add: ")
        file.write(book + "\n")
        print("Book added successfully")


addBook()
