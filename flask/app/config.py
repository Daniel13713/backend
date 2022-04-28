class Config:
    SECRET_KEY = "dev"
    """Connection to docker"""
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "1375"
    MYSQL_DB = "appflask"
    MYSQL_HOST = "172.17.0.2" #"127.0.0.1"
    MYSQL_PORT = 3306 #36060

    """Connection to local wsl
    MYSQL_USER = "daniel"
    MYSQL_PASSWORD = "1375"
    MYSQL_DB = "appflask"
    MYSQL_HOST = "localhost" #"127.0.0.1"
    MYSQL_PORT = 3306 """
