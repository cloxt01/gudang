<?php

// Fungsi untuk mendekripsi teks
function decryptText($encryptedText)
{
    $key = base64_decode("bHljb3h6"); // Ganti dengan kunci yang sesuai
    $iv = base64_decode("MDgwNDIwMDIxNjAxMjAwNA=="); // Ganti dengan IV yang sesuai

    // Gunakan fungsi openssl_decrypt
    $decryptedText = openssl_decrypt($encryptedText, "AES-128-CTR", $key, 0, $iv);

    return $decryptedText;
}

// Teks yang akan didekripsi
$encryptedText = "U2H4FivA7_TARK4rDYw240Z35aNAvZ3QpxHTMjbk7580oUAou599G8oqqkcrd6ht2SVW64mjyH4HsaF4ukoLlw";

// Panggil fungsi decryptText
$decryptedText = decryptText($encryptedText);

// Tampilkan hasil dekripsi
echo "Teks yang didekripsi: " . $decryptedText . "\n";