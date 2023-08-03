#!/usr/bin/env python3
"""
Main file
"""

filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth"]
messages = ["name=eggyemail=eggmin@eggsample.comypassword=eggcellentydate_of_birth=12/12/1986y", "name=bobyemail=bob@dylan.comypassword=bobbycoolydate_of_birth=03/04/1993y"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, 'y'))
