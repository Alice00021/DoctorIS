class UserState:
    def __init__(self):
        self.is_user_logged_in = False

    def login(self):
        self.is_user_logged_in = True

    def logout(self):
        self.is_user_logged_in = False
        
user_state = UserState()