from lexer import lexer

data = r'''
<?php

$num1 = 10;
$num2 = 20;
$hasil = $num1 + $num2;

ECHO "Hasil penjumlahan: ";
ECHO $hasil;

?>


num1 = 10
num2 = 20
hasil = num1 + num2

if __name__ == '__main__':

    lexer.lineno = 1
    lexer.input(data)

    print("\n===== PENJUMLAHAN DUA ANGKA =====\n")

    while True:
        tok = lexer.token()

        if not tok:
            break

        print(f"{tok.type:<12} -> {tok.value}")

    print("\n===== HASIL PERHITUNGAN =====")
    print(f"{num1} + {num2} = {hasil}")

    print("\n===== END OF ANALYSIS =====")
