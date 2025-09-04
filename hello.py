"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente 
o programa exibe a mensagem correspondente.

Usage:

Tenha a variavelmente LANG devidamente configurada.

Execução:

python hello.py
.\\hello.py

"""

__version__ = "0.0.1"
__author__ = "Aline Carrijo"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5] 

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"

print(msg)