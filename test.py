
import file_to_import
from file_to_import import foo

def main():
    print("Hello World")
    print("This file __name__ is : {}".format(__name__))

if __name__ == "__main__":
    main()
    file_to_import.foo()
    foo()
    
    name = "default user"
    name = input("What is your name, " + name + " ? ")
    name = name.strip()     # Trim "name" string
    print ("Welcome {}".format(name))