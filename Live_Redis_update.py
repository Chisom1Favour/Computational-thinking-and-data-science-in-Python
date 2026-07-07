class AsyncResult:
    def __init__(self, task_id):
        self.task_id = task_id

    @property
    def status(self):
        return redis_client.hget(f"task: {self.task_id}", "status")
    
    @property
    def ready(self):
        return self.status in ['SUCCESS', 'FAILURE']
    

result = AsyncResult('abc-123')
while not result.ready:  #polls Redis on each loop
    time.sleep(1)

    