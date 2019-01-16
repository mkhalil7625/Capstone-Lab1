from dataclasses import dataclass

@dataclass
class Student:
    name:str
    college_id: int
    gpa:float

def main():
    alice= Student('Alice', 123456, 3.5)
    bob = Student('Bob',9765, 3.25)

    print(alice)
    print(bob)

main()