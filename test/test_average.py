from lexer import lexer

data = r'''
<?php

$num1 = 80;
$num2 = 90;
$num3 = 100;

$total = $num1 + $num2 + $num3;
$rata = $total / 3;

ECHO "Rata-rata: ";
ECHO $rata;

?>
'''

num1 = 80
num2 = 90
num3 = 100

total = num1 + num2 + num3
rata = total / 3

if __name__ == '__main__':

    lexer.lineno = 1
    lexer.input(data)

    print("\n===== RATA-RATA TIGA ANGKA =====\n")

    while True:
        tok = lexer.token()

        if not tok:
            break

        print(f"{tok.type:<12} -> {tok.value}")

    print("\n===== HASIL PERHITUNGAN =====")
    print(f"Total = {total}")
    print(f"Rata-rata = {rata}")

    print("\n===== END OF ANALYSIS =====")
