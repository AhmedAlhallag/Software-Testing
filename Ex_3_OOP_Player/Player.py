class Player():

    count = 0

    def __init__(self, fname, lname, speed):
        assert isinstance(speed, int), "This cannot be a string."
        assert isinstance(fname, str) and isinstance(
            lname, str), "Fname and Lname should be strings"
        assert fname and lname and speed, "INVALID INPUTS"
        self.fname = fname
        self.lname = lname
        self.speed = speed
        self.nickname = None
        Player.count += 1
        self.id = Player.count

    def set_nickname(self):
        self.nickname = self.fname[0].capitalize(
        ) + "." + self.lname[0].capitalize() + self.lname[1:]
