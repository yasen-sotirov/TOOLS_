from models.comment import Comment
from models.constants.user_role import UserRole
import re

class User:
    USERNAME_LEN_MIN = 2
    USERNAME_LEN_MAX = 20
    USERNAME_LEN_ERR = f'Username must be between {USERNAME_LEN_MIN} and {USERNAME_LEN_MAX} characters long!'
    USERNAME_INVALID_SYMBOLS = 'Username contains invalid symbols!'

    PASSWORD_LEN_MIN = 5
    PASSWORD_LEN_MAX = 30
    PASSWORD_LEN_ERR = f'Password must be between {PASSWORD_LEN_MIN} and {PASSWORD_LEN_MAX} characters long!'
    PASSWORD_INVALID_SYMBOLS = 'Password contains invalid symbols!'

    LASTNAME_LEN_MIN = 2
    LASTNAME_LEN_MAX = 20
    LASTNAME_LEN_ERR = f'Lastname must be between {LASTNAME_LEN_MIN} and {LASTNAME_LEN_MAX} characters long!'

    FIRSTNAME_LEN_MIN = 2
    FIRSTNAME_LEN_MAX = 20
    FIRSTNAME_LEN_ERR = f'Firstname must be between {FIRSTNAME_LEN_MIN} and {FIRSTNAME_LEN_MAX} characters long!'

    NORMAL_ROLE_VEHICLE_LIMIT = 5

    NORMAL_USER_LIMIT_REACHED_ERR = f'You are not VIP and cannot add more than {NORMAL_ROLE_VEHICLE_LIMIT} vehicles!'
    ADMIN_CANNOT_ADD_VEHICLES_ERR = 'You are an admin and therefore cannot add vehicles!'
    YOU_ARE_NOT_THE_AUTHOR = 'You are not the author of the comment you are trying to remove!'
    THE_VEHICLE_DOES_NOT_EXIT = 'The vehicle does not exist!'

    # Todo: Finish the implementation
    # Names of methods/attributes should be exactly match those in the README file




    def __init__(self, username: str, firstname:str, 
                 lastname:str, password:str, user_role:UserRole):
        
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.user_role = user_role
        self.is_admin = False
        self.vehicles = tuple()


    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if len(value) < self.USERNAME_LEN_MIN or len(value) > self.USERNAME_LEN_MAX:
            raise ValueError(self.USERNAME_LEN_ERR)
        if not value.isalnum():
            raise ValueError(self.USERNAME_INVALID_SYMBOLS)
        self._username = value    


    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        if len(value) < self.FIRSTNAME_LEN_MIN or len(value) > self.FIRSTNAME_LEN_MAX:
            raise ValueError(self.FIRSTNAME_LEN_ERR)
        self._firstname = value
    

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, value):
        if len(value) < self.LASTNAME_LEN_MIN or len(value) > self.LASTNAME_LEN_MAX:
            raise ValueError(self.LASTNAME_LEN_ERR)
        self._lastname = value


    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        if len(value) < self.PASSWORD_LEN_MIN or len(value) > self.PASSWORD_LEN_MAX:
            raise ValueError(self.PASSWORD_LEN_ERR)
        
        pattern = r"[^a-zA-Z0-9@*-_]"
        unwanted_char = re.findall(pattern, value)
        
        if len(unwanted_char) > 0:
            raise ValueError(self.PASSWORD_INVALID_SYMBOLS)
        self._password = value





# user_1 = User("StamOFF", "Stamat", "Ivanov", "12345678", "Normal")

# print(user_1.first_name)
# print(user_1.last_name)
# print(user_1.is_admin)
# print(user_1.password)
# print(user_1.username)
# print(user_1.vehicle_list)