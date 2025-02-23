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
pdfkit.from_url(url, output_file, options=options)

# %%
