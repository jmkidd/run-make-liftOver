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
'chainRawDir']

for d in dirsToCheck:
    if os.path.isdir(params[d]) is False:
        print('no dir!',d,params[d])
        sys.exit()

# dirs check out!


cmd = 'chainMergeSort %s*.chain | chainSplit %s stdin ' % (params['chainRawDir'], params['chainDir'] )
print(cmd)
genutils3.runCMD(cmd)
