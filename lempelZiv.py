import unittest

#naivly compress strings over the given alphabet
def lzCompress(s, alph):
	n = len(s)
	dic = {alph[i] : i+1 for i in range(0, len(alph))}
	res = ""
	if n > 0:
		p = s[0]
		for i in range(1, n):
			if not p+s[i] in dic:
				dic[p+s[i]] = len(dic)+1
				res += str(dic[p])
				p = s[i]
			else:
				p = p+s[i]

		res += str(dic[p])
	return res

def lzDecompress(comp, alph):
	c = [int(ch) for ch in comp]
	n = len(c)	
	dic = alph
	res = ""
	if n > 0:
		res += dic[c[0]-1]
		for i in range(1, len(c)):
			if c[i] <= len(dic):
				dic.append(dic[c[i-1]-1]+dic[c[i]-1][0])
			else:
				dic.append(dic[c[i-1]-1]+dic[c[i-1]-1][0])
			res += str(dic[c[i]-1])
	return res




class LempelZivTest(unittest.TestCase):
	def testLzCompress1(self):
		self.assertEquals("125131468", lzCompress("abracadabra", ['a','b','c','d','r']))
	def testLzCompress2(self):
		self.assertEquals("1244373", lzCompress("abababcabcc", ['a','b','c']))

	def testLzDeCompress1(self):
		self.assertEquals("abracadabra", lzDecompress("125131468", ['a','b','c','d','r']))
	def testLzDeCompress2(self):
		self.assertEquals("abababcabcc", lzDecompress("1244373", ['a','b','c']))
	def testLzDeCompress2(self):
		self.assertEquals("abaabaacbaabaabaacbaccc", lzDecompress([1, 2, 1, 4, 6, 3, 5, 7, 11, 9, 1, 3, 15], ['a','b','c']))



if __name__ == "__main__":
	unittest.main()