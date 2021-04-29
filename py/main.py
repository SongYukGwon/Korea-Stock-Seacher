from company import call_company
from Scrapping import list_company
from save import save_to_file

words = call_company()

company_information = list_company(words)

save_to_file(company_information)
