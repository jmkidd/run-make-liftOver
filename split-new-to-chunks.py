import sys
import genutils3
import glob
import os

#split-new-to-chunks.py 
# split new chroms to chunks

paramsFile = 'params-file.txt'

params = genutils3.read_params(paramsFile)
print('Read params from %s' % paramsFile)

for p in params:
    print(p,params[p])
    


# check dirs
for d in [params['oldChromsDir'],params['newChromsDir'],params['chunksDir'],params['liftDir'] ]:
   if os.path.isdir(d) is False:
       print('no dir',d)
       sys.exit()    
# check dirs



fileList = glob.glob(params['newChromsDir']+'/*fa')
print('Found %i files in %s' % (len(fileList),params['newChromsDir']))



for f in fileList:
    print(f)
    baseName = f.split('/')[-1]
    baseName = baseName.split('.')[0]
    print(baseName)
    
    outRoot = params['chunksDir'] + baseName
    liftFile = params['liftDir'] + baseName + '.lft'
    
    cmd = 'faSplit size %s -lift=%s -oneFile 3000 %s' % (f,liftFile,outRoot)
    print(cmd)
    genutils3.runCMD(cmd)
