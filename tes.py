from selenium import webdriver
# URL dan Header
url = 'https://www.lazada.co.id/wow/gcp/id/trade/shipping?spm=a2o4j.pdp_revamp_css.main_page.bottom_bar_main_button&buyParams=%7B%22items%22%3A%5B%7B%22itemId%22%3A%227262046176%22%2C%22skuId%22%3A%2213970378600%22%2C%22quantity%22%3A1%2C%22attributes%22%3Anull%7D%5D%7D&from_pdp_buy_now=1&pwa_true_login=1'
headers = {
    'Host': 'www.lazada.co.id',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2004J19C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.43 Mobile Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'x-requested-with': 'web.dassem.livewebsiteeditorfree',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '__itrace_wid=c8e6b3d1-4007-43dd-38e3-697620ec2524; hng=ID|id-ID|IDR|360; hng.sig=dJwrVwSueShOlZz95EBCvlH9FLAVtzGZ3msUnc25HIQ; lzd_cid=3a1c98a6-abf9-4b60-b2a5-d8887c20c105; t_uid=3a1c98a6-abf9-4b60-b2a5-d8887c20c105; lzd_sid=16cf6c4404c8344823a2c4b6bdb69c3d; _tb_token_=5ebf351efdba6; lwrid=AQGMvu26Sbu%2Fncs7ZZCDY2I3DAOp; t_fv=1704010300320; t_sid=n7lG85vwXAEbsYVDXuzB680NjHQB0368; utm_channel=NA; _bl_uid=y0labqpmttX7g7qkvi55xy8vU867; cna=PBAYHqlloDYCAYzVBPe6UqIC; xlly_s=1; __wpkreporterwid_=ddab343d-5d95-45ed-3da5-f18be9386357; _m_h5_tk=59ee9583573caf91b239da7997be8722_1704017508210; _m_h5_tk_enc=65fe595d8451aabe2b658836236d37e5; smb_fatigue=true; _gcl_au=1.1.1346616119.1704010311; x5sec=7b22617365727665722d6c617a6164613b33223a22617c434f4847784b7747454f335333644c342f2f2f2f2f77456943584a6c5932467764474e6f5954434C6b7175502f2f2f2f2f2f3842536a41774d5441335a6d59774d4441774d4441794d4441344d4441774d4441774d4451794d544178596a4d314d57466d5a5745785a544d7a5a6d51344e6a41774d54553d222c22733b32223a2265623566383334373165666230376438227d'
}
# Set opsi Chrome
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# Atur header
options.add_argument(f'--host={headers["Host"]}')
options.add_argument(f'--sec-fetch-ua={headers["sec-fetch-ua"]}')
options.add_argument(f'--sec-fetch-ua-mobile={headers["sec-fecth-mobile]}')
options.add_argument(f'--sec-fetch-ua-platform={headers["sec-fecth-platform]}')
options.add_argument(f'--upgrade-insecure-requests={headers[upgrade-insecure-requests]}')
options.add_argument(f'--user-agent={headers["user-agent"]}')
options.add_argument(f'--accept={headers["accept"]}')
options.add_argument(f'--x-requested-with={headers["x-requested-with"]}')
options.add_argument(f'--sec-fetch-site={headers["sec-fetch-site"]}')
options.add_argument(f'--sec-fetch-mode={headers["sec-fetch-mode"]}')
options.add_argument(f'--sec-fetch-user={headers["sec-fecth-user"]}')
options.add_argument(f'--sec-fetch-dest={headers["sec-fetch-dest"]}')
options.add_argument(f'--accept-encoding={headers["accept-enlcoding"]}')
options.add_argument(f'--accept-language={headers["accept-language"]}')
options.add_argument(f'--cookie={headers["cookie"]}')


# Inisialisasi driver Firefox
driver = webdriver.Chrome(options=options)

# Buka URL dengan header yang diberikan
driver.get(url)

# Dapatkan halaman yang dimuat
page_source = driver.page_source

# Cetak halaman HTML
print(page_source)

# Tutup driver
driver.quit()