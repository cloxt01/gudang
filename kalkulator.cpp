#include <iostream>
using namespace std;

//deklarasi variabel
int menu;
int num1;
int num2;
float hasil;
//main program
int main () {
	cout << "Program Kalkulator\n" << endl;
	cout << "1.Penjumlahan\n2.Pengurangan\n3.Perkalian\n4.Pembagian\n5.Modulus\n" << endl;
	
	cout << "Pilih Menu : " << endl;
	cin >> menu;
	
	cout << "Masukan Bilangan Pertama : " << endl;
	cin >> num1;
	cout << "Masukan Bilangan Kedua     : " << endl;
	cin >> num2;
	
	cout << "\n";
	if (menu == 1){
		hasil = num1 + num2;
		cout << "Hasil dari" << num1 << " + " << num2 << " = " << hasil << endl;
	} else if (menu == 2){
		hasil = num1 - num2;
		cout << "Hasil dari" << num1 << " - " << num2 << " = " << hasil << endl;
	} else if (menu == 3){
		hasil = num1 * num2;
		cout << "Hasil dari" << num1 << " x " << num2 << " = " << hasil << endl;
	} else if (menu == 4){
		hasil = num1 / num2;
		cout << "Hasil dari" << num1 << " / " << num2 << " = " << hasil << endl;
	} else if (menu == 5){
		hasil = num1 % num2;
		cout << "Hasil dari" << num1 << " % " << num2 << " = " << hasil << endl;
	else {
		cout << "Menu tidak ditemukan ! " << endl;
	}
	cin.get();
	return 0;
}