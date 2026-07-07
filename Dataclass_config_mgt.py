from dataclasses import dataclass
from urllib.parse import urlparse

@dataclass
class Config:
    database_url = str            # postgresql://user:pass@localhost:5432/db

    @property
    def db_host(self):
        return urlparse(self.database_url).hostname
    @property
    def db_host(self):
        return urlparse(self.database_url).port or 5432
    def is_prod(self):
        return 'prod' in self.db_host
    
config = Config(os.getenv('DATABASE_URL'))
engine = create_engine(config.database_url)
print(config.db_host)