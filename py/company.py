import csv


def call_company():
    with open('company.csv', 'r') as f:
        reader = csv.reader(f)
        companys = []
        for row in reader:
            companys.extend(row)
    return companys
