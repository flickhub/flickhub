

def list_duplicates_of(seq):
    test_list=seq
    res = [] 
    oc_set = set() 
    for idx, val in enumerate(test_list): 
        if val not in oc_set: 
            oc_set.add(val)          
        else: 
            res.append(idx) 
    
    return res
