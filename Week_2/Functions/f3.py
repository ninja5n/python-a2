# with parameters, without return


def greet(name: str, age: int, gender: str = None):  # type: ignore
    print(f"My Name is = {name}")
    print(f"My Age is = {age}")
    print(f"My Gender is = {gender}")


# greet("Ninad", 55, "Male")
greet("Ninad", 44)
