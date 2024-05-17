from urllib.parse import parse_qsl

# String parameter cookie
# String parameter cookie
cookie_string = "__itrace_wid=8f50e0c5-2e85-42e3-9933-605a2abb84c5;lwrid=AQGMxFAuSThvdsT7sSdIY2I3DAOp;t_fv=1704100639808;t_uid=QnzENrjPlQj7xDuzTCT46UctxBIwJ0Nb;cna=IXEZHvGgQDACAcu+Mvti9e0y;xlly_s=1;__wpkreporterwid_=ba553b8c-7cd1-49cc-8b27-a45e5a6126f6;lzd_cid=13009bc4-3bcb-4515-f1c2-c6d464e9642a;_bl_uid=7dl6UqFauFCptUkjs720sROwqCd8;hng=ID|id-ID|IDR|360;lzd_sid=1eb99c05fd1c602d900050ee671136c6;_tb_token_=76eb13bebee43;lzd_uti=%7B%22fpd%22%3A%222021-09-11%22%2C%22lpd%22%3A%222021-09-16%22%2C%22cnt%22%3A%222%22%7D;EGG_SESS=S_Gs1wHo9OvRHCMp98md7MvsY-scsmLlOk13eE9rnoi_Pak73PL55MVPhJJC5h96bU74gA9b7CqIDTE4_ykEdHJps-VNSimO6SgJ5BdW0-g__i4yX0pITvIj4wEodRMUHPdLabRfImv67tCvX-naVSp5Ci_0YNnjtznUADOoeCw=;tfstk=e3bB5BNFo9iSiBnnCJNNh5pyJB8U39a2vbORi_3EweLKeYCvQUPn4kAWPd6kL3IUEOMRBsvdLJYPCz6DI4Rzx805CsBbZHLy8_hh5tgr8Jqhw4Tyy-y4ur5ntUY836cwSM13_YnmrrzVt6Lky-y4uWxr0dSeRoUsffCxI40rPfUEDaN6HK76OHgR9d38jNOBAKCp143-MBtBH6pG4l32harIV0vKyC9415ioqSmXEna8WWqyvCAZd5Ns4ntpsC9415ioqHdM_EF_10-f.;t_sid=LTMN1w37ijrcL5rzKzb4Nf6r7lIgXpnv;utm_channel=NA;_m_h5_tk=55811681dd4540e9d6cefc387184ff45_1704214808164;_m_h5_tk_enc=f892e45f33f360d78a557a85ebee512d;epssw=1*wZFG11gQ_5xFgp6MyuWnCjX0i7DDmKwugA5bgQOI_AZINYMsfNzLvqP41ZzaJPn_RNMBIZkMyWAcBQMcjhAWHe8-6nAOx_MA6Z4KKGSNNg5a_fB5jhjI34kbd1fe1Yp5jnwB3hxw6TO2Z1pW6F9XIYXFaWqdvc6_5nGSKfX7rI6zQaB3q-bTWos3etzXbDqxdLHJ3Aa9yIWBYYe4dLURyLKpX8BBFYKg8YEk7UpWVwHBe4QRrQ3HWJRoYUZ6reIJXqVsp5nnxDonx4QRetP.;lzd_uid=400165362962;lzd_b_csg=3a10efc2;sgcookie=E100owYTWHOArt55RUIEO3UvZ7j7UeZLhr%2BGk9%2FjTbcP7823nOsVzOVD07XPfXTMP5DTw0LoeDoORKBrJH%2FQyVVQ%2FoNS4uyMQ3x0V8Scx9xGxzE%3D;lzd_t_login=ID_ddc184aefd9147b1a777f27cf8f6ae07;isg=BKGhn5n9YOSwAMwW8AePzKABu2-7ThVAkCinZwN2m6gHas08UZ58ESeryMDK7K14"

# Mengurai string cookie
parsed_cookies = [cookie.split(';') for cookie in cookie_string.split(';')]

# Mengubah menjadi format yang dapat dimasukkan ke driver
formatted_cookies = [{'name': name_value[0].split('=')[0].strip(), 'value': name_value[0].split('=')[1].strip()} for name_value in parsed_cookies]

