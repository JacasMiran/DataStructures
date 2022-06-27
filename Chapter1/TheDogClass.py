class Dog:
# This is the constructor for the class. It is called whenever
# object is created. The reference called "self" is created by
# and made to point to the space for the newly created object.
# does this automatically for us but we have to have "self" as
# parameter to the __init__ method (i.e. the constructor).
    def __init__(self, name, month, day, year, speakText):
    self.name = name
    self.month = month
    self.day = day
    self.year = year
    self.speakText = speakText
    # This is an accessor method that returns the speakText stored in the
    # object. Notice that "self" is a parameter. Every method has "self" as its
    # first parameter. The "self" parameter is a reference to the current
    # object. The current object appears on the left hand side of the dot (i.e.
    # the .) when the method is called.
    def speak(self):
        return self.speakText
    def getName(self):
        return self.name
    