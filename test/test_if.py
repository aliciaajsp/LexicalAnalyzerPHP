import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'lexer')
    )
)

from lexer_conditional_if import lexer

data = '''
<?php
$num1=10;
$num2=20;

IF ($num1>$num2) {
    $bignum = $num1;
    PRINT "Big Number is " . $bignum;
}
ELSE {
    $bignum = $num2;
    PRINT "Big Number is " . $bignum;
}
?>
'''

# TOKENIZATION PROCESS
lexer.input(data)

print("\n===== LEXICAL ANALYSIS RESULT =====\n")

while True:
    tok = lexer.token()

    if not tok:
        break

    print(f"{tok.type:<12} -> {tok.value}")

print("\n===== END OF ANALYSIS =====")