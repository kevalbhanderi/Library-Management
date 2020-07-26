# ------- LIBRARY MANAGEMENT SYSTEM ------

class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.landDict = {}

    def displaybook(self):
        print(f"We have following books in our Library:{self.name}")
        for book in self.booklist:
            print(book)

    def landbook(self, user, book):
        if book not in self.landDict.keys():
            self.landDict.update({book:user})
            print("Book database has been update. You can take the book now")
        else:
            print(f"This Book is already being used by {self.landDict[book]}")

    def addbook(self, book):
        self.booklist.append(book)
        print("Book has been added to the booklist")

    def returnbook(self, book):
        self.landDict.pop(book)

if __name__ == '__main__':
    keval = Library(["Python", "Devil's Bible", "Algorithms by CLRS", "The Orphan's story"],
                    "Media Center")

    while(True):
        print(f"Welcome to the {keval.name} library. Enter your choice to continue")
        print("1.displaybooks")
        print("2.land a book")
        print("3.add a book")
        print("4.return a book")

        user_input = input()
        if user_input not in ['1','2','3','4']:
            print("Enter a valid option")
            continue

        else:
            user_input = int(user_input)

        if user_input == 1:
            keval.displaybook()

        elif user_input == 2:
            book = input("Enter name of the book:")
            user = input("Enter your name:")
            keval.landbook(user, book)

        elif user_input == 3:
            book = input("Enter the name of the book you want to add:")
            keval.addbook(book)

        elif user_input == 4:
            book = input("Enter the name of the book you want to return:")
            keval.returnbook(book)

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")
        user_input2 = ""
        while(user_input2 != "q" and user_input2 != "c"):

            user_input2 = input()
            if user_input2 == "q":
                exit()
            elif user_input2 == "c":
                continue
