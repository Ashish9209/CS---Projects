class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_numberOfStudents(self):
    return self.numberOfStudents

  def set_numberOfStudents(self, changed_number):
    self.numberOfStudents = changed_number

  def __repr__(self):
    return ("A {level} school named {name} with {numberOfStudents} students.").format(level=self.level, name=self.name, numberOfStudents=self.numberOfStudents)

ttic = School("TTIC", 'Middle', 150)
print(ttic)

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def get_pickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    parent_repr = super().__repr__()
    return parent_repr + "The pickup policy is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)

rsbv = PrimarySchool("RSBV", 100, "pickup after 3pm")
print(rsbv)


class HighSchool(School):
  def __init__(self, name, numberOfStudents, *sportsTeams):
    super().__init__(name, "HighSchool", numberOfStudents)
    self.sportsTeams = sportsTeams

  def get_sportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    parent_repr = super().__repr__()
    return parent_repr + "The sports Team is {sportsTeams}".format(sportsTeams = self.sportsTeams)

rskv = HighSchool("RSKV", 115, 'cricket', 'football', 'vollyball')
print(rskv)