# Cetak format cookie
print("Formatted Cookies:")
for cookie in formatted_cookies:
    print(f"Name: {cookie['name']}, Value: {cookie['value']}")
cookies = [
    {"name": "__itrace_wid", "value": "8f50e0c5-2e85-42e3-9933-605a2abb84c5"},
    {"name": "lwrid", "value": "AQGMxFAuSThvdsT7sSdIY2I3DAOp"},
    {"name": "t_fv", "value": "1704100639808"},
    {"name": "t_uid", "value": "QnzENrjPlQj7xDuzTCT46UctxBIwJ0Nb"},
    {"name": "t_sid", "value": "rPWe79y1XVXWEEAaToZbNKzCh9gbvCUV"},
    {"name": "utm_channel", "value": "NA"},
    {"name": "cna", "value": "IXEZHvGgQDACAcu+Mvti9e0y"},
    {"name": "xlly_s", "value": "1"},
    {"name": "__wpkreporterwid_", "value": "ba553b8c-7cd1-49cc-8b27-a45e5a6126f6"},
    {"name": "lzd_cid", "value": "13009bc4-3bcb-4515-f1c2-c6d464e9642a"},
    {"name": "_bl_uid", "value": "7dl6UqFauFCptUkjs720sROwqCd8"},
    {"name": "_m_h5_tk", "value": "54102068a37c0604ff7e2a9d4f688829_1704110785768"},
    {"name": "_m_h5_tk_enc", "value": "6c2c233d96390391d3c78a4e9453dfdf"},
    {"name": "hng", "value": "ID|id-ID|IDR|360"},
    {"name": "smb_fatigue", "value": "true"},
    {"name": "lzd_sid", "value": "1eb99c05fd1c602d900050ee671136c6"},
    {"name": "_tb_token_", "value": "76eb13bebee43"},
    {"name": "lzd_uid", "value": "400165362962"},
    {"name": "lzd_b_csg", "value": "2eaa69c9"},
    {"name": "sgcookie", "value": "E100%2BLI30Ilrk3jHRahwNu%2FIjp581uI%2BrDoXtlcXVW%2FsgxHMTLDlSEWiGlRsaAOumIEoRIZ5LNxRmV%2FVlM7k710aM8CVO0bY1%2FoYclrNasBpGs8%3D"},
    {"name": "lzd_t_login", "value": "ID_38a3b232190146b1b09c9d88409618a1"},
    {"name": "lzd_uti", "value": "%7B%22fpd%22%3A%222021-09-11%22%2C%22lpd%22%3A%222021-09-16%22%2C%22cnt%22%3A%222%22%7D"},
    {"name": "tfstk", "value": "eiBDDQ96AKRA22DC2ZpbFv-6s35Mhq96kNH9WdLaaU8WMsIY1AAwyaAwBSG9Ihb9ytLAbsKGrMI1Mhp4GFYGzMAtBOjsIhSN5oTTc7Ifcd9aJyBgpisbVxeGeJeoOaRWQyULe8LMDAvNMH4YKMc7nz6Q6tmXMemEo5Fr0XYk8i8D8eWy0TYd0UDZXsKDi7j2rAkNFgkqaXuI8ATLEGhs1I-Wqedt0c2U-qb_cuqoTFR2V3uUqucs1I-WqeEuqXoHg3tr8"},
    {"name": "isg", "value": "BFhY93U4ialNOKUtwRjWlyEGIoTqQbzLsU-OfJJJpBNGLfgXOlGMW24PYXsdJnSj"},
    {"name": "epssw", "value": "1*T9hM11MfT5IrtEz4NcGbgQOIoBXiICb4NAgtbpmn7OXPNAPQm_ngjJ62NKIYr79ANKC5Dbi0wxBdycUE6T1YH_9AwKBCSB9W6U7JwTlAn1MS2N0peSd7_5HcjjNCObXR56l1B-y53YB4FUHCeYB4xDDR34daety53J9-dLHFUukOLQce1CPIJgdt1cio6DDRnzQRxDmnxf"}
]
