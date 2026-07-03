class User:
    def __init__(self, username):
        self.username = username
        self._posts = []
        self._posts_count_cache = None

    def add_post(self, post):
        self._posts.append(post)
        self._posts_count_cache = None
    @property
    def post_count(self):
        if self._post_count_cache is None:
            print("Counting posts from DB....")
            self._posts_count_cache = len(self._posts)
        return self._posts_count_cache
    
u = User("ada")
print(u.post_count)
print(u.post_count)
u.add_post("Hello")
print(u.post_count)

