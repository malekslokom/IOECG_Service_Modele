
class Config:
    PASSWORD = '0000'  
    SQLALCHEMY_PORT= '5432'  
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:' + PASSWORD + '@localhost:'+SQLALCHEMY_PORT+'/models'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVICE_PORT = 5001