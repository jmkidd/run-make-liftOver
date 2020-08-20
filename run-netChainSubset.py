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
    

dirsToCheck = ['oldChromsDir',
'newChromsDir',
'chunksDir',
'liftDir',
'blatOutDir',
'pslDir',
'chainDir',
'chainRunDir',
'chainRawDir',
'netDir',
'overDir']

for d in dirsToCheck:
    if os.path.isdir(params[d]) is False:
        print('no dir!',d,params[d])
        sys.exit()

# dirs check out!



nets = glob.glob(params['netDir'] + '/*')
print('have %i nets to do' % len(nets))

for netFile in nets:
    baseName = netFile.split('/')[-1].split('.')[0]
    if baseName == 'meta':
        continue
    
    chainFile = params['chainDir'] + baseName + '.chain'
    overFile = params['overDir'] + baseName
    
    cmd = 'netChainSubset %s %s %s' % (netFile,chainFile,overFile)
    print(cmd)
    genutils3.runCMD(cmd)
 