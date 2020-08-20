import sys
import genutils3
import glob
import os

#write-blat-cmds.py
#blat NEW vs OLD


paramsFile = 'params-file.txt'


####INFO#######
params = genutils3.read_params(paramsFile)
print('Read params from %s' % paramsFile)

for p in params:
    print(p,params[p])
    


# check dirs
for d in [params['oldChromsDir'],params['newChromsDir'],params['chunksDir'],params['liftDir'],params['blatOutDir'] ]:
   if os.path.isdir(d) is False:
       print('no dir',d)
       sys.exit()    
# check dirs


newFiles = glob.glob(params['chunksDir'] + '/*fa')
oldFiles = glob.glob(params['oldChromsDir'] + '/*fa')

print('Found %i NEW FASTA' % len(newFiles))
print('Found %i OLD FASTA' % len(oldFiles))

outSame = open('blat.SAME.cmds','w')
outUnk = open('blat.UNK.cmds','w')
outRest = open('blat.REST.cmds','w')

for nf in newFiles:
    newBaseName = nf.split('/')[-1].split('.')[0]
    for of in oldFiles:
        oldBaseName = of.split('/')[-1].split('.')[0]
        outName = params['blatOutDir'] + newBaseName + '-' + oldBaseName + '.psl'
        
        cmd = 'blat %s %s -tileSize=11 -ooc=%s -minScore=100 -minIdentity=95 %s' % (of,nf,params['oldOOC'],outName)
        cmd += '\n'
        
        if 'chrUn' in oldBaseName:
            outUnk.write(cmd)
        elif oldBaseName == newBaseName:
            outSame.write(cmd)
        else:
            outRest.write(cmd)

outSame.close()
outUnk.close()
outRest.close()
