from locust import HttpUser, task

class TestSuite(HttpUser):
    @task
    def test_predict_data(self):
        data = {
            "CHAS":
            {
                "0":0
            },
            "RM":{
                "0":6.575
            },
            "TAX":{
                "0":296.0
            },
            "PTRATIO":{
                "0":15.3
            },
            "B":{
                "0":396.9
            },
            "LSTAT":{
                "0":4.98
            }
        }
        headers = {"Content-type": "application/json"}
        self.client.post("/predict", headers=headers, json=data)