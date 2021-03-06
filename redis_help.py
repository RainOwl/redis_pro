#_author_ : duany_000
#_date_ : 2018/2/7
import redis


class RedisHelper:

    def __init__(self):
        self.__conn = redis.Redis(host='192.168.0.103',port=6379,db=0,password='rootroot')
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'

    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub

