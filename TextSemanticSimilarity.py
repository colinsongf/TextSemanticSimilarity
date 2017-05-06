from SOCPMI import SemanticSimilarity
from Cleaner import clean
from Auxiliary import Commonwords, DisplayMatrixform
from SimilarityCount import SimilarityCount
from SyntacticSimilarity import SyntacticSimilarity

s1="The world knows it has lost a heroic champion of justice and freedom"
s2="The earth recognizes the loss of a valliant champoin of independence and justice"


#Removing punctuations, stopwords and storing important words in a list
sent1=clean(s1)
sent2=clean(s2)
m=len(sent1)
n=len(sent2)
#Getting the list of common words and the removal of those words from the original list
common,s1,s2=Commonwords(sent1,sent2)


synmat={}
if len(s2)<len(s1):
	for i in s2:
		synmat[i]={}
		for j in s1:
			synmat[i][j]=SyntacticSimilarity(i,j)
else:
	for i in s1:
		synmat[i]={}
		for j in s2:
			synmat[i][j]=SyntacticSimilarity(i,j)


semmat={}
a=2; 
delta=0.7	#Constant depends on the size of the training corpus
gamma =3 	#Defines the weight given to semantic measure. Should be greater than 1.
if len(s2)<len(s1):
	for i in s2:
		semmat[i]={}
		for j in s1:
			semmat[i][j]=SemanticSimilarity(i,j,a,delta,gamma)
else:
	for i in s1:
		semmat[i]={}
		for j in s2:
			semmat[i][j]=SemanticSimilarity(i,j,a,delta,gamma)

DisplayMatrixform(synmat,s1,s2)
DisplayMatrixform(semmat,s1,s2)

primat={}
if len(s2)<len(s1):
	for i in s2:
		primat[i]={}
		for j in s1:
			primat[i][j]=0.3*synmat[i][j]+ 0.7*semmat[i][j]
else:
	for i in s1:
		primat[i]={}
		for j in s2:
			primat[i][j]=0.3*synmat[i][j]+0.7*semmat[i][j]



DisplayMatrixform(primat,s1,s2)

out1=[]
out2=[]
rhosum= SimilarityCount(primat,s1,s2,out1,out2)

print("Sumattion of maximum terms: ",rhosum)

sentencesimilarity= (len(common)+rhosum)*(m+n)/(2*m*n)
print("Sentence Similarity Measure: ",sentencesimilarity)

