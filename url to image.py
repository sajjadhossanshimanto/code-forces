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

# %% weasyprint 
# -> external executable depen
from weasyprint import HTML
import requests

# Fetch webpage content
url = "https://example.com"
response = requests.get(url)
html_content = response.text

# Convert to PDF
output_file = "output.pdf"
HTML(string=html_content).write_pdf(output_file)

# With custom styles
stylesheets = [
    # Add CSS if needed
    'https://example.com/style.css'
]
HTML(string=html_content).write_pdf(output_file, stylesheets=stylesheets)
# %% selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pdfkit  # We'll still use pdfkit to convert the rendered HTML to PDF

def webpage_to_pdf(url, output_path):
    try:
        # Set up Chrome options
        chrome_options = Options()
        # chrome_options.add_argument('--headless')  # Run in background
        # chrome_options.add_argument('--disable-gpu')
        
        # Initialize the driver
        driver = webdriver.Chrome(options=chrome_options)
        
        # Navigate to the webpage
        driver.get(url)
        
        # Wait for page to load (adjust time as needed)
        driver.implicitly_wait(5)
        
        # Get the fully rendered HTML
        html_content = driver.page_source
        
        # Configure PDF options
        pdf_options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8"
        }
        
        # Convert to PDF
        pdfkit.from_string(html_content, output_path, options=pdf_options)
        
        print(f"PDF successfully created at {output_path}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
    # finally:
        # Clean up
        # driver.quit()

# Usage
# url = "https://example.com"
output_file = "output_selenium.pdf"
webpage_to_pdf(url, output_file)

# %% selenium -> chome's build in pdf print
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64
import json


def delete_element(element):
    driver.execute_script("""
    var element = arguments[0];
    element.parentNode.removeChild(element);
    """, element)

def webpage_to_pdf(output_path):    
    # Configure print parameters
    print_options = {
        'landscape': False,
        'displayHeaderFooter': False,
        'printBackground': True,
        'paperWidth': 8.27,  # A4 width in inches
        'paperHeight': 11.69,  # A4 height in inches
        # 'marginTop': 0.75,
        # 'marginBottom': 0.75,
        # 'marginLeft': 0.75,
        # 'marginRight': 0.75,
        'scale': 1
    }
    
    # Execute print to PDF command
    result = driver.execute_cdp_cmd('Page.printToPDF', print_options)
    
    # Decode base64 PDF data and save
    pdf_data = base64.b64decode(result['data'])
    with open(output_path, 'wb') as file:
        file.write(pdf_data)
        
    print(f"PDF successfully created at {output_path}")

def load_page(url):
    driver.get(url)
    return WebDriverWait(driver, 10).until(# max 10 secs
        EC.presence_of_element_located((By.CLASS_NAME, "problem-statement"))
    )

# Set up Chrome options
chrome_options = Options()
# chrome_options.add_argument('--headless')  # Run in background
# chrome_options.add_argument('--disable-gpu')

# Initialize driver
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# Usage
# url = "https://example.com"
output_file = "output_print2pdf.pdf"
# webpage_to_pdf(url, output_file)

def filter_page():
    # Remove unwanted elements
    delete_element(driver.find_element(By.ID, "header"))
    delete_element(driver.find_element(By.ID, "footer"))
    delete_element(driver.find_element(By.CLASS_NAME, "menu-box"))
    delete_element(driver.find_element(By.CLASS_NAME, "ContestVirtualFrame"))


# %%
