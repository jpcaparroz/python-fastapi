from passlib.context import CryptContext


CRIPTO = CryptContext(schemes=['bcrypt'])


def verify_password(password: str, password_hash: str) -> bool:
    """
    Verify if password is correct

    Args:
        password (str): user password
        password_hash (str): password hash

    Returns:
        bool:
    """
    return CRIPTO.verify(password, password_hash)


def generate_hash(password: str) -> str:
    """
    Generate password hash
    
    Args:
        password (str): user password

    Returns:
        str: password hash
    """
    return CRIPTO.hash(password)

