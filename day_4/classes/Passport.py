import re

from day_4.classes.Data import is_in_range, is_accepted, xstr
from day_4.classes.Year import check_year
from day_4.exceptions.InvalidValue import InvalidValue
from day_4.exceptions.MissingRequiredValue import MissingRequiredValue

PASSPORT_ID_PATTERN = "^[0-9]{9}$"

ACCEPTED_EYE_COLOURS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

HAIR_COLOUR_PATTERN = "#[0-9|a-f]{6}"

MIN_BIRTH_YEAR = 1920
MAX_BIRTH_YEAR = 2002

MIN_ISSUE_YEAR = 2010
MAX_ISSUE_YEAR = 2020

MIN_EXPIRATION_YEAR = 2020
MAX_EXPIRATION_YEAR = 2030

MIN_CM_HEIGHT = 150
MAX_CM_HEIGHT = 193

MIN_IN_HEIGHT = 59
MAX_IN_HEIGHT = 76


def extract_passports(file_path):
    with open(file_path) as file:
        passports = []
        passport_blocks = file.read().split("\n\n")
        for passport_block in passport_blocks:
            passport_block = passport_block.replace("\n", " ")
            try:
                passport = import_block(passport_block)
                passports.append(passport)
            except MissingRequiredValue:
                pass
            except InvalidValue:
                pass
    return passports


def import_block(passport_block):
    birth_year = get_passport_item("byr", passport_block)
    issue_year = get_passport_item("iyr", passport_block)
    expiration_year = get_passport_item("eyr", passport_block)
    height = get_passport_item("hgt", passport_block)
    hair_colour = get_passport_item("hcl", passport_block)
    eye_colour = get_passport_item("ecl", passport_block)
    passport_id = get_passport_item("pid", passport_block)
    country_id = get_passport_item("cid", passport_block)

    return Passport(birth_year, issue_year, expiration_year, height, hair_colour, eye_colour, passport_id, country_id)


def get_passport_item(item_key, passport_block):
    match_ding = item_key + ":(\\S+)"
    passport_item = re.search(match_ding, passport_block)
    return passport_item.group(1) if passport_item else None


def check_birth_year(birth_year, *, required):
    if is_accepted(birth_year, required=required):
        birth_year = check_year(birth_year, MIN_BIRTH_YEAR, MAX_BIRTH_YEAR)
        return birth_year
    else:
        raise MissingRequiredValue("This field cannot be empty, please provide a valid passport.")


def check_issue_year(issue_year, *, required):
    if is_accepted(issue_year, required=required):
        issue_year = check_year(issue_year, MIN_ISSUE_YEAR, MAX_ISSUE_YEAR)
        return issue_year
    else:
        raise MissingRequiredValue("This field cannot be empty, please provide a valid passport.")


def check_expiration_year(expiration_year, *, required):
    if is_accepted(expiration_year, required=required):
        expiration_year = check_year(expiration_year, MIN_EXPIRATION_YEAR, MAX_EXPIRATION_YEAR)
        return expiration_year
    else:
        raise MissingRequiredValue("This field cannot be empty, please provide a valid passport.")


def check_height(height, *, required):
    if is_accepted(height, required=required):
        if height[-2:] == "cm":
            if not is_in_range(int(height[:-2]), MIN_CM_HEIGHT, MAX_CM_HEIGHT):
                raise InvalidValue("A height can be at least " + str(MIN_CM_HEIGHT) + " and at most " + str(MAX_CM_HEIGHT) + ".")
        elif height[-2:] == "in":
            if not is_in_range(int(height[:-2]), MIN_IN_HEIGHT, MAX_IN_HEIGHT):
                raise InvalidValue("A height can be at least " + str(MIN_CM_HEIGHT) + " and at most " + str(MAX_CM_HEIGHT) + ".")
        else:
            raise InvalidValue("A height must be proceeded by \"cm\" or \"in\".")
        return height
    else:
        raise MissingRequiredValue("This field cannot be empty, please provide a valid passport.")


def check_hair_colour(hair_colour, *, required):
    if is_accepted(hair_colour, required=required):
        if re.match(HAIR_COLOUR_PATTERN, hair_colour):
            return hair_colour
        else:
            raise InvalidValue("A hair colour must conform to the following pattern: " + HAIR_COLOUR_PATTERN + ".")
    else:
        raise MissingRequiredValue("This field cannot be empty, please provide a valid passport.")


def check_eye_colour(eye_colour, *, required):
    if is_accepted(eye_colour, required=required):
        if eye_colour in ACCEPTED_EYE_COLOURS:
            return eye_colour
        else:
            raise InvalidValue("An eye colour must be one of the following colours: " +
                               str(ACCEPTED_EYE_COLOURS).strip('[]') + ".")
    else:
        raise MissingRequiredValue("This field cannot be empty, please provide a valid passport.")


def check_passport_id(passport_id, *, required):
    if is_accepted(passport_id, required=required):
        if re.match(PASSPORT_ID_PATTERN, passport_id):
            return passport_id
        else:
            raise InvalidValue("A passport ID must conform to the following pattern: " + PASSPORT_ID_PATTERN + ".")
    else:
        raise MissingRequiredValue("This field cannot be empty, please provide a valid passport.")


def check_country_id(country_id, *, required):
    if is_accepted(country_id, required=required):
        return country_id
    else:
        raise MissingRequiredValue("This field cannot be empty, please provide a valid passport.")


class Passport(object):
    def __init__(self,
                 birth_year, issue_year, expiration_year,
                 height, hair_colour, eye_colour,
                 passport_id, country_id):
        self.birth_year = check_birth_year(birth_year, required=True)
        self.issue_year = check_issue_year(issue_year, required=True)
        self.expiration_year = check_expiration_year(expiration_year, required=True)
        self.height = check_height(height, required=True)
        self.hair_colour = check_hair_colour(hair_colour, required=True)
        self.eye_colour = check_eye_colour(eye_colour, required=True)
        self.passport_id = check_passport_id(passport_id, required=True)
        self.country_id = check_country_id(country_id, required=False)

    def __str__(self):
        return "Passport (ID: " + xstr(self.passport_id) + " and country ID: " + xstr(self.country_id) +\
               ") from someone of " + xstr(self.height) + ", with " + xstr(self.hair_colour) + " hair and " + xstr(self.eye_colour) + " eyes. " +\
               "This person was born in " + xstr(self.birth_year) + " and was issued this passport in " + xstr(self.issue_year) + ". " +\
               "The passport will expire in " + xstr(self.expiration_year) + "."
