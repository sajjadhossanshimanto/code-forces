#%%
url = "https://codeforces.com/problemset/problem/1914/D"

#%% with pdfkit
import pdfkit

# Basic usage
output_file = "output.pdf"

# Convert webpage to PDF
pdfkit.from_url(url, output_file)

# With options
options = {
    'page-size': 'A4',
    # 'margin-top': '0.75in',
    # 'margin-right': '0.75in',
    # 'margin-bottom': '0.75in',
    # 'margin-left': '0.75in',
}
# pdfkit.from_url(url, output_file, options=options)

#%% modified html with pdfkit
import requests
from bs4 import BeautifulSoup
import pdfkit

# Fetch the web page
# url = 'https://example.com'
response = requests.get(url)
html_content = response.text


# Use BeautifulSoup to parse and modify the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Example: Modify the title of the page
# title_tag = soup.find(id="header")
# if title_tag:
#     title_tag.string = 'Modified Title'


# Example: Add a new paragraph at the end
new_paragraph = soup.new_tag('p')
new_paragraph.string = 'This is a new paragraph added to the page.'
soup.body.append(new_paragraph)

# Convert the modified HTML to a PDF
modified_html = str(soup)
pdfkit.from_string(modified_html, 'output_pdfkit_from html.pdf')

print("PDF generated with modified content!")


# %%
