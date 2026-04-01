class Voter:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def validate_age(self):
        try:
            if self.age < 18:
                raise ValueError("You are not eligible to vote")
        except ValueError as e:
            print(e)
        else:
            print("You are eligible to vote")
            print("Name : ", self.name)
            print("Age : ", self.age)

            


v = Voter("abhi", 20)
v.validate_age()

v1 = Voter("abhi", 17)
v1.validate_age()