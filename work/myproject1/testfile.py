from main import readf, writef
from pip._vendor.distlib.compat import raw_input
from test.test_enum import Question
terms={'verb':'verb','noun':'noun','ques':'ques'}
lookup={terms['verb']:"",terms['noun']:"",terms['ques']:""}
lookup[terms['verb']],lookup[terms['noun']],lookup[terms['ques']]=readf("verb"),readf("noun"),readf("ques")
#print(verb,noun,ques)
class check:
    def __init__(self,inp):
        self.inp=inp
        global dict1
        dict1={}
    
    def cal(self):
        a=self.inp.split()
        for b in a:
            print (b)
    def ckhnoun(self,a):
        if a in lookup['noun']:
            pass
    def updatedict(self,key,value):
        dict1[key]=value
            

inp=raw_input("enter the question")
ob=check(inp)
ob.updatedict(terms['ques'], inp)
print(dict1)


    