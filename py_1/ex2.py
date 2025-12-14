class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1

    def age_one_day(self):
        self.age += 1

    def get_info(self):
        print(
            self.name,
            ": ",
            self.height,
            "cm, ",
            self.age,
            " days old",
            sep=""
        )



rose = Plant("Rose", 25, 30)

start_height = rose.height

print("=== Day 1 ===")
rose.get_info()

day = 1
while day < 7:
    rose.grow()
    rose.age_one_day()
    day += 1

print("=== Day 7 ===")
rose.get_info()

growth = rose.height - start_height
print("Growth this week: +", growth, "cm", sep="")
