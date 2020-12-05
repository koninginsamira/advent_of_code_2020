import re

from day_4.exceptions.MissingRequiredField import MissingRequiredField


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


def set_required_field(value):
    if value:
        return value
    else:
        raise MissingRequiredField("This field cannot be empty, please provide a valid passport.")


def set_optional_field(value, placeholder):
    if value:
        return value
    else:
        return placeholder


class Passport(object):
    def __init__(self,
                 birth_year, issue_year, expiration_year,
                 height, hair_colour, eye_colour,
                 passport_id, country_id):
        self.birth_year = set_required_field(birth_year)
        self.issue_year = set_required_field(issue_year)
        self.expiration_year = set_required_field(expiration_year)
        self.height = set_required_field(height)
        self.hair_colour = set_required_field(hair_colour)
        self.eye_colour = set_required_field(eye_colour)
        self.passport_id = set_required_field(passport_id)
        self.country_id = set_optional_field(country_id, "undefined")

    def __str__(self):
        return "Passport (ID: " + self.passport_id + " and country ID: " + self.country_id +\
               ") from someone of " + self.height + ", with " + self.hair_colour + " hair and " + self.eye_colour + " eyes. " +\
               "This person was born in " + self.birth_year + " and was issued this passport in " + self.issue_year + ". " +\
               "The passport will expire in " + self.expiration_year + "."
