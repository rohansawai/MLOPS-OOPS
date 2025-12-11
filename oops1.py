class employee:
    def __init__(self):
        print("Started")
        self.id = 123
        self.salary = 5000000
        self.designation = "SDE"
        print("Initiated")


    def travel(self, destination):
        print("This was called manually")
        print(f"Employee is now traveling to {destination}")

sam = employee()

print(sam.id)
sam.travel("Mumbai")