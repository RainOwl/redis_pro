#_author_ : duany_000
#_date_ : 2018/2/7
from redis_help import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()

while True:
    msg = redis_sub.parse_response()
    print(msg)
