import requests                                     # Import requests (to download the page)
from bs4 import BeautifulSoup                       # Import BeautifulSoup (to parse what we download)
import time                                         # Import Time (to add a delay between the times the scape runs)
import smtplib                                      # Import smtplib (to allow us to email)


while True:
    url = "http://Google.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    if str(soup).find("Google") == -1:
        time.sleep(60)
        continue

    else:
        msg = 'Subject: This is Chris\'s script talking, CHECK GOOGLE!'
        fromaddr = 'akhileshkrbhagat666@gmail.com'
        toaddrs = ['akiraj20134@gmail.com']         # 'A_SECOND_EMAIL_ADDRESS', 'A_THIRD_EMAIL_ADDRESS'

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login("akhileshkrbhagat666@gmail.com", "bpbjvsuiqlznqxeo")
        subject = 'hello here are some changes from previous'

        body = "check the amazon link https://www.amazon.in/gp/product/B07HG8SBDV/ref=s9_acss_bw_cg_AugART_1a1_w?" \
               "pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-6&pf_rd_r=HQJBKWG57AKDR7TNR5FT&pf" \
               "_rd_t=101&pf_rd_p=5f8f0523-85b2-4d12-90b6-94959d312b93&pf_rd_i=1389401031"
        msg = f"Subject : {subject} \n\n {body}"

        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)
        # server.sendmail(fromaddr, toaddrs, msg)
        # server.quit()

        server.sendmail(
            'akhileshkrbhagat666@gmail.com',
            'akiraj20134@gmail.com',
            msg
        )
        print('hey email has been sent')
        server.quit()

        # break

