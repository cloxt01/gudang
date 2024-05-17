import requests
import json
import time

url = "https://shopee.co.id/api/v4/checkout/get"

current_time = int(time.time())

data = {
    "_cft": [1811668587, 2],
    "timestamp": current_time,
    "shoporders": [
        {
            "shop": {"shopid": 85463417},
            "items": [
                {
                    "itemid": 16083140214,
                    "modelid": 221768575714,
                    "quantity": 1,
                    "add_on_deal_id": 0,
                    "is_add_on_sub_item": False,
                    "item_group_id": None,
                    "insurances": [],
                    "channel_exclusive_info": {"source_id": 0, "token": ""},
                    "supports_free_returns": False,
                }
            ],
            "shipping_id": 1,
        }
    ],
    "selected_payment_channel_data": {
        "version": 2,
        "option_info": "",
        "channel_id": 8005200,
        "channel_item_option_info": {"option_info": "89052004"},
        "text_info": {},
    },
    "promotion_data": {
        "use_coins": False,
        "free_shipping_voucher_info": {
            "free_shipping_voucher_id": 0,
            "free_shipping_voucher_code": "",
            "disabled_reason": None,
            "disabled_reason_code": 0,
            "banner_info": {"msg": "", "learn_more_msg": ""},
            "required_be_channel_ids": [],
            "required_spm_channels": [],
        },
        "platform_vouchers": [],
        "shop_vouchers": [],
        "check_shop_voucher_entrances": True,
        "auto_apply_shop_voucher": False,
    },
    "fsv_selection_infos": [],
    "device_info": {
        "device_id": "",
        "device_fingerprint": "",
        "tongdun_blackbox": "",
        "buyer_payment_info": {},
    },
    "buyer_info": {
        "kyc_info": None,
        "checkout_email": "",
        "spl_activation_status": 0,
        "authorize_to_leave_preference": 0,
    },
    "cart_type": 0,
    "client_id": 0,
    "client_event_info": {
        "is_platform_voucher_changed": False,
        "is_fsv_changed": False,
        "recommend_payment_preselect_type": 0,
        "recommend_shipping_preselect": False,
    },
    "tax_info": {"tax_id": ""},
    "dropshipping_info": {"enabled": False, "name": "", "phone_number": ""},
    "shipping_orders": [
        {
            "sync": True,
            "buyer_address_data": {"addressid": 101966111, "address_type": 0, "tax_address": ""},
            "selected_logistic_channelid": 8003,
            "shipping_id": 1,
            "shoporder_indexes": [0],
            "selected_preferred_delivery_time_slot_id": None,
            "selected_preferred_delivery_window": {},
            "prescription_info": {"images": None},
            "fulfillment_info": {
                "fulfillment_flag": 64,
                "fulfillment_source": "",
                "managed_by_sbs": False,
                "order_fulfillment_type": 2,
                "warehouse_address_id": 0,
                "is_from_overseas": False,
            },
        }
    ],
    "order_update_info": {},
    "checkout_price_data": {
        "merchandise_subtotal": 299900000,
        "shipping_subtotal_before_discount": 1550000000,
        "shipping_discount_subtotal": 0,
        "shipping_subtotal": 1550000000,
        "tax_payable": 0,
        "tax_exemption": 0,
        "import_tax_amount": 0,
        "icms_amount": 0,
        "iof_amount": 0,
        "custom_tax_subtotal": 0,
        "promocode_applied": None,
        "credit_card_promotion": None,
        "shopee_coins_redeemed": None,
        "group_buy_discount": 0,
        "bundle_deals_discount": None,
        "price_adjustment": None,
        "buyer_txn_fee": 100000000,
        "buyer_service_fee": 100000000,
        "insurance_subtotal": 0,
        "insurance_before_discount_subtotal": 0,
        "insurance_discount_subtotal": 0,
        "vat_subtotal": 0,
        "total_payable": 2049900000,
    },
}

