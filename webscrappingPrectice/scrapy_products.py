import requests
from bs4 import BeautifulSoup
import smtplib
from time import sleep

url = 'https://www.amazon.in/gp/product/B07HG8SBDV/ref=s9_acss_bw_cg_AugART_1a1_w?' \
      'pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-6&pf_rd_r=HQJBKWG57AKDR7TNR5FT&pf' \
      '_rd_t=101&pf_rd_p=5f8f0523-85b2-4d12-90b6-94959d312b93&pf_rd_i=1389401031'

headers = {"user-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                         ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}


def check_price():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_dealprice').get_text()
    con = price.replace(',', '')
    final_price = con.strip()
    if final_price < '45000.00':
        send_mail()

    print(final_price)
    print(title.strip())

    if final_price > '49000.00':
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('akhileshkrbhagat666@gmail.com', 'bpbjvsuiqlznqxeo')
    subject = 'hey price fall down do not miss this opportunity'
    body = "check the amazon link https://www.amazon.in/gp/product/B07HG8SBDV/ref=s9_acss_bw_cg_AugART_1a1_w?" \
           "pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-6&pf_rd_r=HQJBKWG57AKDR7TNR5FT&pf" \
           "_rd_t=101&pf_rd_p=5f8f0523-85b2-4d12-90b6-94959d312b93&pf_rd_i=1389401031"
    msg = f"Subject : {subject} \n\n {body}"

    server.sendmail(
        'akhileshkrbhagat666@gmail.com',
        'akiraj20134@gmail.com',
        msg
    )
    print('hey email has been sent')
    server.quit()


# check_price()
while True:
    check_price()
    sleep(60 * 60)

