#ifndef SiPixelPixels_h
#define SiPixelPixels_h

#include <map>

#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "CondFormats/DataRecord/interface/SiPixelFedCablingMapRcd.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFedCablingMap.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelFedCablingTree.h"

//#include "FWCore/MessageLogger/interface/MessageLogger.h"

//#include "DataFormats/Common/interface/Handle.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"

#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"

class SiPixelPixels : public edm::one::EDAnalyzer<edm::one::SharedResources>
{
 public:
  
  SiPixelPixels(const edm::ParameterSet& conf);
  
  ~SiPixelPixels();
  
  //  void beginJob() (const edm::EventSetup&) override;

  void beginJob() override;
  
  void endJob() override; 
  
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  
  void printDet(DetId detid, const TrackerTopology* tt);

 private:

  edm::ParameterSet conf_;
  bool phase1_;
  //typedef std::vector< edm::ParameterSet > Parameters;
  //Parameters BPixParameters_;
  //Parameters FPixParameters_;
  edm::ESGetToken<TrackerTopology, TrackerTopologyRcd> trackerTopoToken_;
  edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> trackerGeomToken_;
  edm::ESGetToken<SiPixelFedCablingMap, SiPixelFedCablingMapRcd> cablingMapToken_;
};


#endif
