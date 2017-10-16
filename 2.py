from enum import Enum

class Set:
    def __init__(self, input_set):
        self.data = {}
        for id in input_set:
            self.data[id] = input_set[id]

    def all_available(self):
        return all(self.data.values())

class WOStatus(Enum):
    New, Pending, Complete, Cancelled = range(4)

class WorkOrder:
    def __init__(self, name, set):
        self.name = name
        self.set = set
        self.status = WOStatus.New

    def check_material_availability(self):
        return self.set.all_available()

def main():
    set_1 = Set({1: True, 32: False, 6: True, 3: True, 19: True})
    set_2 = Set({6: True, 11: True, 1: True})

    # Create some work orders
    work_order_1 = WorkOrder("Full Genome Sequencing", set_1)
    work_order_2 = WorkOrder("Biomaterial Formatting", set_2)

    # Check availability of materials for those work orders:
    if work_order_1.check_material_availability() == True:
        print("Work Order 1 materials are available!")
    else:
        print("Work Order 1 materials un-available.")

    if work_order_2.check_material_availability() == True:
        print("Work Order 2 materials are available!")
    else:
        print("Work Order 2 materials un-available.")

main()
