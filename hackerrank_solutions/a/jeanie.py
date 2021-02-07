n,k=map(int, raw_input().split())

a=map(int, raw_input().split())
g=[[] for x in range(n+1)]
need=[0 for x in range(n+1)]
savniche=[0 for x in range(n+1)]
for val in a: need[val]=1

maxd=0
tsum=0
end=0
def call(last, u,dis):
    global tsum
    global maxd
    global end
    if need[u]:
        if dis>=maxd:
            maxd=dis
            end=u

    niche=need[u]
    for tup in g[u]:
        v,d=tup[0],tup[1]
        if v==last: continue
        niche=niche+call(u,v,dis+d)
        if savniche[v]==0 or savniche[v]==k: continue
        tsum=tsum+d


    savniche[u]=niche
    return niche

for _ in range(n-1):
    u,v,d=map(int, raw_input().split())
    g[u].append([v,d])
    g[v].append([u,d])


call(0,a[0],0)
tsum=0
maxd=0
call(-1,end,0)

print (tsum*2)-maxd