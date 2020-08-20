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

pslFiles = glob.glob(params['pslDir'] + '*.psl')
print('have %i psl files to do' % len(pslFiles))

ofn = 'runChain.cmds'
print('Writing cmds to',ofn)

outFile = open(ofn,'w')

for psl in pslFiles:
    pslBaseName = psl.split('/')[-1].split('.')[0]
        
#    print(pslBaseName)
    
    targetFile = params['oldRef']
    queryFile = params['newChromsDir'] + pslBaseName + '.fa'
    chainFile = params['chainRawDir'] + pslBaseName + '.chain'
    
    cmd = 'axtChain -linearGap=medium -psl -faQ -faT %s %s %s %s' % (psl,targetFile,queryFile,chainFile)
    cmd += '\n'
    outFile.write(cmd)
#    print(cmd)
#    genutils3.runCMD(cmd)
outFile.close()
    

    
