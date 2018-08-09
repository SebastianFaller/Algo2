import unittest
import random

def multiKeyQS(strings):
	return mkQs(strings, 0)

def mkQs(strings, l):
	if len(strings) <= 1:
		return strings
	sShort, sLong = [], []
	for s in strings:
		if len(s) == l:
			sShort.append(s)
		else:
			sLong.append(s)
	pivot = random.randrange(0, len(sLong))
	p = sLong[pivot]
	a = mkQs([s for s in sLong if s[l] < p[l]], l)
	b = mkQs([s for s in sLong if s[l] == p[l]], l+1)
	c = mkQs([s for s in sLong if s[l] > p[l]], l)
	return sShort + a + b + c
	

class TestMkQs(unittest.TestCase):
	def testMkQsA(self):
		self.assertEquals(multiKeyQS(["ca", "accc", "a", "", "aa", "aba", "bb", "uuu"]), ["", "a", "aa", "aba", "accc", "bb", "ca", "uuu"])
	def testMkQsB(self):
		self.assertEquals(multiKeyQS(["sortieren", "sortiererin", "sortiermaschine", "sortiert", "sortierung", "sortenschutz", "sortenverzeichnis"]), 
			["sortenschutz", "sortenverzeichnis" ,"sortieren", "sortiererin", "sortiermaschine", "sortiert", "sortierung"])
		

if __name__ == "__main__":
	unittest.main()