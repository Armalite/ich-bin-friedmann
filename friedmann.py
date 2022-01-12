from itertools import*

r={};k=product;m=map

q=lambda n,h=1:["("+i+c+j+")"for(i,j),c in k(chain(*[k(*m(q,f))for f in sum(([(x[:q],x[q:])for q in range(1,len(x))]for x in m("".join,permutations(n))),[])]),list("+-*/^")+[""]*h)]if 1<len(n)else[n]*h
minval,maxval=m(int,m(input,"nm"))

for i,j in chain(*[k(q(str(n),0),[n])for n in range(minval,maxval+1)]):
    try:exec("if eval(%r)==j:r[j]=i"%i.replace("^","**"))
    except:0

print(len(r))
for j,i in r.items():print(i,j)