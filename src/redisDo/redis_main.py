# coding=utf-8
import redis

conn = redis.Redis()
print(conn.get('key'))


