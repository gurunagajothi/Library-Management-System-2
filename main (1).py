class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  


class Stack:
    def __init__(self):
        self.top = None 

    def push(self, value):
        newNode = Node(value)
        if self.top is None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        print(f'"{value}" added to stack.')

    def pop(self):
        if self.top is None:
            print("Stack is Empty!!! Cannot pop.")
        else:
            temp = self.top
            self.top = self.top.next
            print(f'"{temp.data}" removed from stack.')
            del temp

    def display(self):
        if self.top is None:
            print("Stack is Empty!!!")
        else:
            temp = self.top
            print("Stack elements:")
            while temp:
                print(f"{temp.data} --> ", end="")
                temp = temp.next
            print("NULL")


if __name__ == "__main__":
    stack = Stack()

    while True:
        print("\n***** STACK MENU *****")
        print("1. Push (Add Book)")
        print("2. Pop (Remove Book)")
        print("3. Display Stack")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            book = input("Enter book title to add: ")
            stack.push(book)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.display()
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")