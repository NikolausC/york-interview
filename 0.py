# a set is a group of biomaterials and their status (whether they're
# available for use)
set_medium = {1: True, 32: False, 6: True, 3: True, 19: False, 19: True}
set_small = {6: true, 11: true, 1: true}

class WorkOrder:
    def _init(self, name, set):
        self.name = name
        self.set = set
        # Status can only be New, Pending, Complete or Cancelled
        self.status = "New"

    def check_material_availability(set):
    numberOfMaterials = len(set)
    material_ids = list(set.keys())

    for i in range(0, len(set)):
        if set[material_ids[i]] == False:
            return False

# Create some work orders
work_order_1 = WorkOrder("Full Genome Sequencing", set_medium)
work_order_2 = WorkOrder("Biomaterial Formatting", set_small)

# Check availability of materials for those work orders:
if work_order_1.check_material_availability(set_medium) = True:
    print("Work Order 1 materials are available!")
else:
    print("Work Order 1 materials un-available.")

if work_order_2.check_material_availability(set_small) = True
    print("Work Order 2 materials are available!")
else
    print("Work Order 2 materials un-available.")
