from locust import HttpUser, task


class ConsumerService(HttpUser):
    @task
    def consumer(self):
        self.client.get("/mock")
