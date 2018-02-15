import redis
import unittest
import time


class Ranking:
    def __init__(self, key):
        # protected mode off:
        #   CONFIG SET protected-mode no
        self._redis = redis.StrictRedis(host='saki.ninja', port=6379, db=0)
        self._key = key

    def clear(self):
        self._redis.delete(self._key)

    def expire(self, time):
        self._redis.expire(self._key, time)

    def set_score(self, user_id, score):
        self._redis.zadd(self._key, score, user_id)

    def get_ranking(self, user_id):
        return self._redis.zrevrank(self._key, user_id)

    def get_ranking_top3(self):
        return [v.decode("utf-8") for v in self._redis.zrevrange(self._key, 0, 2)]


class RankingTest(unittest.TestCase):
    def testRanking(self):
        r = Ranking('moe')
        r.clear()

        self.assertEqual(r.get_ranking('nanoha'), None)
        self.assertEqual(r.get_ranking_top3(), [])

        r.set_score('nanoha', 10)
        self.assertEqual(r.get_ranking('nanoha'), 0)
        self.assertEqual(r.get_ranking_top3(), ['nanoha'])

        r.set_score('saki', 0)
        r.set_score('sonico', 20)
        r.set_score('reisen', 30)
        self.assertEqual(r.get_ranking('nanoha'), 2)
        self.assertEqual(r.get_ranking('saki'), 3)
        self.assertEqual(r.get_ranking('sonico'), 1)
        self.assertEqual(r.get_ranking('reisen'), 0)
        self.assertEqual(r.get_ranking_top3(), ['reisen', 'sonico', 'nanoha'])

        r.expire(1)
        time.sleep(1)
        self.assertEqual(r.get_ranking_top3(), [])


if __name__ == '__main__':
    unittest.main()
