#_author_ : duany_000
#_date_ : 2018/2/7
import redis

# 注释掉bind 127.0.0.1;在地址前面加个#，或者改为0.0.0.0；
# 设置密码，在#requirepass foobared去掉#号变requirepass foobared;foobared是密码;
# conn_red = redis.Redis(host='192.168.0.103',port=6379,db=0,password='rootroot')


"""
管道：
redis-py默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，
如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，
并且默认情况下一次pipline 是原子性操作。
"""
pool = redis.ConnectionPool(host='192.168.0.103',port=6379,db=0,password='rootroot')

r = redis.Redis(connection_pool=pool)

pipe = r.pipeline(transaction=True)

pipe.set('class', 'python')
pipe.set('teacher', 'rose')

pipe.execute()

