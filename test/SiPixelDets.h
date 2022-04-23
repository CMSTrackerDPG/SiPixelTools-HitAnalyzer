#ifndef SiPixelDets_h
#define SiPixelDets_h

#include <map>

#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

//#include "FWCore/MessageLogger/interface/MessageLogger.h"

//#include "DataFormats/Common/interface/Handle.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"

#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"

class SiPixelDets : public edm::one::EDAnalyzer<edm::one::SharedResources>
{
 public:
  
  SiPixelDets(const edm::ParameterSet& conf);
  
  ~SiPixelDets();
  //  void beginJob() (const edm::EventSetup&) override;
  void beginJob() override;
  void endJob() override; 
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  
  void printDet(DetId detid, const TrackerTopology* tt);

 private:

  edm::ParameterSet conf_;
  bool phase1_;
  edm::ESGetToken<TrackerTopology, TrackerTopologyRcd> trackerTopoToken_;
  edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> trackerGeomToken_;

  //typedef std::vector< edm::ParameterSet > Parameters;
  //Parameters BPixParameters_;
  //Parameters FPixParameters_;

};


#endif
