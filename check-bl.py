import sys
import genutils3


for i in range(1,39):
    n = 'chr' + str(i)
    cmd = 'ls -lh blatRun/%s-%s.psl' % (n,n)
#    print(cmd)
    genutils3.runCMD(cmd)