
class BookStore:
    NoOfBooks = 0

    def __init__(self,Book,Auth):
         self.Name = Book
         self.Author = Auth
         BookStore.NoOfBooks +=1
    def Display(self):
        print(f"{self.Name} by {self.Author}.No of Books: {BookStore.NoOfBooks}")    


def main():
    obj1 = BookStore("Linux system programming","Robert Love")
    obj1.Display()

    obj1 = BookStore("C programming","Dennis Ritchie")
    obj1.Display()
if __name__ == "__main__":
    main()