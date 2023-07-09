#!/bin/bash
# 
######SBATCH -p wn
######SBATCH --time 10:00:00 # 4h not enough for digis
######SBATCH -w t3wn60
######SBATCH --job-name=job-name
######SBATCH --account=t3
#SBATCH -e cn-test.err 
#SBATCH -o cn-test.out  # replace default slurm-SLURM_JOB_ID.out

echo HOME: $HOME 
echo USER: $USER 
echo SLURM_JOB_ID: $SLURM_JOB_ID
echo HOSTNAME: $HOSTNAME
echo PWD: $PWD

MYPWD=$PWD
echo $MYPWD

export X509_USER_PROXY=/t3home/kotlinski/.x509up_u1373
# export X509_USER_PROXY=/tmp/x509up_u1373  # does not work, copy from this to myhome 

echo JOB_ID: $SLURM_JOB_ID 
echo $X509_USER_PROXY

# each worker node has local /scratch space to be used during job run
mkdir -p /scratch/$USER/${SLURM_JOB_ID}
sleep 10
#
cd /scratch/$USER/${SLURM_JOB_ID}
cp $MYPWD/translation_pix.dat ./translation.dat
#cmsRun $MYPWD/SimsToClus.py
#cmsRun $MYPWD/SimsToRec.py
#cmsRun $MYPWD/RawToRec.py
#cmsRun $MYPWD/gen_sim.py
#cmsRun $MYPWD/digitize.py
#cmsRun $MYPWD/reco.py

#cmsRun $MYPWD/runRawDumper_360927.py
#cmsRun $MYPWD/runRawDumper_360942.py
#cmsRun $MYPWD/runRawDumper_360991.py
#cmsRun $MYPWD/runRawDumper_361045.py
#cmsRun $MYPWD/runRawDumper_361188.py
#cmsRun $MYPWD/runRawDumper_361223.py
#cmsRun $MYPWD/runRawDumper_361239.py
#cmsRun $MYPWD/runRawDumper_361417.py
#cmsRun $MYPWD/runRawDumper_361443.py
#cmsRun $MYPWD/runRawDumper_361468.py
#cmsRun $MYPWD/runRawDumper_361475.py
#cmsRun $MYPWD/runRawDumper_361512.py
#cmsRun $MYPWD/runRawDumper_368546_rnd.py
#cmsRun $MYPWD/runRawDumper_368546.py

#cmsRun $MYPWD/runHotPixels_347874.py
#cmsRun $MYPWD/PixClusterAndTrack_360820.py
#cmsRun $MYPWD/PixClusterAndTrack_360991.py
#cmsRun $MYPWD/PixClusterAndTrack_361971.py
#cmsRun $MYPWD/PixClusterAndTrack_361913.py
#cmsRun $MYPWD/PixClusterAndTrack_361188.py
#cmsRun $MYPWD/PixClusterAndTrack_361223.py
#cmsRun $MYPWD/PixClusterAndTrack_362439.py
#cmsRun $MYPWD/PixClusterAndTrack_362643.py
#cmsRun $MYPWD/PixClusterAndTrack_362695.py
#cmsRun $MYPWD/PixClusterAndTrack_362695_tree.py
#cmsRun $MYPWD/PixClusterAndTrack_362696.py
#cmsRun $MYPWD/PixClusterAndTrack_362698.py
#cmsRun $MYPWD/PixClusterAndTrack_362758.py
#cmsRun $MYPWD/PixClusterAndTrack_ephmeral.py
#cmsRun $MYPWD/PixClusterAndTrack_369596.py
#cmsRun $MYPWD/PixClusterAndTrack_369927.py
#cmsRun $MYPWD/PixClusterAndTrack_369956.py
#cmsRun $MYPWD/PixClusterAndTrack_370093.py
cmsRun $MYPWD/PixClusterAndTrack_370129.py
#cmsRun $MYPWD/PixClusterAndTrack_370129_1mod.py
# 
pwd
ls 
cd $MYPWD
pwd
ls /scratch/$USER/${SLURM_JOB_ID}
#cp /scratch/$USER/${SLURM_JOB_ID}/noise.root $MYPWD/.
#cp /scratch/$USER/${SLURM_JOB_ID}/simtorec.root $MYPWD/.
#cp /scratch/$USER/${SLURM_JOB_ID}/rawtoreco.root $MYPWD/.
#cp /scratch/$USER/${SLURM_JOB_ID}/raw.root $MYPWD/raw.root
#cp /scratch/$USER/${SLURM_JOB_ID}/clus_ana_cosmics.root $MYPWD/.
cp /scratch/$USER/${SLURM_JOB_ID}/clus_ana.root $MYPWD/.

# xrdcp -d 1 -f s.root root://t3se01.psi.ch:1094//store/user/kotlinski/MC/test/s.root  # is OK,
# xrdcp      -f s.root root://t3dcachedb.psi.ch:1094//pnfs/psi.ch/cms/trivcat/store/user/kotlinski/MC/test/. # OK
# xrdcp -f /scratch/$USER/${SLURM_JOB_ID}/s.root root://t3dcachedb.psi.ch:1094//pnfs/psi.ch/cms/trivcat/store/user/kotlinski/MC/test/s.root   # OK
#xrdcp -f /scratch/$USER/${SLURM_JOB_ID}/s.root root://t3se01.psi.ch:1094//store/user/kotlinski/MC/mu_pt100/simhits/simHits2_eta0p1.root # OK
#xrdcp -f /scratch/$USER/${SLURM_JOB_ID}/d.root root://t3se01.psi.ch:1094//store/user/kotlinski/MC11/mu_pt100/raw/raw1.root # OK
#xrdcp -f /scratch/$USER/${SLURM_JOB_ID}/r.root root://t3se01.psi.ch:1094//store/user/kotlinski/MC11/mu_pt100/reco/reco1.root # OK

#  rmdir  /scratch/$USER/${SLURM_JOB_ID}
rm -rf  /scratch/$USER/${SLURM_JOB_ID}
date


