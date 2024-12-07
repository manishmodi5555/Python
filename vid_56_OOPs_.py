class person:
    name="manish"
    age=20
    profession="accountant"
    def add(self):
        print(f"{self.name} is a {self.profession}")# self refers to the current object of the class
print(person.name)
a=person()
print(a.age)
person.add(a)  # we can  also call using class name and passing obj as argumnets
a.age=30
print(a.age)
a.add()
