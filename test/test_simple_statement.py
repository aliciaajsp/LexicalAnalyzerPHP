import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'lexer')
    )
)

from lexer_simple_statement import lexer


data = r'''
<?php //php 7.2.24

PRINT "Hello, world! \n";
ECHO "Welcome "

?>
'''

expected_tokens = [
    'PHP_OPEN',
    'PRINT',
    'STRING',
    'SEMICOLON',
    'ECHO',
    'STRING',
    'PHP_CLOSE'
]

lexer.lineno = 1
lexer.input(data)

actual_tokens = []

print("\n===== SIMPLE STATEMENT TEST =====\n")

while True:
    tok = lexer.token()

    if not tok:
        break

    actual_tokens.append(tok.type)

    print(f"{tok.type:<12} -> {tok.value}")

# VALIDATION
print("\n===== VALIDATION RESULT =====\n")

if actual_tokens == expected_tokens:
    print("TEST PASSED!")
    print("All tokens match the expected sequence.")

else:
    print("TEST FAILED!")
    print("Expected:", expected_tokens)
    print("Actual:  ", actual_tokens)

print("\n===== END OF TEST =====")