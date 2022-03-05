import re

class Validaciones:
    def is_name(self, name):
        """ 
        valida que el nombre empieze con mayuscula
        """
        validacion = re.compile('^[A-Z]')

        return True if re.search(validacion, name) else False
    
    def is_email(self, email):
        """ 
        valida que el email es correcto 
        """

        validacion = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        return True if re.search(validacion, email) else False
    
    def is_gender(self, gender):
        """ 
        valida que el genero es masculino o femenino
        """

        m = "Male"
        f = "Female"

        return True if gender == m or gender == f else False
    
    def is_ip(self, ip):
        """ 
        valida que la ip sea correcta
        """
        validacion = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

        return True if re.search(validacion, ip) else False

            


