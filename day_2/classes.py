# Class for character
class Password(object):
    def __init__(self, min_length=None, max_length=None, required_symbol=None, password=None):
        self.min_length = min_length
        self.max_length = max_length
        self.required_symbol = required_symbol
        self.password = password

    def __str__(self):
        return "Password \"" + self.password + "\" should contain \"" + self.required_symbol + "\" between " + str(self.min_length) + " to " + str(self.max_length) + " times."

    def import_match(self, matched_line):
        self.min_length = int(matched_line[0])
        self.max_length = int(matched_line[1])
        self.required_symbol = matched_line[2]
        self.password = matched_line[3]