headers = {
    "Host": "shopee.co.id",
    "Content-Length": str(len(json.dumps(data))),
    "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "Referer": "https://shopee.co.id",
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "Origin": "https://shopee.co.id",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    # Tambahkan header lain berdasarkan data yang telah diberikan
    "cookie": (
        "_gcl_au=1.1.724160787.1703912992; "
        "_med=affiliates; "
        "SPC_SI=M4CKZQAAAABJQzd2UUpWbtuXNwAAAAAATXhpaUg3T1I=; "
        "SPC_SEC_SI=v1-a1IyNTZDTWlzeWFRUEpYSMRAkuyrAtayBHCcatLFiqMmWDgi9ir/JmKmvoMJiX40gmkopyxCEfgNLB5dR02QBkOSDKuaRJn+e+ha2eCnB68=; "
        "SPC_F=qOYU5Cl21ZFsFMLeJCXcTAfwFsZtMPlt; "
        "REC_T_ID=4b9f0db3-a7a1-11ee-9357-eebf8a9e1561; "
        "_QPWSDCXHZQA=543a6355-8d66-45e1-868a-743a3aeee00718e63f63; "
        "REC7iLP4Q=7ce3185b-d2ef-42e8-8247-65dd0e70b113; "
        "_fbp=fb.2.1704002178883.759980235; "
        "HAS_BEEN_REDIRECTED=true; "
        "AMP_TOKEN=%24NOT_FOUND; "
        "_gid=GA1.3.924965936.1704002189; "
        "SPC_CLIENTID=cU9ZVTVDbDIxWkZzsjowtgdbcwfdixqj; "
        "SPC_EC=.eEtUYldrWmxxSUI2VGkzUGcytmhiJJyp4WeU1PMTBXvyYTNObaLqBi4bVLKeHi2VCQIChKKbK/ka9TOBPOdgb9nBh20ANdvA78aUuI2UNez8fwA8nedvKkiqLT2fap7FXuTU8c9SpIBu7DSQtuJFj9RGsDznERF7CU/SzPe3P0zm7TH/ngKyW6QewFlywxBP1QpJD0GN7b8RZcDF+DHMrg==; "
        "SPC_ST=.eEtUYldrWmxxSUI2VGkzUGcytmhiJJyp4WeU1PMTBXvyYTNObaLqBi4bVLKeHi2VCQIChKKbK/ka9TOBPOdgb9nBh20ANdvA78aUuI2UNez8fwA8nedvKkiqLT2fap7FXuTU8c9SpIBu7DSQtuJFj9RGsDznERF7CU/SzPe3P0zm7TH/ngKyW6QewFlywxBP1QpJD0GN7b8RZcDF+DHMrg==; "
        "SPC_U=690967806; "
        "SPC_T_IV=YnRLN0hTZ1VpMm5wTGoyeg==; "
        "SPC_R_T_ID=OLGJOtCERcuYgYW+Pk9t7tXc4mQ4JEaqULQl+nsaEGurZfqH8rOXIDORmksJ96kifK2aPMWRKd8GQ+p9AQquzsfnn8WTK4p8aM0tUYq72M/6ewLT6f8X9Nq01iyuNpqso1sTW/idnHMNxZhXwmY6mp4rxWnzjHgLzuFggKlYKG8=; "
        "SPC_R_T_IV=YnRLN0hTZ1VpMm5wTGoyeg==; "
        "SPC_T_ID=OLGJOtCERcuYgYW+Pk9t7tXc4mQ4JEaqULQl+nsaEGurZfqH8rOXIDORmksJ96kifK2aPMWRKd8GQ+p9AQquzsfnn8WTK4p8aM0tUYq72M/6ewLT6f8X9Nq01iyuNpqso1sTW/idnHMNxZhXwmY6mp4rxWnzjHgLzuFggKlYKG8=; "
        "shopee_webUnique_ccd=c9rtuuVNobQbkVMAnpLjiw%3D%3D%7CGnBPdurV%2BdbTCAAKLh2ZY2CSAea4Hwv17EkqVufzwbABZ%2BvRj3HB831GUp6fTKW9COC%2Fgo4dy0oOCOTJ%7ChoCtyd7AZStoqbvT%7C08%7C3; "
        "ds=d09f0c10c4f4cccab48cfc5cad9dd2e3; "
        "_ga_SW6D8G0HXK=GS1.1.1704002182.1.1.1704003650.39.0.0; "
        "_ga=GA1.1.120456746.1704002183; "
        "csrftoken=HC7wM7IYcuBDv43ujk5OKoO1zbWdj9kK; "
        "_sapid=547235422c70a4272675ba0ded29674e8cb670e0e608169bd09e0c76"
    ),
}

response = requests.post(url, json=data, headers=headers)

print(response.json())