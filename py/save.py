import csv


def save_to_file(companys):
    file = open("company_information.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["company", "stock_price"])
    for company in companys:
        writer.writerow(list(company.values()))
