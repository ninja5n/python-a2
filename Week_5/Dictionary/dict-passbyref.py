from typing import Dict


# pass by reference == mutable


def greet(dictonary: Dict[str, int]) -> None:
    k = input("Enter key = ")
    v = int(input("Enter value = "))
    dictonary[k] = v


my_dict = {"ninad": 100, "anirudh": 20}
print(my_dict)
greet(my_dict)
print(my_dict)
