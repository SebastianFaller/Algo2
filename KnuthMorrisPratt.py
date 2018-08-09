import unittest

def match(s, p):
	b = border(p)
	i, j = 0, 0
	while i <= len(s)-len(p)-1:
		while j < len(p) and s[i+j] == p[j]:
			j+=1
		if j >= len(p):
				return i
		i, j = i + j - b[j], 0
	
		
def border(p):
	b = [0 for i in range(0,len(p))]
	i = -1
	b[0] = i
	for j in range(1, len(p)):
		while i >= 0 and p[i] != p[j-1]:
			i = b[i]
		i+=1
		b[j] = i 
	return b

class TestKMP(unittest.TestCase):
	def testBorderA(self):
		self.assertEqual(border("ababcabab"), [-1,0,0,1,2,0,1,2,3])
	def testBorderB(self):
		#Seems to be a different border array than we did in lecture. Source: Wikipedia
		#self.assertEqual(border("participate in parachute"), [-1,0,0,0,0,0,0,-1,0,2,0,0,0,0,0,-1,0,0,3,0,0,0,0,0,0])
		self.assertEqual(border("abacababc"), [-1,0,0,1,0,1,2,3,2])
	def testKmpA(self):
		self.assertEqual(match("abaabcabcaa", "abc"), 3)
	def testKmpB(self):
		self.assertEqual(match("This is a pattern to match", "pattern"), 10)

if __name__ == '__main__':
	unittest.main()