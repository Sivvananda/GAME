import numpy as np
import nltk
import string
import random
from nltk.corpus import words
class game:
	def __init__(self,size=None):
		if not size:
			self.size=9
	def generate(self):
		self.a=np.chararray((3,3))
		p=self.a.flat
		for i in range(self.size):
			p[i]=random.choice((string.ascii_letters).lower())
		self.a=np.core.defchararray.decode(self.a,encoding="utf-8")
		self.alist=self.a.reshape(1,self.size)
	def op(self):
		self._w=words.words()
		middle=self.a[1][1]
		k=self.alist.flat
		R=nltk.FreqDist("".join(k[i] for i in range(self.size)))
		self._s=[w for w in self._w if len(w)>=3 and middle in w and nltk.FreqDist(w)<=R]
		self.diff=len(self._s)
	def score(self,l):
				sc=0
				for i in l:
					if i in self._s:
						if len(i)==9:sc+=20
						else:sc+=10
					else:continue
				print("YOUR FINAL SCORE IS:",sc) 
	def sta(self):
		print("##########################  Y O U R       A R R A Y  ##################################\n")
		print(self.a)
		userw=[]
		i=1
		print("-----------------------------------INSTRUCTIONS-------------------------------------\nenter words of length 'GREATER THAN 3' and which in include the 'MIDDLE LETTER'.\nRepeatition of one letter is not allowed (if same letter appears twice then treat them as different letter i.e each of the letters can appear once.\nFor each word of length between 3 and 8 including(3,8) gives you 10 points and a letter of length of 9 would give u a bonus of 20 points.\nQUIT THE GAME BY TYPING 0.\nREFRESH THE ARRAY BY TYPING 1.\nYOUR WORD(S):")
		if self.diff in range(20):print("DIFFICULTY: VERY HARD")
		elif self.diff in range(20,35):print("DIFFICULTY:  HARD")
		elif self.diff in range(35,65):print("DIFFICULTY:  MEDIUM")
		else:print("DIFFICULTY:EASY")
		while(9):
				text=input("%d:"%(i))
				if text=="0":break
				elif text=="1":self.refresh()
				else:
					userw.append(text)
					i+=1
		self.score(userw)
	def refresh(self):
		del(self)
		a=game()
		a.main()
	@staticmethod
	def main():
		a.generate()
		a.op()
		a.sta()
				
if __name__=="__main__":
	a=game()
	a.main()	
		
