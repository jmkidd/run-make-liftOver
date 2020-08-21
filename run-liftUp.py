import sys
import genutils3
import glob
import os

#blat NEW vs OLD


from optparse import  OptionParser

#####################################################################
USAGE = """
python run-liftUp.py --file <optional>

runs the liftUp cmds, reads from params-file.txt
use option --file to optionally save cmds to file to be run in stead of
executing


"""
parser = OptionParser(USAGE)
parser.add_option('--file',dest='writeFile', action='store_true',default=False, help = 'write cmds to file, do not run')

(options, args) = parser.parse_args()

#####################################################################


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


if options.writeFile is True:
    cmFileName = 'liftUp.cmds'
    print('saving cmds to file',cmFileName)
    cmdFile = open(cmFileName,'w')

newFiles = glob.glob(params['chunksDir'] + '/*fa')
print('\nstart\n')
for nf in newFiles:
    newBaseName = nf.split('/')[-1].split('.')[0]
    
    pslFile = params['pslDir'] + newBaseName + '.psl'
    liftFile = params['liftDir'] + newBaseName + '.lft'
    blatFilePre = params['blatOutDir'] + newBaseName + '-*'
    
    cmd = 'liftUp -pslQ %s %s warn %s' % (pslFile,liftFile,blatFilePre)
    if options.writeFile is True:    
        cmd += '\n'
        cmdFile.write(cmd)
    else:
       print(cmd)
       genutils3.runCMD(cmd)
    
    
if options.writeFile is True:
    cmdFile.close()
    


