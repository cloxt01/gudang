<?php
class ApiCrypto
{
    function cHeader_POST($request)
    {
        $ch = curl_init();
        $url_encrypt = openssl_decrypt("9Dak7fa1LE2kNF62YztSo2AZzhNMqhm5qtMpR0/nrL0mYV6b4NK93Yt/DMGyd+T96Lo=","AES-128-CTR",base64_decode("bHljb3h6"),0,base64_decode("MDgwNDIwMDIxNjAxMjAwNA=="));
        curl_setopt($ch, CURLOPT_URL,sprintf($url_encrypt,$request));
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt ($ch, CURLOPT_ENCODING, "gzip");
        $server_output = curl_exec ($ch);
        curl_close ($ch);
        flush();
        return $server_output;
    }

    function Api_Encrypt($data)
    {
        $enc = openssl_decrypt("+Syz7/z/dz32IFL2","AES-128-CTR",base64_decode("bHljb3h6"),0,base64_decode("MDgwNDIwMDIxNjAxMjAwNA=="));
        $query = array($enc => "".$data."");
        return $this->cHeader_POST(base64_encode(json_encode($query)));
    }

    function encrypt($data)
    {
        $json_enc = json_decode($this->Api_Encrypt($data), true);
        $enc_data = openssl_decrypt("+COk/A==","AES-128-CTR",base64_decode("bHljb3h6"),0,base64_decode("MDgwNDIwMDIxNjAxMjAwNA=="));
        $data_enc = $json_enc[$enc_data];
        $decrypt_data_enc = base64_decode((string)$data_enc,true);
        $json_data_enc = json_decode($decrypt_data_enc, true);
        $enc_decrypt_3des = openssl_decrypt("+Cez7/z/dz32IFL2","AES-128-CTR",base64_decode("bHljb3h6"),0,base64_decode("MDgwNDIwMDIxNjAxMjAwNA=="));
        $decrypt_3des = $json_data_enc[$enc_decrypt_3des];
        return $decrypt_3des;
    }
    
    function Api_Decrypt($data)
    {
        $dec = openssl_decrypt("+Cez7/z/dz32IFL2","AES-128-CTR",base64_decode("bHljb3h6"),0,base64_decode("MDgwNDIwMDIxNjAxMjAwNA=="));
        $query = array($dec => "".$data."");
        return $this->cHeader_POST(base64_encode(json_encode($query)));
    }

    function decrypt($data)
    {
        $json_dec = json_decode($this->Api_Decrypt($data), true);
        $enc_data = openssl_decrypt("+COk/A==","AES-128-CTR",base64_decode("bHljb3h6"),0,base64_decode("MDgwNDIwMDIxNjAxMjAwNA=="));
        $data_dec = $json_dec[$enc_data];
        $decrypt_data_dec = base64_decode((string)$data_dec,true);
        $json_data_dec = json_decode($decrypt_data_dec, true);
        $enc_encrypt_3des = openssl_decrypt("+Syz7/z/dz32IFL2","AES-128-CTR",base64_decode("bHljb3h6"),0,base64_decode("MDgwNDIwMDIxNjAxMjAwNA=="));
        $encrypt_3des = $json_data_dec[$enc_encrypt_3des];
        return $encrypt_3des;
    }
}

class ApiAXIS
{
    function SendOTP($msisdn_otp)
    {
        $crypto = new ApiCrypto;
        $url_encrypt = "U2H4FivA7_TARK4rDYw240Z35aNAvZ3QpxHTMjbk7580oUAou599G8oqqkcrd6ht2SVW64mjyH4HsaF4ukoLlw==";

        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, sprintf($crypto->decrypt($url_encrypt), $msisdn_otp));
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_ENCODING, "gzip");

        $server_output = curl_exec($ch);
        curl_close($ch);
        flush();

        return $server_output;
    }
}

// Input nomor telepon dari pengguna
echo "Masukkan nomor telepon: ";
$nomor = str_replace(['-', '+', ' '], ['', '', ''], trim(fgets(STDIN)));

// Menggunakan kelas ApiAXIS untuk mengirim OTP
$axis = new ApiAXIS;
$result = $axis->SendOTP($nomor);echo "Hasil pengiriman OTP: " . $result . "\n";

// Periksa apakah $result tidak null sebelum melanjutkan
// Fungsi untuk mendekripsi teks
function decryptText($encryptedText)
{
    $key = base64_decode("bHljb3h6"); // Ganti dengan kunci yang sesuai
    $iv = base64_decode("MDgwNDIwMDIxNjAxMjAwNA=="); // Ganti dengan IV yang sesuai

    // Gunakan fungsi openssl_decrypt
    $decryptedText = openssl_decrypt($encryptedText, "AES-128-CTR", $key, 0, $iv);

    return $decryptedText;
}

// Fungsi untuk mendekripsi teks dari kelas ApiCrypto
function decryptApiCryptoText($encryptedText)
{
    $crypto = new ApiCrypto();

    // Panggil fungsi decrypt pada objek $crypto
    $decryptedText = $crypto->decrypt([$encryptedText]);

    return $decryptedText;
}

// Teks yang akan didekripsi
$encryptedText = "U2H4FivA7_TARK4rDYw240Z35aNAvZ3QpxHTMjbk7580oUAou599G8oqqkcrd6ht2SVW64mjyH4HsaF4ukoLlw";

// Panggil fungsi decryptText
$decryptedText = decryptText($encryptedText);

// Tampilkan hasil dekripsi
echo "Teks yang didekripsi: " . $decryptedText . "\n";

// Panggil fungsi decryptApiCryptoText
$decryptedApiCryptoText = decryptApiCryptoText($encryptedText);

// Tampilkan hasil dekripsi dari kelas ApiCrypto
echo "Teks yang didekripsi menggunakan ApiCrypto: " . $decryptedApiCryptoText . "\n";
