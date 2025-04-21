#Union-Find
#用意するもの：parentリスト（ノードiの親を記録）、nodeリスト（ノードiが親である時、接続されているノード数を記録）
#UF(parent:リスト,node:リスト,m:ノード(u,v)の関係など（入力数）)
#find(x:親を求めたいノード,parent:リスト)

def find(x,parent):
    if parent[x]==x:
        return x
    else:
        parent[x] = find(parent[x],parent)
        return parent[x]

def UF(parent,node,m):
    ring = set()
    for i in range(m):
        a,c = input().split()#TODO:入力の更新
    
        num1 = int(a)
        num2 = int(c)
    
        pa = find(num1,parent)
        pb = find(num2,parent)
        #print(pa,pb)
    
        if pa==pb:
            ring.add(pa)
        else:
            if pa>pb:
                temp = pa
                pa = pb
                pb = temp
            parent[pb] = pa
            node[pa] += node[pb]
            node[pb] = 0
