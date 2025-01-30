from typing import Optional
from datetime import datetime
from System import Object  # Import the System.Object base class


class User(Object):
    """
    Represents a user with attributes such as UserName, Email, and Role,
    including getter and setter properties.
    """

    def __init__(self):
        """
        Default constructor to initialize all properties to None or default values.
        """
        self.UserId: Optional[int] = None
        self.UserName: Optional[str] = None
        self.FirstName: Optional[str] = None
        self.LastName: Optional[str] = None
        self.Email: Optional[str] = None
        self.PasswordHash: Optional[str] = None
        self.Role: Optional[str] = None
        self.CreatedAt: Optional[datetime] = None
        self.IsActive: int = 0
        self.Token: Optional[str] = None

    # UserId Property (Getter and Setter)
    @property
    def UserId(self) -> Optional[int]:
        return self.UserId

    @UserId.setter
    def UserId(self, value: int):
        self._UserId = value

    # UserName Property
    @property
    def UserName(self) -> Optional[str]:
        return self.UserName

    @UserName.setter
    def UserName(self, value: str):
        self.UserName = value

    # FirstName Property
    @property
    def FirstName(self) -> Optional[str]:
        return self.FirstName

    @FirstName.setter
    def FirstName(self, value: str):
        self.FirstName = value

    # LastName Property
    @property
    def LastName(self) -> Optional[str]:
        return self.LastName

    @LastName.setter
    def LastName(self, value: str):
        self.LastName = value

    # Email Property
    @property
    def Email(self) -> Optional[str]:
        return self.Email

    @Email.setter
    def Email(self, value: str):
        self.Email = value

    # PasswordHash Property
    @property
    def PasswordHash(self) -> Optional[str]:
        return self.PasswordHash

    @PasswordHash.setter
    def PasswordHash(self, value: str):
        self.PasswordHash = value

    # Role Property
    @property
    def Role(self) -> Optional[str]:
        return self.Role

    @Role.setter
    def Role(self, value: str):
        self.Role = value

    # CreatedAt Property
    @property
    def CreatedAt(self) -> Optional[datetime]:
        return self.CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, value: datetime):
        self.CreatedAt = value

    # IsActive Property
    @property
    def IsActive(self) -> int:
        return self._IsActive

    @IsActive.setter
    def IsActive(self, value: int):
        self.IsActive = value

    # Token Property
    @property
    def Token(self) -> Optional[str]:
        return self.Token

    @Token.setter
    def Token(self, value: str):
        self.Token = value

    def __repr__(self):
        return (
            f"User(UserId={self.UserId}, UserName={self.UserName}, FirstName={self.FirstName}, "
            f"LastName={self.LastName}, Email={self.Email}, Role={self.Role}, "
            f"CreatedAt={self.CreatedAt}, IsActive={self.IsActive}, Token={self.Token})"
        )
