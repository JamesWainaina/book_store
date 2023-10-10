def main():
    
    try:
        booklist = []
        infile = open("theBookList", "r")
        line = infile.readline()
        while line:
            booklist.append(line.rstrip("\n").split(","))
            line = infile.readline()

        infile.close() 
    except FileNotFoundError:
        print("the <booklist.txt> file is not found")
        print("starting a new book list")
        booklist = []

    choice = 0
    while choice !=4:
        print("*** Books manager ***")
        print("1) Add a book")
        print("2) lookup a book")
        print("3) Display books")
        print("4) Quit")
        choice= int(input())
        
        if choice == 1:
            print("Adding a book..")
            nbook= input("Enter the name of the book >>>")
            nAuthor= input("Enter the Author of the book >>>") 
            nPages= input("Enter the number of pages >>>")  
            booklist.append([nbook, nAuthor, nPages])
            
        elif choice == 2:
            print("looking up for a book...")
            keyword= input("Enter search Term: ")
            for book in booklist:
                if keyword in book:
                    print(book)                                  
        elif choice == 3:
            print("Display all books...")
            for i in range(len(booklist)):
                print(booklist[i])
        elif choice == 4:
            print("Quitting Program")
    print("Program terminated!")


    #saving to externaal txt file

    outfile = open("theBookList.txt", "w")
    for book in booklist:
        outfile.write(",".join(book) + "\n")


if __name__=="__main__":
    main()