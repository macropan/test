import redis
import os

redis_host = os.environ['REDIS_HOST']
redis_pwd = os.environ['REDIS_PWD']
print(redis_host.split('.')[0])

login_access = '$1$A$'
login_refresh = '$1$R$'
guest_access = '$2$A$'
guest_refresh = '$2$R$'
login_access_cnt = 0
login_refresh_cnt = 0
guest_access_cnt = 0
guest_refresh_cnt = 0
others_cnt = 0

r = redis.Redis(host=redis_host, port=6380, ssl=True, password=redis_pwd)
keys = r.keys('*')
print("key count: {}".format(len(keys)))
for key in keys:
    key_str = key.decode("utf-8")
    if login_access in key_str:
        login_access_cnt += 1
    elif login_refresh in key_str:
        login_refresh_cnt += 1
    elif guest_access in key_str:
        guest_access_cnt += 1
    elif guest_refresh in key_str:
        guest_refresh_cnt += 1
    else:
        others_cnt += 1
print("login_access_cnt: {0}, login_refresh_cnt: {1}, guest_access_cnt: {2}, guest_refresh_cnt: {3}, others_cnt: {4}".format(login_access_cnt, login_refresh_cnt, guest_access_cnt, guest_refresh_cnt, others_cnt))
