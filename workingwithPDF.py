import PyPDF2

# Open the PDF file
with open('example.pdf', 'rb') as file:
    pdf = PyPDF2.PdfFileReader(file)

# Extract the text from the first page
page = pdf.getPage(0)
text = page.extractText()
print(text)
