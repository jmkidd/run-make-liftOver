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

chainFileName = params['liftName'] + '.chain'

cmd = 'cat %s/* > %s' % (params['overDir'],chainFileName)
print(cmd)
genutils3.runCMD(cmd)

cmd = 'gzip %s' % chainFileName
print(cmd)
genutils3.runCMD(cmd)

fname = chainFileName + '.gz'
print('Complete!  liftover chain file is %s' % fname)
