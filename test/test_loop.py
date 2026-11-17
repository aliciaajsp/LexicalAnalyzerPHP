import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "lexer"))

from lexer_looping import lexer

data = '''
<?php
PRINT "List of Odd Number 1-100:\\n";
PRINT "\\n";

$num=1;

WHILE ($num<=100) {
    IF (($num % 2)!=0) {
        $oddnum=$num;
        PRINT "".$num." ";
    }

    $num=$num+1;
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