import requests, json, redis

class Search:

  headers = {
    'content-type': 'application/json',
    'client_id': '2d6a8ffd-e4ad-3940-9407-cba3e2dd7528'
  }
  cache = {}

  def __init__(self, url):
    self.url = url

  def exec_query(self, number):

    payload = """
      query OneBin {
        bin(number: "%d") {
          services {
            name,
            description
          }
        }
      }
    """ % number

    response = requests.post(self.url, data=json.dumps({"query": payload}), headers=self.headers)

    return response.json()

  def load_cache(self):
    r = redis.Redis(
      host='database',
      port=6379,
    )

    keys = r.keys()

    for k in keys:
      self.cache[int(k.decode())] = r.get(k)

    r.close()

  def set_cache(self, key, value):
    r = redis.Redis(
      host='database',
      port=6379,
    )

    r.set(key, json.dumps(value))
    r.close()

    self.cache[key] = value

  def run(self, number):
    self.load_cache()

    if number in self.cache.keys():
      return self.cache.get(number)

    data = self.exec_query(number)
    self.set_cache(number, data)

    return data