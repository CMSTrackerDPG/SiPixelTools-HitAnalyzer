for i in {1..116};
#do dasgoclient -query="file dataset=/ExpressPhysics/Run2025C-Express-v1/FEVT run=392669 lumi=$i";
#do dasgoclient -query="file dataset=/ExpressPhysics/Run2025D-Express-v1/FEVT run=394431 lumi=$i";
do dasgoclient -query="file dataset=/ExpressPhysics/Run2025D-Express-v1/FEVT run=394449 lumi=$i";
done; 


 
