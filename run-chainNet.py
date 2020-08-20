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
'netDir']

for d in dirsToCheck:
    if os.path.isdir(params[d]) is False:
        print('no dir!',d,params[d])
        sys.exit()

# dirs check out!



chains = glob.glob(params['chainDir'] + '/*chain')
print('have %i chains to do' % len(chains))

for chainFile in chains:
    baseName = chainFile.split('/')[-1].split('.')[0]
    netFile = params['netDir'] + baseName + '.net'
    cmd = 'chainNet %s %s %s %s /dev/null ' % (chainFile,params['oldFai'],params['newFai'],netFile)
    print(cmd)
    genutils3.runCMD(cmd)
 
