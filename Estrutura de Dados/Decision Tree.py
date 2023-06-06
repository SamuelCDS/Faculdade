from math import log2

class Arvore(object):
	def __init__(self,valor=None,f=None):
		super(Arvore, self).__init__()
		self.filhos = f
		if type(valor)==list:
			self.filhos = valor
		self.valor = valor
		self.x = 0
		self.y = 0

	def __str__(self):
		if self.valor is None:
			return "[ xy: "+str((self.x,self.y))+" ]"
		return "[ "+str(self.valor)+", xy: "+str((self.x,self.y))+" ]"
	
	def addFilho(self,f):
		if self.filhos is None:
			self.filhos = [f]
		else:
			self.filhos.append(f)

	def largura(self,f=None):
		verts = [self]
		nexts = []
		i = 0
		while len(verts)!=0:
			v = verts.pop(0)
			# print "?:",out[i]
			if f==None:
				print i,v
			else:
				f(v,i)
			if(v.filhos!=None):
				nexts.extend(v.filhos)
			if len(verts)==0 and len(nexts)!=0:
				i+= 1
				verts = nexts
				nexts = []

	def preencherXY(T,level,scale,leftL):
		if T.filhos is None:
			T.x = leftL
			rootX = T.x
			rightL = T.x
			T.y = scale * level
			return (rootX,rightL)
		elif len(T.filhos) == 1:
			(rootX,rightL) = T.filhos[0].preencherXY(level+1,scale,leftL)
			T.x = rootX
			T.y = scale*level
			return (rootX,rightL)
		elif len(T.filhos) > 1:
			left = leftL
			for f in T.filhos:
				(rRootX,rightLim) = f.preencherXY(level+1,scale,left)
				left = rightLim+scale
			rootX = (T.filhos[0].x+rRootX)/2
			T.x = rootX
			T.y = scale*level
			return (rootX,rightLim)

def entropy(n):
    entropia = 0.0
    for i in range(n):
        entropia -= n*log2(n) 
