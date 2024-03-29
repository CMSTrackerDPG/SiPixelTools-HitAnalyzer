#ifndef DetectorInformation_h
#define DetectorInformation_h

/** \class DetectorInformation
 * ----------------------------------------------------------------------
 * DetectorInformation
 * ---------
 *
 * ----------------------------------------------------------------------
 * Send all questions, wishes and complaints to the 
 *
 * Author:  Urs Langenegger (PSI)
 * ----------------------------------------------------------------------
 *
 *
 ************************************************************/

#include <map>

#include "CondFormats/SiPixelObjects/interface/SiPixelFrameConverter.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFedCablingMap.h"
#include "CondFormats/DataRecord/interface/SiPixelFedCablingMapRcd.h"

#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHitCollection.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "Geometry/CommonDetUnit/interface/PixelGeomDetUnit.h"

#include "TrackingTools/TrackFitters/interface/TrajectoryFitter.h"
#include "TrackingTools/TrackFitters/interface/TrajectoryStateCombiner.h"
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"

#include "Alignment/OfflineValidation/interface/TrackerValidationVariables.h"
#include "TrackingTools/TrackAssociator/interface/TrackAssociatorParameters.h"
#include "TrackingTools/TrackAssociator/interface/TrackDetectorAssociator.h"

#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"

class TFile;
class DetId; 

class DetectorInformationPhase1 {

 public:
  
  DetectorInformationPhase1( const SiPixelFedCablingMap *cabling, const TrackerGeometry *geom);
  ~DetectorInformationPhase1();
  void dumpDetIds(const TrackerTopology* tt, const TrackerGeometry *geom);
  void ROClist(const DetId &pID);
  void bpixNames(const DetId &pID, int &DBlayer, int &DBladder, int &DBmodule, const TrackerTopology* tt);
  void fpixNames(const DetId &pID, int &DBdisk, int &DBblade, int &DBpanel, int &DBplaquette,  const TrackerTopology* tt);
  void onlineRocColRow(const DetId &pID, int offlineRow, int offlineCol, int &roc, int &col, int &row);
  void isPixelTrack(const edm::Ref<std::vector<Trajectory> > &refTraj, bool &isBpixtrack, bool &isFpixtrack);

 private:
  int             fVerbose; 
  //std::string     fRootFileName; 
  const SiPixelFedCablingMap *fCablingMap;
  //edm::ESGetToken<TrackerTopology, TrackerTopologyRcd> trackerTopoToken_;
  //edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> trackerGeomToken_;

  //TFile *fFile; 

  int                    fInit; 
  std::map<int, int>     fFEDID; 
  SiPixelFrameConverter *fPFC[140]; 
  int FEDMin, FEDMax;
  bool phase1_;

};

#endif
