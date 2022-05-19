def extract_tuples_pro(e,prop=("gene","pos","refNt")):
    """
    Must extract the desired parameters from the exome "e"
    in a list of tuples(default triples)
    """
    return e[list(prop)].values


def extract_tuples(e,prop=("gene","pos","refNt")):
    """
    Must extract the desired parameters from the exome "e"
    in a list of tuples(default triples)
    """
    r={}
    for i in range(len(prop)):
        r[prop[i]]=tuple(e[prop[i]])

    # rr[0]=("a_gen","a_pos","a_refNt")
    rr=[]
    for i in range(len(r[prop[0]])):
        rri=[r[j][i] for j in prop]#list comprehension
        rr.append(rri)           

    return r,rr


def subset(Ax,Bx,Cx,prop=("gene","pos","refNt")):
    """
    Must obtain the different subsets to contruct the Venn
    diagram.
    A and B: parents
    C: Child
    """
    A=frozenset(tuple(m) for m in extract_tuples_pro(Ax,prop)) #as set 1
    B=frozenset(tuple(m) for m in extract_tuples_pro(Bx,prop)) #as set 2
    C=frozenset(tuple(m) for m in extract_tuples_pro(Cx,prop)) #as set 3

    a=((A-B)-C)             #001
    b=((B-A)-C)             #010
    c=((C-B)-A)             #100
    y=((A&C)-B)             #101
    w=((A&B)-C)             #011
    x=((B&C)-A)             #110
    z=A.intersection(B,C)   #111

    combinations=[a,b,w,c,y,x,z]
    merge_vector=[bin(i)[2:].zfill(3) for i in range (1,2**3)]
    r=dict(zip(merge_vector,combinations))
    return r

def venn(r,Vtags=('A','B','C')):
    plt.figure(figsize=(10,8))
    #(Abc, aBc, ABc, abC, AbC, aBC, ABC) <- format of venn3
    # str[::-1] is used to flip strings
    mv=[bin(i)[2:].zfill(3) for i in range (1,2**3)]
    tags=['a','b','w','c','y','x','z']
    q=dict(zip(mv,tags))
    v=venn3([len(r[i]) for i in mv],Vtags)
    for i in mv:
        t=v.get_label_by_id(i).get_text()
        v.get_label_by_id(i).set_text(f"id:{i}\n{q[i[::-1]]}\n{t}")
    plt.show()
    return None
