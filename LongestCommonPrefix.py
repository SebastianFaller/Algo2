import unittest

#Builds inverse suffix array from given suffix array
def buildISA(sa):
	isa = [0 for i in range(0, len(sa))]
	for i in range(0, len(sa)):
		isa[sa[i]] = i
	return isa


#Builds a longest common prefix array from a given text with its suffix array
def buildLCPArray(t, sa):
	h = 0
	lcp = [0 for i in range(0, len(sa))]
	isa = buildISA(sa)
	for i in range (0, len(sa)):
		if isa[i] != 0:
			while i+h < len(t) and sa[isa[i]-1]+h < len(t) and t[i+h] == t[sa[isa[i]-1]+h]:
				h += 1
			lcp[isa[i]] = h
			h = max(0, h-1)
	return lcp


class TestLCPArray(unittest.TestCase):
	def testISA(self):
		self.assertEquals([3,2,5,1,4,0], buildISA([5,3,1,0,4,2]))

	def testLCPArray1(self):
		self.assertEquals([0,1,3,0,0,2], buildLCPArray("banana", [5, 3, 1, 0, 4, 2]))


if __name__ == "__main__":
	unittest.main()
