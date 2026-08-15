class User:
    def __init__(self, user_id, username):
        self._user_id = user_id
        self.username = username
    @property
    def user_id(self):
        return self._user_id
    
u = User(20, 'Nenye')
print(u.user_id)
print(u.username)