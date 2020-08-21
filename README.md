# run-make-liftOver
scripts to make liftOver chain files


example is for
/home/jmkidd/links/kidd-lab/genomes/Dog10K_Boxer_Tasha_1.0.KP081776.1/make-liftOver/TashaToCanFam3.1/run-make-liftOver

make Dog10K_Boxer_Tasha_1.0.KP081776.1TocanFam3.1


made new params files

old = Dog10K_Boxer_Tasha_1.0.KP081776.1
new = canFam3.1

make the dirs that are needed
mkdir chunks lift blatRun psl chain chainRun chainRaw net over logs

####
liftName Dog10K_Boxer_Tasha_1.0.KP081776.1TocanFam3.1
oldRef /home/jmkidd/links/kidd-lab/genomes/Dog10K_Boxer_Tasha_1.0.KP081776.1/ref/Dog10K_Boxer_Tasha_1.0.KP081776.1.fa
oldFai /home/jmkidd/links/kidd-lab/genomes/Dog10K_Boxer_Tasha_1.0.KP081776.1/ref/Dog10K_Boxer_Tasha_1.0.KP081776.1.fa.fai
oldOOC /home/jmkidd/links/kidd-lab/genomes/Dog10K_Boxer_Tasha_1.0.KP081776.1/ref/11.ooc
oldChromsDir /home/jmkidd/links/kidd-lab/genomes/Dog10K_Boxer_Tasha_1.0.KP081776.1/by-chrom/
newChromsDir canfam-by-chrom/
newFai /home/jmkidd/links/kidd-lab/genomes/canFam3.1/canFam3.1-noY/canFam3.1.fa.fai
chunksDir chunks/
liftDir lift/
blatOutDir blatRun/
pslDir psl/
chainDir chain/
chainRunDir chainRun/
chainRawDir chainRaw/
netDir net/
overDir over/

#Step 1, split NEW genome to 3kb chunks using UCSC faSplit tool
python split-new-to-chunks.py

# Step 2, write blat cmds
blat NEW vs OLD (old is the database, uses old 11.ooc file.), minScore=100 and minIdentity=95
python write-blat-cmds.py

this makes three files of blat cmds to be run on the cluster
one is of same vs same chroms, these take a longer time to run,
one is of chroms vs chroms
one involves 'unplaced' chroms, may need to edit python script to get names right

[jmkidd@gl-login1 run-make-liftOver]$ wc blat*cmds
   133948   1071584  38140926 blat.REST.cmds
       40       320     10436 blat.SAME.cmds
   349676   2797408 101646270 blat.UNK.cmds


check completion:
[jmkidd@gl-login2 run-make-liftOver]$ dircnt_args blatRun/
blatRun/ contains 483664 files
sum: 483664



# Step 3
run liftUp to convert psl output files from blat chunks to original chromosome coordinates
python run-liftUp.py

use python run-liftUp.py --file 
there are lots of cmds!

[jmkidd@gl3207 run-make-liftOver]$ wc liftUp.cmds
  3268  19608 320211 liftUp.cmds


# Step 4 run axtcCain to chain together alignments
python run-chain.py
edit to be write-run-chain.py

then run runChain.cmds

# Step 5 merge, sort, and split
runs chainMergeSort then chainSplit

python run-merge-sort.py

# Step 6, run chainNet to make alignment nets out of the chains

python run-chainNet.py

# Step 7 run netChainSubset
this gets only the chains that appear in the net

python run-netChainSubset.py


# Step 8 cat together chains and gzip
python combine-over.py

Complete!  liftover chain file is Dog10K_Boxer_Tasha_1.0.KP081776.1TocanFam3.1.chain.gz



