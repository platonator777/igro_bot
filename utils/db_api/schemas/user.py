from sqlalchemy import BigInteger, Column, String, sql
from utils.db_api.db_gino import TimedBaseModel

class User(TimedBaseModel):
    __tablename__ = "users"
    user_id = Column(BigInteger, primary_key = True)
    first_name = Column(String(200))
    balance = Column(BigInteger, default= 1000)
    stake = Column(BigInteger, default = 1)
    win_money = Column(BigInteger, default = 0)
    lose_money = Column(BigInteger, default = 0)
    wins = Column(BigInteger, default = 0)
    loses = Column(BigInteger, default = 0)
    draws = Column(BigInteger,default = 0)

    query: sql.select

