from rolepermissions.roles import AbstractUserRole


class Desenvolvedor(AbstractUserRole):
    available_permissions = {
        'addProducts': True,
        'discount': True,
        'addSeller': True,
        'deleteAccount': True,
        'sell': True,
    }

class Gerente(AbstractUserRole):
    available_permissions = {
        'addProducts': True,
        'discount': True,
        'addSeller': True,
        'deleteAccount': True,
    }

class Vendedor(AbstractUserRole):
    available_permissions = {
        'sell': True,
    }