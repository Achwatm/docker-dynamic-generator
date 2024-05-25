import json

class Job:

    def __init__(self):
        self._prepare_job()
    
    def _prepare_job(self):
        self.job = {
            "type": 'action',
            "method": 'newOrder',
            "integrator": 'eaa4012e-a787-40f4-9026-ed1847494c5c',
            "topics": [
            ],
            'data': {
                'test': 'test1'
            }
        }
        
    def add_topic(self, topic):
        self.job['topics'].insert(0, topic)
        
    def dump(self):
        return json.dumps(self.job)