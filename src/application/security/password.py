"""method for encrypt and descript password"""
import bcrypt

from fastapi import HTTPException


class SecurityPWD:
    @staticmethod
    def has_password(pwd: str) -> str:
        salt = bcrypt.gensalt()
        pwd_hashed = bcrypt.hashpw(pwd.encode("utf-8"), salt)

        return str(pwd_hashed)[2:-1]

    @staticmethod
    def check_password_hashed(pwd: str, pwd_hashed: str) -> bool:
        try:
            result = bcrypt.checkpw(pwd.encode("utf-8"), pwd_hashed.encode("utf-8"))
        except Exception as error:
            raise HTTPException(
                detail="invalid password encrypt format",
                status_code=400
            )
        return result

