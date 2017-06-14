import redis
import unittest


class Ranking:
    def __init__(self):
        # protected mode off:
        #   CONFIG SET protected-mode no
        self._redis = redis.StrictRedis(host='saki.ninja', port=6379, db=0)
        self._redis.delete('ranking')

    def set_score(self, user_id, score):
        self._redis.zadd('ranking', score, user_id)

    def get_ranking(self, user_id):
        return self._redis.zrevrank('ranking', user_id)

    def get_ranking_top3(self):
        return [v.decode("utf-8") for v in self._redis.zrevrange('ranking', 0, 2)]


class RankingTest(unittest.TestCase):
    def testRanking(self):
        r = Ranking()
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


if __name__ == '__main__':
    unittest.main()
