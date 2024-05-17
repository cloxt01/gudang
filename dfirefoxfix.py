import time,os
from selenium import webdriver
from urllib.parse import urlparse
from urllib.parse import unquote
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Payload
response_page = 'response_page.html'
url = "https://www.lazada.co.id/wow/gcp/id/trade/shipping?spm=a2o4j.pdp_revamp_css.main_page.bottom_bar_main_button&buyParams=%7B%22items%22%3A%5B%7B%22itemId%22%3A%227262046176%22%2C%22skuId%22%3A%2213970378600%22%2C%22quantity%22%3A1%2C%22attributes%22%3Anull%7D%5D%7D&from_pdp_buy_now=1&pwa_true_login=1"
url_decode = unquote(url, encoding='utf-8')
cookie_string = "__itrace_wid=8f50e0c5-2e85-42e3-9933-605a2abb84c5;lwrid=AQGMxFAuSThvdsT7sSdIY2I3DAOp;t_fv=1704100639808;t_uid=QnzENrjPlQj7xDuzTCT46UctxBIwJ0Nb;cna=IXEZHvGgQDACAcu+Mvti9e0y;xlly_s=1;__wpkreporterwid_=ba553b8c-7cd1-49cc-8b27-a45e5a6126f6;lzd_cid=13009bc4-3bcb-4515-f1c2-c6d464e9642a;_bl_uid=7dl6UqFauFCptUkjs720sROwqCd8;hng=ID|id-ID|IDR|360;lzd_sid=1eb99c05fd1c602d900050ee671136c6;_tb_token_=76eb13bebee43;lzd_uti=%7B%22fpd%22%3A%222021-09-11%22%2C%22lpd%22%3A%222021-09-16%22%2C%22cnt%22%3A%222%22%7D;tfstk=e3bB5BNFo9iSiBnnCJNNh5pyJB8U39a2vbORi_3EweLKeYCvQUPn4kAWPd6kL3IUEOMRBsvdLJYPCz6DI4Rzx805CsBbZHLy8_hh5tgr8Jqhw4Tyy-y4ur5ntUY836cwSM13_YnmrrzVt6Lky-y4uWxr0dSeRoUsffCxI40rPfUEDaN6HK76OHgR9d38jNOBAKCp143-MBtBH6pG4l32harIV0vKyC9415ioqSmXEna8WWqyvCAZd5Ns4ntpsC9415ioqHdM_EF_10-f.;_m_h5_tk=55811681dd4540e9d6cefc387184ff45_1704214808164;_m_h5_tk_enc=f892e45f33f360d78a557a85ebee512d;lzd_uid=400165362962;smb_fatigue=true;t_sid=BdM57I5mPy1CDYnAn1otTNwQstAjRNZb;utm_channel=NA;lzd_b_csg=875858d5;sgcookie=E100tFXBbzMivb1ub7orrJwYL2z%2BTJ4WOyIZM6Ajgk6mGPT709MMDIeptgZ7S5Z%2FpOypY6sV4YxiGiDxovecTg0Nq0Y6Np95Xv2OVy2%2FxoFA5OE%3D;lzd_t_login=ID_6184f0c857404899b55dd502a3333e28;isg=BDw8SarIdVshcUEBRYx6g23KBtjuNeBfzTPqEBa9SCcK4dxrPkWw77JTxReZiBi3;epssw=1*iWRK11GM05LrtFzaIA7GE9OSoBXiIdkMuzUo8mZWfRgV7lGdPQHI3hxMjhxau962NKIGIfEzwxCJrCgFdtRp3_9AwKC9J69Wj1IdanUqn1MS2i4FeSpI60oSNVRh8R9R56l1B-rExkmnHUK3xv9-dLHBekqduEJ53vEk5gMCvxQq1Tnnxv9uclYND0bBtXcNQkLY6W_NcMmnYDmnxv98dC"

# ChromeOptions
options = webdriver.ChromeOptions()

#ChromeDriver Options
options.add_argument("--headless")
options.add_argument("--no-sandbox")
#Additional Header
options.add_argument('Host=www.lazada.co.id')
options.add_argument('sec-ch-ua="Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"')
options.add_argument('sec-ch-ua-mobile=?1')
options.add_argument('sec-ch-ua-platform="Android"')
options.add_argument('upgrade-insecure-requests=1')
options.add_argument('user-agent=Mozilla/5.0 (Linux; Android 12; M2004J19C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.43 Mobile Safari/537.36')
options.add_argument('accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7')
options.add_argument('x-requested-with=web.dassem.livewebsiteeditorfree')
options.add_argument('sec-fetch-site=none')
options.add_argument('sec-fetch-mode=navigate')
options.add_argument('sec-fetch-user=?1')
options.add_argument('sec-fetch-dest=document')
options.add_argument('accept-encoding=gzip, deflate, br')
options.add_argument('accept-language=id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7')

#Webdriver ChromeOptions
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(url)

# Adding Cookie to Driver
parsed_cookies = [cookie.split(';') for cookie in cookie_string.split(';')]
formatted_cookies = [{'name': name_value[0].split('=')[0].strip(), 'value': name_value[0].split('=')[1].strip()} for name_value in parsed_cookies]
for formatted_cookie in formatted_cookies:
    try:
        driver.add_cookie(formatted_cookie)
        print(f"Added cookie: {formatted_cookie['name']}")
    except Exception as e:
        print(f"Error : {e}")
        
try:
    # Open Url
    print("Opening the url")
    driver.get(url)

    # Print headers response
    try:
      print("Searching an element")
      element_present = EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Buat Pesanan')]"))
      WebDriverWait(driver, 10).until(element_present)
      response_headers = driver.execute_script("return performance.getEntries()[0].responseHeaders")
      print("Response Headers:")
      print(response_headers)
    except Exception as e:
      print(f"Error when find element: {e}")
      
    time.sleep(2)
    # Saving page source response
    print("Saving page source response")
    with open(response_page, 'w') as file:
        file.write(response_text)
    # Menunda sebentar sebelum menyimpan tangkapan layar
    time.sleep(2)
    # Saving screenshot response
    driver.save_screenshot("/sdcard/download/code/screenshot.png")
    print("Saving screenshot")
except Exception as e:
    print(f"Error: {e}")
finally:
    # Selalu panggil driver.quit() untuk memastikan penutupan sesi
    driver.quit()