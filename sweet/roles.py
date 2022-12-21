from rolepermissions.roles import AbstractUserRole


class Desenvolvedor(AbstractUserRole):
    available_permissions = {
        'addProduct': True,
        'discount': True,
        'addSeller': True,
        'sell': True,
    }

class Gerente(AbstractUserRole):
    available_permissions = {
        'addProduct': True,
        'discount': True,
        'addSeller': True,
    }

class Vendedor(AbstractUserRole):
    available_permissions = {
        'sell': True,
    }