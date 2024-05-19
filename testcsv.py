from src.application.security import SecurityPWD



pwd_org = "antoniocampos2024"
pwd_hashed = SecurityPWD.has_password(pwd_org)
with open("passwords.key", "w") as file:
    file.write(f"{pwd_org} - {pwd_hashed}")
