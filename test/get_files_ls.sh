for i in {1..21};
#do dasgoclient -query="file dataset=/ExpressPhysics/Run2025C-Express-v1/FEVT run=392669 lumi=$i";
#do dasgoclient -query="file dataset=/ExpressPhysics/Run2025D-Express-v1/FEVT run=395392 lumi=$i";
#do dasgoclient -query="file dataset=/ExpressPhysics/Run2025E-Express-v1/FEVT run=396421 lumi=$i";
#do dasgoclient -query="file dataset=/ExpressPhysics/Run2025F-Express-v1/FEVT run=396805 lumi=$i";
#do dasgoclient -query="file dataset=/ExpressPhysics/Run2025G-Express-v1/FEVT run=398081 lumi=$i";
do dasgoclient -query="file dataset=/ExpressPhysics/Run2025G-Express-v1/FEVT run=398859 lumi=$i";
done; 


 
