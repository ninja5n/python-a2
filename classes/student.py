class Student:
    """Create an object called student with various attributes and features."""

    def __init__(
        self, roll_no: int, name: str, gender: str, age: float, phone_number: int
    ) -> None:
        self.roll_no = roll_no
        self.name = name
        self.gender = gender
        self.age = age
        self.phone_number = phone_number

    def updateName(self) -> None:
        self.name = input("Enter new name: ")

    def updatePhoneNumber(self, new_number=0) -> None:
        self.phone_number = new_number

    def display(self) -> None:
        """Display all the info related to a Student"""
        print(f"\nRoll no = {self.roll_no}")
        print(f"Name = {self.name}")
        print(f"Gender = {self.gender}")
        print(f"Age = {self.age}")
        print(f"Phone Number = {self.phone_number}\n")


s1 = Student(
    roll_no=100, name="JAMES", gender="Male", age=30, phone_number=2242123245512
)
s2 = Student(10, "Nick", "Male", 330, 2212)
s3 = Student(name="Nick", age=330, phone_number=2212, gender="Male", roll_no=2)
s1.display()
s2.display()
s3.display()
