from dataclasses import dataclass

@dataclass
class MyClass:
    param1: str
    param2: int

    def method1(self) -> None:
        # Define a method for your class
        pass

    def method2(self) -> None:
        # Another method
        pass

def main() -> None:
    # Instantiate an object of MyClass
    obj = MyClass(param1="Hello", param2=42)

    # Call methods on the object
    obj.method1()
    obj.method2()

if __name__ == "__main__":
    # This block of code will be executed when the script is run,
    # but not when it's imported as a module in another script.
    main()
