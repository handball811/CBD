from Datasource.entities import Encrypted, DataInformation
from typing import List
import random

class SentenceGenerator:
	def __init__(self):
		self._hard_sample = [
			"とうきょうはにほんのしゅとです",
			"きのうのてすとではなんとかあかてんをかいひすることができました",
		]
		self._rot_rule = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽゃゅょっぁぃぅぇぉ" 
		self._rot_len = len(self._rot_rule)
	def generate(self, t :str) -> List[Encrypted]:
		"""
		tには生成タイプを指定できる
		"""
		gen = []
		if t == "sample":
			gen = self._hard_sample
		else:
			raise RuntimeError("generate type {} not known.".format(t))

		for g in gen:
			n = random.randint(1,self._rot_len-1)
			enc = "".join([self._rot_rule[(self._rot_rule.find(a)+n)%self._rot_len] for a in g])
			rule = DataInformation(rot_num=n)
			yield Encrypted(sentence=enc, info=rule)

