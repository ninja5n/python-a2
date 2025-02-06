class Student:
    """Create an object called student with various attributes and features."""

    def __init__(
        self, roll_no: int, name: str, gender: str, age: float, phone_number: int
    ) -> None:
        """appne aap run hota hai jab 1 object create hota hai"""
        self.roll_no = roll_no
        self.name = name
        self.gender = gender
        self.age = age
        self.phone_number = phone_number

    def __str__(self) -> str:
        """Apne aap run hota hai jab 1 object ko print kiya jata hai"""
        return f"Name: {self.name}, Age: {self.age}."

    def __add__(self, object2):
        return self.age + object2.age

    def __len__(self) -> int:
        return self.phone_number

    def __gt__(self, object2) -> bool:
        return self.age > object2.age

    def __lt__(self, object2) -> bool:
        return self.age < object2.age

    def __ge__(self, object2) -> bool:
        return self.age >= object2.age

    def __le__(self, object2) -> bool:
        return self.age <= object2.age

    def __eq__(self, object2) -> bool:
        return self.age == object2.age

    def updateName(self) -> None:

        return self.age > object2.age
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

# print(s1)
# print(s2)
# print(s3)

# print(s1 + s2)
# print(len(s3))

print(s2 > s3)
