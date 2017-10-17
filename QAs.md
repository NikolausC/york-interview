# Zero
- Syntax errors:
  - _init should be __init__
  - Same key appears twice in set_medium dictionary
  - Lower case boolean used in set_small
  - Single equals used as comparator
  - Incorrect indentation for check_material_availability
  - Second if statement missing colons
  - 'self' isn't passed into check_material_availability
- Same key appears twice in set_medium

# One
- What will the outputs be? What would happen if all the materials are available?
  - Both un-available, even though WO2 materials are all available.
  - Why is this?
    - check_material_availability returns None, as it's only returning False if a material is un-available. Must be made to return true.

- What is bad about this code? What would you improve?
  - Sets dictionaries hold state, this should be handled by a Set class, to prevent duplication of data and data inconsistency
  - Work Order status use an enum instead of a string
  - set_id doesn't need passing into check_material_availability, as it's available as self.set_id
  - Inconsistent variable cases: set_id and numberOfMaterials
  - numberOfMaterials not used
  - Loop through materials dictionary should be "for id in materials", much shorter
  - Create a Set class, Materials class
  - Program code should be in a main function

# Two
- How would you improve this further?
  - Create a Material class

- Anything else wrong with it?
  - 'set' shadows the python function set

- How would you test this code?
