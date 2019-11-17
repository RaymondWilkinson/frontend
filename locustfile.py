from locust import HttpLocust, TaskSet, between

def index(l):
    l.client.get("/")

class UserBehavior(TaskSet):
    tasks = {index: 1}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(1.0, 2.0)
