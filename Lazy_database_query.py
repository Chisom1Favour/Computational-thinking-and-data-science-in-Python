class User(models.Model):
    username = models.CharField(max_length=100)
    @property
    def post_count(self):       # Runs SQL only when accessed
        return self.posts.count()        # SELECT COUNT(*) FROM users WHERE user_id=...
    @property
    def is_admin(self):         # Computed from other fields
        return self.groups.filter(name='Admin').exists()
    

u = User.objects.get(id=1)
print(u.username)               # instant - from initial query
print(u.post_count)             # now runs second query, not before
