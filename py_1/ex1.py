class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


ob1 = Plant("Ma3dnous", 10, 22)
ob2 = Plant("Rose", 25, 47)
ob3 = Plant("Ri7an", 23, 90)
print("=== Garden Plant Registry ===")
print(ob1.name, ": ", ob1.height, "cm, ", ob1.age, " days old", sep="")
print(ob2.name, ": ", ob2.height, "cm, ", ob2.age, " days old", sep="")
print(ob3.name, ": ", ob3.height, "cm, ", ob3.age, " days old", sep="")

