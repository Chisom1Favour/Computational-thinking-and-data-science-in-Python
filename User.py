class User:
    def __init__(self, username):
        self.username = username
        self._posts = []
        self._post_count_cache = None

    def add_post(self, post):
        self._posts_append(post)
        self._post_count_cache = None

    @property
    def post_count(self):
        if self._post_count_cache is None:
            print("Counting posts from DB....")
            self._post_count_cache = len(self._posts)
        return self._post_count_cache
    
u = User()
