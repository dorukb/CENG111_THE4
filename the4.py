def children(tree): #fundamentals for tree traversal..
    return tree[2:]

def force(tree):
    return tree[1]

def name(tree):
    return tree[0]

def is_leaf(tree):
    return len(children(tree)) == 0


def max_height(tree):#helper for constraint_2
    if is_leaf(tree):
        return 0
    else:
        maximum = -1
        for child in children(tree):
            curr = 1 + max_height(child)
            if curr > maximum :
                maximum = curr
        return maximum

def constraint_1(tree,h):
    allchild = h
    # check whether any child is stronger than its parent
    for child in allchild:
        if force(tree) < force(child):
            temp = (tree[0],tree[1])
            (tree[0],tree[1]) =(child[0],child[1])
            (child[0],child[1]) = temp
    return tree



def helper_1(tree,childs):#helper for constraint_1
    if children(tree) == [] and childs == []:
        return
    else:
        constraint_1(tree,childs)
        count = len(tree[2:])
        if not childs:
            lowers = []
            for x in range(0,count):
                lowers += children(tree[2:][x])
            for x in range(0,count):
                helper_1(tree[2:][x],lowers)
        else:
            newchilds = []
            for sub_tree in childs:
               newchilds += children(sub_tree)
            for x in range(0,count):
                helper_1(tree[2:][x],newchilds)



def help_ben_solo(tree,cons): #main function that calls the others.
    helper_1(tree,[])
    retired= constraint_2(tree,cons)
    return tree,retired



def constraint_2(tree,threshold):#helper and organizer for constraint 2
    height = max_height(tree)+1
    T = threshold
    retired = []
    copy = tree[::]
    curr_path = []
    curr_path.append(tree)
    m_h = height
    retired = traversal(tree,height,T,copy,retired,curr_path,m_h)
    return retired

     
def traversal(tree,h,t,memory,retired,curr_path,m_h):
    if h <= t and h > 0:
        if len(tree)>0:
            for child in children(tree):
                if children(child):
                    for child in children(tree):
                        curr_path.append(child)
                        traversal(child,h-1,t,tree,retired,curr_path,m_h)
                        curr_path.pop()
                    traversal(tree,h-1,t,tree,retired,curr_path,m_h)
                added = []
                border = m_h - t
                for comms in curr_path[0:border][::-1]: #find the force limit for every commander on the path
                    currentpower = 0
                    limit = force(comms)
                    print name(comms)
                    for lower in children(comms):
                        currentpower += force(lower)
                    f_o_c = force(child)
                    if f_o_c+currentpower <= limit:#move if possible
                        currentpower+=f_o_c
                        if child not in comms:
                            comms.append(child)
                            added.append(child)
                        if child in tree:
                            tree.remove(child)
                        break
                else: #retire if not possible
                    if child in tree:
                        retired.append(name(child))
                        tree.remove(child)
        return retired
    else:
        for child in children(tree):
            curr_path.append(child)
            traversal(child,h-1,t,tree,retired,curr_path,m_h)
            curr_path.pop()
        return retired








