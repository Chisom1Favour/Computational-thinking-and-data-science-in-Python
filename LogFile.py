class LogFile:
    def __init__(self, path):
        self.path = path
        self._error_count = None

    @property
    def error_count(self):
        if self._error_count is None:
            print('Scanning file....')
            with open(self.path) as f:
                self._error_count = sum(1 for line in f if "ERROR" in line)
        return self._error_count
    
log = LogFile("huge.log")
print("Created")
print(log.error_count)
print(log.error_count)