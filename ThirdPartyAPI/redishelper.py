import redis


def main():
    redis_uri = 'rediss://default:AVNS_8u6gdXeb93vDEKIcq58@ashishbaj-redis-ashishbaj-mysql.b.aivencloud.com:20543'
    uri = 'rediss://default:AVNS_8u6gdXeb93vDEKIcq58@ashishbaj-redis-ashishbaj-mysql.b.aivencloud.com:20543'
    redis_client = redis.from_url(redis_uri)

    redis_client.set('key', 'hello world')
    key = redis_client.get('key').decode('utf-8')

    print('The value of key is:', key)


if __name__ == '__main__':
    main()