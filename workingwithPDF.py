import PyPDF2

from PyPDF2 import PdfReader

reader = PdfReader("test.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
account_index = text.find("Account Number:")
gross_index = text.find("Gross Pay (Rs.):")
deductions_index = text.find("Deductions: (Rs.):")
net_index = text.find("Net Pay: (Rs.):")

account_number = text[int(account_index): int(account_index)+27]

gross_pay = text[int(gross_index): int(gross_index)+35]
deductions = text[int(deductions_index): int(deductions_index)+38]
net_pay = text[int(net_index): int(net_index)+35]
print(account_number + gross_pay + deductions + net_pay)
