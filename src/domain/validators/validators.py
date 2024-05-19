"""validators for password"""



def validate(password: str) -> bool:
    password_stripped = password.strip()
    
    if password_stripped != "" and len(password_stripped) >= 8:
        return True
    return False
