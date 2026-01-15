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
cp $MYPWD/translation.dat ./translation.dat
#cmsRun $MYPWD/SimsToClus.py
#cmsRun $MYPWD/SimsToRec.py
#cmsRun $MYPWD/RawToRec.py
#cmsRun $MYPWD/gen_sim.py
#cmsRun $MYPWD/digitize.py
#cmsRun $MYPWD/reco.py

#cmsRun $MYPWD/runRawDumper.py
#cmsRun $MYPWD/runRawDumper_368546_rnd.py
#cmsRun $MYPWD/runRawDumper_379613.py
#cmsRun $MYPWD/runRawDumper_379765.py
#cmsRun $MYPWD/runRawDumper_307063.py
#cmsRun $MYPWD/runRawDumper_307073.py
#
#cmsRun $MYPWD/runHotPixels_394248.py
#cmsRun $MYPWD/runHotPixels_400179.py

#
#cmsRun $MYPWD/PixClusterAndTrack_386478.py   
#cmsRun $MYPWD/PixClusterAndTrack_386509.py   
#cmsRun $MYPWD/PixClusterAndTrack_386661.py   
#cmsRun $MYPWD/PixClusterAndTrack_386753.py   
#cmsRun $MYPWD/PixClusterAndTrack_386764.py   
#cmsRun $MYPWD/PixClusterAndTrack_386811.py   
#cmsRun $MYPWD/PixClusterAndTrack_386814.py   
#cmsRun $MYPWD/PixClusterAndTrack_386851.py      
#cmsRun $MYPWD/PixClusterAndTrack_386863.py   
#cmsRun $MYPWD/PixClusterAndTrack_386885.py
#cmsRun $MYPWD/PixClusterAndTrack_386917.py   
#cmsRun $MYPWD/PixClusterAndTrack_386945.py   
#cmsRun $MYPWD/PixClusterAndTrack_386951.py   
#cmsRun $MYPWD/PixClusterAndTrack_386951_ls30_70.py   
#cmsRun $MYPWD/PixClusterAndTrack_387474.py   
#cmsRun $MYPWD/PixClusterAndTrack_387528.py   
#cmsRun $MYPWD/PixClusterAndTrack_387530.py   
#cmsRun $MYPWD/PixClusterAndTrack_387607.py   
#cmsRun $MYPWD/PixClusterAndTrack_387716.py   
#cmsRun $MYPWD/PixClusterAndTrack_388056.py   
#cmsRun $MYPWD/PixClusterAndTrack_388088.py   
#cmsRun $MYPWD/PixClusterAndTrack_388089.py   
#cmsRun $MYPWD/PixClusterAndTrack_393346.py   
#cmsRun $MYPWD/PixClusterAndTrack_393514_rnd.py   
#cmsRun $MYPWD/PixClusterAndTrack_393516.py   
#cmsRun $MYPWD/PixClusterAndTrack_394467.py   
#cmsRun $MYPWD/PixClusterAndTrack_394508.py   
#cmsRun $MYPWD/PixClusterAndTrack_394619.py   
#cmsRun $MYPWD/PixClusterAndTrack_394638.py   
#cmsRun $MYPWD/PixClusterAndTrack_394677_rnd.py   
#cmsRun $MYPWD/PixClusterAndTrack_394753_rnd.py   
#cmsRun $MYPWD/PixClusterAndTrack_394753.py   
#cmsRun $MYPWD/PixClusterAndTrack_394776_rnd.py   
#cmsRun $MYPWD/PixClusterAndTrack_394860_rnd.py   
#cmsRun $MYPWD/PixClusterAndTrack_394861_rnd.py   
#cmsRun $MYPWD/PixClusterAndTrack_394862_rnd.py   
#cmsRun $MYPWD/PixClusterAndTrack_395148.py   
#cmsRun $MYPWD/PixClusterAndTrack_395392.py   
#cmsRun $MYPWD/PixClusterAndTrack_395392_rnd.py   
#cmsRun $MYPWD/PixClusterAndTrack_395424.py   
#cmsRun $MYPWD/PixClusterAndTrack_394886.py   
#cmsRun $MYPWD/PixClusterAndTrack_395939.py   
#cmsRun $MYPWD/PixClusterAndTrack_396008.py   
#cmsRun $MYPWD/PixClusterAndTrack_396727.py   
#cmsRun $MYPWD/PixClusterAndTrack_396735.py   
#cmsRun $MYPWD/PixClusterAndTrack_396757.py   
#cmsRun $MYPWD/PixClusterAndTrack_396421.py   
#cmsRun $MYPWD/PixClusterAndTrack_396805.py   
#cmsRun $MYPWD/PixClusterAndTrack_397432.py   
#cmsRun $MYPWD/PixClusterAndTrack_397489.py   
#cmsRun $MYPWD/PixClusterAndTrack_397502.py   
#cmsRun $MYPWD/PixClusterAndTrack_397502_rnd.py   
#cmsRun $MYPWD/PixClusterAndTrack_398040.py   
#cmsRun $MYPWD/PixClusterAndTrack_398081.py   
#cmsRun $MYPWD/PixClusterAndTrack_398183.py   
#cmsRun $MYPWD/PixClusterAndTrack_398183_rnd.py   
#cmsRun $MYPWD/PixClusterAndTrack_398859.py   
#cmsRun $MYPWD/PixClusterAndTrack_399890.py   
#cmsRun $MYPWD/PixClusterAndTrack_400165.py   
cmsRun $MYPWD/PixClusterAndTrack_400179.py   
 
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


