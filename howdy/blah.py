import os
import csv

data = "Springfield"
name = data.split(',')[0] # lower case and remove any reference to state
# check if the city is in the csv file
valid_city = False
fname = os.path.join(os.path.dirname(__file__), 'dummy_csv.csv')
with open(fname, "r") as f:
    csvreader = csv.reader(f, delimiter=",")
    for row in csvreader:
        if name.lower() in row[0].lower():
            valid_city = True
            break
if not valid_city:
    raise ValidationError(_('Invalid city name'))

print("FOUND {}".format(data))
