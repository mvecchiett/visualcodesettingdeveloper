import re
# 42536258796157867 #17 dígitos en número de tarjeta → Inválido
# 4424444424442444 #Los dígitos consecutivos se repiten 4 o más veces → Inválido
# 5122-2368-7954 - 3214 #Se utilizan separadores distintos de '-' → Inválido
# 44244x4424442444 #Contiene caracteres que no son dígitos → Inválido
# 0525362587961578 #No empieza con 4, 5 o 6 → Inválido.

validator = re.compile(r"^"
                       r"(?!.*(\d)(-?\1){3})"
                       r"[456]"  # Doesn't start with 4, 5 or 6 → Invalid
                       r"\d{3}"  # Contains non digit characters → Invalid
                       r"(?:-?\d{4}){3}"
                       r"$")

for _ in range(int(input().strip())):
    print("Valid" if validator.search(input().strip()) else "Invalid")
