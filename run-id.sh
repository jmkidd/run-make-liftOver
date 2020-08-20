#!/bin/bash
# The interpreter used to execute the script

# “#SBATCH” directives that convey submission options:

# #SBATCH --job-name=mrsFAST-map
#SBATCH --mail-user=jmkidd@umich.edu
#SBATCH --mail-type=FAIL,ARRAY_TASKS
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=8G 
#SBATCH --time=72:00:00
#SBATCH --account=jmkidd99
#SBATCH --partition=standard
#SBATCH --output=logs/%x-%A_%a.out.log
#SBATCH --export=ALL

#SBATCH --array=1-148

# The application(s) to execute along with its input arguments and options:
cd $SLURM_SUBMIT_DIR;
date;
run-by-id-log.pl runChain.cmds logs/runChain.cmds.cmds $SLURM_ARRAY_TASK_ID
#run-by-cmd-number-modulus.py --cmds blat.Y.cmds --log logs/blat.Y.cmds.log --mod 100 --worker $SLURM_ARRAY_TASK_ID
date;






