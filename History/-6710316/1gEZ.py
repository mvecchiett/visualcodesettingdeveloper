import re

class Validaciones:



   def validartarjeta(self, nrotarjeta):
        # 42536258796157867 #17 dígitos en número de tarjeta → Inválido
        # 4424444424442444 #Los dígitos consecutivos se repiten 4 o más veces → Inválido
        # 5122-2368-7954 - 3214 #Se utilizan separadores distintos de '-' → Inválido
        # 44244x4424442444 #Contiene caracteres que no son dígitos → Inválido
        # 0525362587961578 #No empieza con 4, 5 o 6 → Inválido.
    regex_pattern = re.compile(r"^"
                       r"(?!.*(\d)(-?\1){3})"
                       r"[456]"  #No empieza con 4, 5 o 6 → Inválido.
                       r"\d{3}"  #Contiene caracteres que no son dígitos → Inválido
                       r"(?:-?\d{4}){3}"
                       r"$")
    return regex_pattern.match(nrotarjeta)

