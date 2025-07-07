import os

class Config:
    TARGET_URL = os.getenv("TARGET_URL", "erp.svmoutlet.com")
