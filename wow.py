class Person: 
    def __init__(self, name) -> None:
        self.left_child = None
        self.right_child = None


        self.children = [Person("child 1")] 

        self.name = name 

    def set_left_child(self, x):
        self.left_child = x
    
    def set_right_child(self, x): 
        self.right_child = x
    
    def set_name(self, x): 
        self.name = x

    def get_left_child(self):
        return self.left_child

    def print(self):
        print(self.name)
        print(self.left_child)
        print(self.right_child)
        print("====================")


if __name__ == "__main__":
    james = Person("James")

    x = "james"

    # print(james.print())

    james_2nd = Person("James the 2nd")
    james.set_left_child(james_2nd)

    james.print()
    james_3rd = Person("James the 3rd")
    james_2nd.set_left_child(james_3rd)
    james.get_left_child().print()
    james.get_left_child().get_left_child().print()
    


    

