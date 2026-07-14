class User:
    def __init__(self, user_id, username):
        self.username = username
        self._user_id = user_id

    @property
    def user_id(self):
        return self._user_id
    

u = User(99, "Ifeoma")
print(u.username)
print(u.user_id)
u.user_id = 100
print(u.user_id)