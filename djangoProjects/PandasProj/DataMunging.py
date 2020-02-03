import pandas as pd

product = pd.read_csv('F:\flipkartScraping\product.csv', index_col=0)
product.to_html('edu.html')