class User:
    def __init__(self, user_id):
        self.user_id = user_id
    
    @property
    def posts(self):
        print(f"SELECT * FROM posts WHERE user_id = {self.user_id}")
        return db.query("SELECT * FROM posts WHERE user_id=?", self.user_id)

u = User(42)
for post in u.posts:
    print(post)