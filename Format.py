class User:
    def __init__(self, raw_name):
        self._raw_name = raw_name

    @property
    def username(self):
        return self._raw_name.strip().lower()
    @property
    def display_name(self):
        return self._raw_name.strip().title()
    @property
    def slug(self):
        return self._raw_name.strip().lower().replace(" ", "-")
    
    
u = User("  Ada Lovelace ")
print(u.username)
print(u.display_name)
print(u.slug)