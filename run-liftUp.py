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
for d in [params['oldChromsDir'],params['newChromsDir'],params['chunksDir'],params['liftDir'],params['blatOutDir'],params['pslDir'] ]:
   if os.path.isdir(d) is False:
       print('no dir',d)
       sys.exit()    
# check dirs


newFiles = glob.glob(params['chunksDir'] + '/*fa')
print('\nstart\n')
for nf in newFiles:
    newBaseName = nf.split('/')[-1].split('.')[0]
    
    pslFile = params['pslDir'] + newBaseName + '.psl'
    liftFile = params['liftDir'] + newBaseName + '.lft'
    blatFilePre = params['blatOutDir'] + newBaseName + '-*'
    
    cmd = 'liftUp -pslQ %s %s warn %s' % (pslFile,liftFile,blatFilePre)
    print(cmd)
    genutils3.runCMD(cmd)


