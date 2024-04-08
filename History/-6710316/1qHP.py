import re

class Validaciones:

    def __init__(self,):
        # 42536258796157867 #17 dígitos en número de tarjeta → Inválido
        # 4424444424442444 #Los dígitos consecutivos se repiten 4 o más veces → Inválido
        # 5122-2368-7954 - 3214 #Se utilizan separadores distintos de '-' → Inválido
        # 44244x4424442444 #Contiene caracteres que no son dígitos → Inválido
        # 0525362587961578 #No empieza con 4, 5 o 6 → Inválido.
        self.regex_card_pattern = re.compile(r"^"
                                  r"(?!.*(\d)(-?\1){3})"
                                  r"[456]"  #No empieza con 4, 5 o 6 → Inválido.
                                  r"\d{3}"  #Contiene caracteres que no son dígitos → Inválido
                                  r"(?:-?\d{4}){3}"
                                  r"$")
        self.regex_email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        self.regex_cuit_pattern = re.compile(\b(20|23|24|27|30|33|34)(\D)?[0-9]{8}(\D)?[0-9])


    def validartarjeta(self, nrotarjeta):
        return not (self.regex_card_pattern.fullmatch(nrotarjeta) is None)

    def validaremail(self, email):
        return not (self.regex_email_pattern.fullmatch(email) is None)