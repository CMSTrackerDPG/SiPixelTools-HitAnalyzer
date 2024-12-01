/** \class SiPixelRawDumper_H
 *  Plug-in module that dump raw data file 
 *  for pixel subdetector
 *  Added class to interpret the data d.k. 30/10/08
 *  Add histograms. Add pix 0 detection.
 * Works with v7x, comment out the digis access.
 * Adopted for Phase1 
 * Add simple error vs fed num histos.
 */

#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Common/interface/Handle.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/FEDRawData/interface/FEDRawDataCollection.h"
#include "DataFormats/FEDRawData/interface/FEDRawData.h"

#include "DataFormats/FEDRawData/interface/FEDNumbering.h"

#include "EventFilter/SiPixelRawToDigi/interface/PixelDataFormatter.h"

// To use root histos
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

// For ROOT
#include <TROOT.h>
//#include <TChain.h>
#include <TFile.h>
#include <TF1.h>
#include <TH2F.h>
#include <TH1D.h>
#include <TTree.h>
#include <TProfile.h>
#include <TProfile2D.h>

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <iomanip>


using namespace std;

//#define L1  // L1 information not in RAW
//#define OUTFILE 
#define PHASE1
#define TEST_LAYERS
#define CHECK_BX
//#define USE_TREE
//#define PER_FED
#define DO_CHANNEL_ORDER

namespace {
  //const bool FULL_DECODE = true;
  bool printErrors  = false;
  bool printData    = false;
  bool printHeaders = false;
  bool printDebug = false; // special printouts 
  const bool printBX = false;
  const bool CHECK_PIXELS = true;
  const bool PRINT_BASELINE = false;
  const bool SKIP_PERMANENT_MASK = true; //ignore channelks which are always masked 
  //int countDecodeErrors1=0, countDecodeErrors2=0;
#ifdef PHASE1
  const int n_of_FEDs = 139;
  const int n_of_Channels = 48;
  const int fedIdBpixMax = 93;
  const bool phase1 = true;
#else
  const int n_of_FEDs = 41;
  const int n_of_Channels = 36;
  const int fedIdBpixMax = 32;
  const bool phase1 = false;
#endif

  ///////////////////////////////////////////
// Class to get names, hide in namespace to avoid conflicts 
class MyConvert {
public:
  MyConvert();  // read translation.dat
  ~MyConvert() {}
  string moduleNameFromFedChan(int fed,int fedChan); // gives module name using the setup table
  int layerFromFedChan(int fed, int fedChan); // gives layer using the setup table
  static string moduleNameFromFedChan(int fed,int fedChan, int roc, string & tbm); //reads translation.dat
  static int layerFromName(string name);  // just parses the string name
  static int ladderFromName(string name);
  static int moduleFromName(string name);
  static int shellFromName(string name);

private:
  int layerNumber[139][48];
  string moduleName[139][48];
};

MyConvert::MyConvert() {

  // layer number: 1,2,3,4, 0 for fpix, -1 for undefined
  for(int fed=0; fed<139; ++fed) {
    for(int chan=0; chan<48; ++chan) {
      layerNumber[fed][chan]=-1;
      moduleName[fed][chan]="";
    }
  }

  ifstream infile;                        // input file, name data_file uniqe
  infile.open("translation.dat",ios::in); // open data file

  if (infile.fail()) {
    cout << " File not found " << endl;
    return; // 
  }
  cout<<"MyConvert constructor - read translation.dat, setup layer and module tables"<<endl;

  //string line;
  char line[500];
  infile.getline(line,500,'\n');
  
  //bool print = false;
  string name, modName=" ";
  int fec,mfec,mfecChan,hub,port,rocId,fed,fedChan,rocOrder;
  string tbm = " ";
  int fedOld=-1, fedChanOld=-1;
  for(int i=0;i<1000000;++i) {
    // first get the name, then  decide whether it is barrel and endcap
    infile>>name;
    infile>>tbm>>fec>>mfec>>mfecChan>>hub>>port>>rocId>>fed>>fedChan>>rocOrder;
    
    // if(name==" ")continue;
    // if (name[0]=='F') {
    //   // endcap doesn't have the TBM token to read
    //   infile>>tbm>>fec>>mfec>>mfecChan>>hub>>port>>rocId>>fed>>fedChan>>rocOrder;
    // } else {
    //   infile>>tbm>>fec>>mfec>>mfecChan>>hub>>port>>rocId>>fed>>fedChan>>rocOrder;
    // }
    // cout<<name<<endl;

    if ( infile.eof() != 0 ) {
      //cout<< " end of file " << endl;
      break;;
    } else if (infile.fail()) { // check for errors
      cout << "Cannot read data file" << endl;
      return;
    }
    
    if(fed==fedOld && fedChanOld==fedChan) continue;
    fedOld = fed;
    fedChanOld = fedChan;

    if (fed<1294) { // do only for bpix 
      //barrel module name requested, do not use the roc0 parameter

      // strip out the _ROC section from the name because it is not needed to identify the ROC number
      string::size_type idx;
      idx = name.find("_ROC");
      if(idx != string::npos) {
	modName = name.substr(0,(idx));
	moduleName[fed-1200][fedChan-1] = modName;
	int layer = layerFromName(modName);
	layerNumber[fed-1200][fedChan-1] = layer;

      }

    } else {  // fpix 
      modName = name; 
      moduleName[fed-1200][fedChan-1] = modName;
      layerNumber[fed-1200][fedChan-1] = 0; // make fpix layer=0
    } 
  }  // end line loop
  
  infile.close();  

  // print 
  // for(int fed=0; fed<94; ++fed) {
  //   for(int chan=0; chan<48; ++chan) {
  //     cout<<"fed "<<(fed+1200)<<" chan "<<(chan+1)<<" module "<<moduleName[fed][chan]
  // 	  <<" layer "<<layerNumber[fed][chan];
  //     if(layerNumber[fed][chan]>0) cout<<" found ";
  //     else cout<<" not found ";
  //     cout<<endl;
  //   }
  // }

} // end constructor 

// used the table made in the constructor, fast but needs class instatiation
string MyConvert::moduleNameFromFedChan(int fed,int fedChan) {
  string module="";
  if(fed<1200 || fed>1338 || fedChan<1 || fedChan>48) {
    cout<<" wrong fed/channel "<<fed<<"/"<<fedChan<<endl;
    return module;
  }
  module = moduleName[fed-1200][fedChan-1];
  //if(fed<1294 && module=="") cout<<"module name not fund "<<fed<<"/"<<fedChan<<endl;
  return module;
}
int MyConvert::layerFromFedChan(int fed, int fedChan) {
  int layer = -1;
  if(fed<1200 || fed>1338 || fedChan<1 || fedChan>48) {
    cout<<" wrong fed/channel "<<fed<<"/"<<fedChan<<endl;
    return layer;
  }
  layer = layerNumber[fed-1200][fedChan-1]; // return -1 for non-existing channels
  if(layer==-1) return -1;

  if(fed<1294 && layer==0) cout<<"layer number not fund "<<fed<<"/"<<fedChan<<endl;
  if(fed>1294 && layer!=0) cout<<"layer number wrong for fpix "<<fed<<"/"<<fedChan<<endl;
  return layer;
}

// layer number form module name 
int MyConvert::layerFromName(string modName) {
  int layer=0;
  string::size_type idx;
  for(int i=1; i<=4; ++i) {
    string name = "_LYR" + std::to_string(i);
    idx=modName.find(name);
    if(idx != string::npos) {layer=i; break;}
  }
  return layer;
}
// laddder number from module name 
int MyConvert::ladderFromName(string modName) {
  int ladder=0;
  string::size_type idx;
  for(int i=32;i>=1;--i) {  // this is not optimal 
    string name = "_LDR" + std::to_string(i);
    idx=modName.find(name);
    if(idx != string::npos) {ladder=i; break;}
  }
  // add sign for I/O
  int shell = shellFromName(modName);
  if(shell==1 || shell==3) ladder *= (-1);
  return ladder;
}
// module number from module name 
int MyConvert::moduleFromName(string modName) {
  int module=0;
  string::size_type idx;
  for(int i=1;i<=4;++i) {
    string name = "_MOD" + std::to_string(i);
    idx=modName.find(name);
    if(idx != string::npos) {module=i; break;}
  }
  // add sign for +-z
  int shell = shellFromName(modName);
  if(shell==1 || shell==2) module *= (-1);
  return module;
}
// shell number from module name 
int MyConvert::shellFromName(string modName) {
  int shell=0;
  //1-BmO,2-BmI,3-BpO,4-BpI
  string::size_type idx;
  idx = modName.find("_BmO");
  if(idx != string::npos) {shell=1; return shell;}
  idx = modName.find("_BmI");
  if(idx != string::npos) {shell=2; return shell;}
  idx = modName.find("_BpO");
  if(idx != string::npos) {shell=3; return shell;}
  idx = modName.find("_BpI");
  if(idx != string::npos) {shell=4; return shell;}
  return 0;
}

// Method returns the module name and the tbm type as strings
// Slow, read the translation.dat file each time 
// input: int fed, fedChan
// output: string name, tbm ("A" or "B")
string MyConvert::moduleNameFromFedChan(int fed0,int fedChan0, int roc0, string & tbm0) {
  if ( fed0<1200 || fed0>1293) return " "; // works only for bpix

  ifstream infile;                        // input file, name data_file uniqe
  infile.open("translation.dat",ios::in); // open data file

  if (infile.fail()) {
    cout << " File not found " << endl;
    return(" "); // signal error
  }

  //string line;
  char line[500];
  infile.getline(line,500,'\n');

  string name, modName=" ";
  int fec,mfec,mfecChan,hub,port,rocId,fed,fedChan,rocOrder;
  string tbm = " ";
  int fedOld=-1, fedChanOld=-1, rocOld=-1;
  bool found = false;
  for(int i=0;i<100000;++i) {
    //bool print = false;

    // first get the name, then  decide whether it is barrel and endcap
    infile>>name;
    
    if(name==" ")continue;

    if (name[0]=='F') {
        // endcap doesn't have the TBM token to read
        infile>>fec>>mfec>>mfecChan>>hub>>port>>rocId>>fed>>fedChan>>rocOrder;
    } else {
        infile>>tbm>>fec>>mfec>>mfecChan>>hub>>port>>rocId>>fed>>fedChan>>rocOrder;
    }

    
    if ( infile.eof() != 0 ) {
      //cout<< " end of file " << endl;
      break;;
    } else if (infile.fail()) { // check for errors
      cout << "Cannot read data file" << endl;
      return(" ");
    }

    if (fed0<1294) {
        //barrel module name requested, do not use the roc0 parameter
        if(fed==fedOld && fedChanOld==fedChan) continue;
        fedOld = fed;
        fedChanOld = fedChan;

        if(fed==fed0 && fedChan==fedChan0) {  // found
            found = true;
            tbm0=tbm;
            // strip out the _ROC section from the name because it is not needed to identify the ROC number
            string::size_type idx;
            idx = name.find("_ROC");
            if(idx != string::npos) {
                modName = name.substr(0,(idx));
            }
            break;
        }
    } else {  // DOES NOT YET WORK FOR FPIX
        // endcap module name requested, use the roc0 parameter
        if(fed==fedOld && fedChanOld==fedChan && rocOld==rocOrder) continue;
        fedOld = fed;
        fedChanOld = fedChan;
        rocOld = rocOrder;

        if(fed==fed0 && fedChan==fedChan0 && rocOrder==roc0) {  // found
            found = true;
            tbm0=tbm;
            // do not strip anything from the endcap name because it is needed to identify the ROC number
            modName = name; 
            break;
        }
    }
  }  // end line loop
  
  infile.close();  
  if(!found &&0) cout<<" Module not found "<<fed0<<" "<<fedChan0<<endl;

  return modName;  // just return " " if not found

}

} // end namespace 
////////////////////////////////////////////////////////////////////////////////

// Include the helper decoding class (how did I mange to avoid linking conflicts?)
/////////////////////////////////////////////////////////////////////////////
class MyDecode {
public:
  MyDecode();
  ~MyDecode() {}
  int error(int error,int & fedChannel, int fed, int & stat1, int & stat2, bool print=false);
  int data(int word, int & fedChannel, int fed, int & stat1, int & stat2, bool print=false);
  int header(unsigned long long word64, int fed, bool print, unsigned int & bx);
  int trailer(unsigned long long word64, int fed, bool print);
  static int convertToCol(int dcol,int pix);
  static int convertToRow(int pix);
  int getLayer(int fed, int chan);
  int getFpixRing(int fed, int chan);
  string getModName(int fed, int chan);
  int get_adc(void) {return adc_;}
  int get_roc(void) {return roc_;}
  int get_dcol(void) {return dcol_;}
  int get_pix(void) {return pix_;}
  int get_col(void) {return col_;}
  int get_row(void) {return row_;}
  int get_channel(void) {return channel_;}
  void setPrint(int selectedFED, int selectedChannel);
  vector<int>* getStatuses(void) {return &errorStatuses;}

private:
  int channel_, adc_, roc_, dcol_, pix_, col_, row_;
  int selectedFED_, selectedChannel_;
  // to store the previous pixel 
  int fed0, chan0, roc0, dcol0, pix0, col0, row0, count0;
  vector<int> errorStatuses;

  MyConvert converter;
};
MyDecode::MyDecode() {
  cout<<"Construct MyDecode "<<endl;
  selectedFED_=-1; selectedChannel_=-1;
  cout<<selectedFED_<<" "<<selectedChannel_<<endl;
  fed0 = -1, chan0 = -1, roc0 = -1, dcol0 =-1, pix0 =-1, col0=-1, row0=-1, count0=-1;
}
/////////////////////////////////////////////////////////////////////////////
//Returns 1,2,3,4 for layer 1,2,3,4, 0 for fpix
int MyDecode::getLayer(int fed, int chan) {
  int layer = converter.layerFromFedChan(fed,chan); // uses the table
  return layer;
}
int MyDecode::getFpixRing(int fed, int chan) {
  string name = getModName(fed,chan); 
  int ring=0;
  string::size_type idx;
  idx = name.find("RNG1");
  if(idx != string::npos) {ring=1;}
  else {
    idx = name.find("RNG2");
    if(idx != string::npos) ring=2;
  }
  return ring;
}
string MyDecode::getModName(int fed, int chan) {
  string name = converter.moduleNameFromFedChan(fed,chan); // uses the table
  return name;
}
void MyDecode::setPrint(int fed, int chan) {
  selectedFED_=fed;
  selectedChannel_=chan;
  return;
}

int MyDecode::convertToCol(int dcol, int pix) {
  // First find if we are in the first or 2nd col of a dcol.
  int colEvenOdd = pix%2;  // module(2), 0-1st sol, 1-2nd col.
  // Transform
  return (dcol * 2 + colEvenOdd); // col address, starts from 0

}
int MyDecode::convertToRow(int pix) {
  return abs( int(pix/2) - 80); // row addres, starts from 0
}

int MyDecode::header(unsigned long long word64, int fed, bool print, unsigned int & bx) {
  int fed_id=(word64>>8)&0xfff;
  int event_id=(word64>>32)&0xffffff;
  bx =(word64>>20)&0xfff;
//   if(bx!=101) {
//     cout<<" Header "<<" for FED "
// 	<<fed_id<<" event "<<event_id<<" bx "<<bx<<endl;
//     int dummy=0;
//     cout<<" : ";
//     cin>>dummy;
//   }
  if(print) cout<<"Header "<<" for FED "
		<<fed_id<<" event "<<event_id<<"/"<<hex<<event_id<<dec<<" bx "<<bx<<endl;
  fed0=-1; // reset the previous hit fed id
  return event_id;
}
//
int MyDecode::trailer(unsigned long long word64, int fed, bool print) {
  int slinkLength = int( (word64>>32) & 0xffffff );
  int crc         = int( (word64&0xffff0000)>>16 );
  int tts         = int( (word64&0xf0)>>4);
  int slinkError  = int( (word64&0xf00)>>8);
  if(print) cout<<"Trailer "<<" len "<<slinkLength
		<<" tts "<<tts<<" error "<<slinkError<<" crc "<<hex<<crc<<dec<<endl;
  return slinkLength;
}
//
// Decode error FIFO
// Works for the SLink error words. d.k. 11/22
int MyDecode::error(int word, int & fedChannel, int fed, int & stat1, int & stat2, bool print) {
  int status = -1;
  print = print || printErrors;

  // main masks to extract different fields 
  const unsigned int  channelMask   = 0xfc000000; // channel num mask
  const unsigned int  errorMask     = 0x03e00000;
  const unsigned int  eventNumMask  = 0x001fe000; // event number mask for ENE
  const unsigned int  headerMask    = 0x00001000; // no header bit
  const unsigned int  decodeMask    = 0x00000f00; // decode errors 
  const unsigned int  tbmEventMask  = 0x000000ff;   // tbm event num mask
  const unsigned int  tbmStatusMask = 0x000000ff;   // TBM trailer info
  const unsigned int  tbmStackMask  = 0x0000003f; //Stack info in TO

  const unsigned int  maskedMask     = 0x03200000; // roc=25
  const unsigned int  gapMask        = 0x03400000; // roc=26
  const unsigned int  dummyMask      = 0x03600000; // roc=27
  const unsigned int  timeOut        = 0x03a00000; // roc=29
  const unsigned int  trailError     = 0x03c00000; // roc=30
  const unsigned int  eventNumError  = 0x03e00000; // rpc=31 

  const unsigned int  bit20Mask      = 0x00100000; // event counter
  const unsigned int  l1countMask    = 0x000fffff; // event counter

  // Error flags 
  const unsigned int  RocErrMask   = 0x800;   // bit 11, NOR 
  const unsigned int  AutoMask     = 0x400;   // bit 10, Autoreset 
  const unsigned int  PKAMMask     = 0x200;   // bit 9, PKAM 
  const unsigned int  overflowMask = 0x100;  // bit 8, Overflow 
  const unsigned int  noTrailerMask= 0x300;  // bit 8&9 trailer missing  

  //TBM08 status masks
  const unsigned int  StackFullMask = 0x1;
  const unsigned int  CalMask       = 0x2;
  const unsigned int  EvtNumRstMask = 0x4;
  const unsigned int  SyncTrigMask  = 0x8;
  const unsigned int  SyncErrMask   = 0x10; // also hardreset
  const unsigned int  ROCResetMask  = 0x20;
  const unsigned int  TBMResetMask  = 0x40;
  const unsigned int  NTPMask       = 0x80; // No Token Pass
  

  unsigned int channel =  (word & channelMask) >>26;
  fedChannel = channel;
 
  //cout<<"error word "<<hex<<word<<dec<<endl;
  
  if( (word&errorMask) == dummyMask ) { // DUMMY WORD
    //cout<<" Dummy word";
    return 0;

  } else if( (word&errorMask) == gapMask ) { // GAP WORD
    //cout<<" Gap word";
    return 0;
    
  } else if( (word&errorMask) == maskedMask ) { // Masked  WORD
    
    unsigned int bit20 =      (word & bit20Mask); // works only for slink format    
    if(bit20!=0) {  // Auto masking
      status=-18;
      errorStatuses.push_back(18);
      if(print) {
	int l1count = word&l1countMask;
	cout<<"Masked: channel "<<channel<<" by automasking, in event "<<l1count;   
      }
    } else { // permanent mask (masked and unused channels)
      if(print && !SKIP_PERMANENT_MASK) 
	cout<<" Masked: channel "<<channel<<" by permanent mask";
      status=-17;  // not filled in data
      errorStatuses.push_back(17);
      return status;  
    }
    
  } else if( (word&errorMask)==timeOut ) { // TIMEOUT

    if(selectedChannel_>-1 && channel!=unsigned(selectedChannel_)) return 0;

    unsigned int bit20 = (word & bit20Mask); // works only for slink format
    if(bit20!=0) { // count timeout on first word
      unsigned int diag = (word & tbmStackMask); // TBM stack, does it have a meaning  
      // no event number in the FEROL format
      if(print) {
	cout << "Timeout Error - channel: " << channel ; 
	cout <<" TBM Stack Count " << diag; 
      }
      //cout<<"1st TO word"<<endl;
      stat1=int(diag);
      status=-10;
      errorStatuses.push_back(10);
    } else { // 2nd word, useless, nothing interesting  
      //unsigned int index=(word & tbmStackMask); // TBM chan, same as channel
      //if(print) { cout << ", 2nd word:index = " << index; }
      return 0;
    }
   
    //cout<<fed<<" "<<channel<<" "<<bit20<<" "<<l1acnt<<" "<<diag<<endl;

  } else if( (word&errorMask) == eventNumError ) { // EVENT NUMBER ERROR
    if(selectedChannel_>-1 && channel!=unsigned(selectedChannel_)) return 0;

    status = -11;
    errorStatuses.push_back(11);
    unsigned int tbm_event   =  (word & tbmEventMask); // OK
    unsigned int fed_event   =  (word & eventNumMask)>>13; //always 0 in FEROL 
    unsigned int tbm_header  =  (word & headerMask);
    stat1 = int(tbm_event);
    stat2 = int(fed_event);
    if(stat2>0) cout<<"ene tbm "<<stat1<<" fed "<<stat2<<endl;

    if(print) {
      cout<<"Event Number Error- channel: "<<channel<<" tbm event "<<tbm_event;
	//<<" fed event num "<<fed_event; // always 0
      if(tbm_header!=0) cout<<" NO header!";
    }
    
  } else if( ((word&errorMask) == trailError)) {  // TRAILER 

    if(selectedChannel_>-1 && channel!=unsigned(selectedChannel_)) return 0;

    unsigned int tbm_status   =  (word & tbmStatusMask);
    unsigned int decode_status=  (word & decodeMask);
    
    if(print) cout<<"Trailer Error-TBM status:0x"<<hex<<tbm_status
		  <<" ErrBits:0x"<<decode_status<<dec<<","; // <<endl;

    if(tbm_status!=0) { // trailer errors
      status = -15;  // catch others (Cal?)
     if(tbm_status & NTPMask)      {status=-9;errorStatuses.push_back(9);if(print) cout << " NTP, ";}
     if(tbm_status & TBMResetMask) {status=-19;errorStatuses.push_back(19); if(print) cout << " TBM Reset, "; }
     if(tbm_status & ROCResetMask) {status=-8;errorStatuses.push_back(8); if(print) cout << " ROC Reset, "; }
     if(tbm_status & SyncErrMask) {status=-24;errorStatuses.push_back(24); if(print) cout << " SyncErr, ";}
     if(tbm_status & SyncTrigMask) {status=-24;errorStatuses.push_back(21); if(print) cout << " SyncTrig, ";}
     if(tbm_status & EvtNumRstMask) {status=-23;errorStatuses.push_back(23); if(print) cout << " TBMEvt#Clear, ";}
     if(tbm_status & CalMask) if(print) {errorStatuses.push_back(15);cout << " CalTrig, ";}
     if(tbm_status & StackFullMask) {status=-22;errorStatuses.push_back(22); if(print) cout << " Stack Full, ";}
    }
     
    if(decode_status!=0) { // decode errors

      if(word & RocErrMask) {
	if(print) cout<<" NOR Error, "; // <<endl;
	status = -12;
	errorStatuses.push_back(12);
      }
      
      if(word &AutoMask) {
	if(print) cout<<" Autoreset, ";
	status = -13;
	errorStatuses.push_back(13);
      }
      
      if( (word&noTrailerMask)==noTrailerMask ) { // both bits noTrailer
	if(print) cout<<" noTrailer Error, "; // <<endl;
	status = -20;
	errorStatuses.push_back(20);
      } else if(word & overflowMask) { // bit 8 OV
	if(print) cout<<" OV Error, "; // <<endl;
	status = -14;
	errorStatuses.push_back(14);
      } else if(word &PKAMMask) { // bit 9 PKAM
	if(printDebug) print=true; // enable for this error
	if(print) cout<<" PKAM, ";
	status = -16;
	errorStatuses.push_back(16);
      }
      
    } // decode errors

  } // trailer&decode errors

  if(print && status <0) cout<<" FED "<<fed<<" channel "<<channel
			     <<" status "<<status
			     <<" "<<errorStatuses.size()<<endl;
  return status;
}
///////////////////////////////////////////////////////////////////////////
int MyDecode::data(int word, int & fedChannel, int fed, int & stat1, int & stat2, bool print) {

  //const int ROCMAX = 24;
  const unsigned int plsmsk = 0xff;   // pulse height
  const unsigned int pxlmsk = 0xff00; // pixel index
  const unsigned int dclmsk = 0x1f0000;

#ifdef PHASE1
  // for layer-1
  const unsigned int rowmsk = 0x7f00; 
  const unsigned int colmsk = 0x1f8000;
#endif
  // for both phase0 and phase1
  const unsigned int rocmsk  = 0x3e00000;   // 5 bits
  const unsigned int chnlmsk = 0xfc000000; // 6 bits 
  const unsigned int rocshift = 21;
  const unsigned int linkshift = 26;
  int status = 0;

  errorStatuses.clear();  // clear the error status vector for each word

  //bool bpix = (fed<1294); // identify bpix channels 

  roc_ = ((word&rocmsk)>>rocshift); // rocs start from 1
  // Check for embeded special words
  if(roc_>0 && roc_<25) {  // valid ROCs go from 1-24
    //if(print) cout<<"data "<<hex<<word<<dec;
    channel_ = ((word&chnlmsk)>>linkshift);

    if(channel_>0 && channel_ <= n_of_Channels) {  // valid channels 1-48
      //cout<<hex<<word<<dec;
      dcol_=(word&dclmsk)>>16;
      pix_=(word&pxlmsk)>>8;
      adc_=(word&plsmsk);
      fedChannel = channel_;

      //if(!phase1) {cout<<"must be phase1 "<<endl; return 0;}

      if(print || CHECK_PIXELS ) {  // info 

	string modName = getModName(fed,fedChannel);
	int layer = getLayer(fed,fedChannel);
	bool printOn = (print && (selectedChannel_==-1 || selectedChannel_==channel_) );

	// if(!FULL_DECODE) {
	//   col_=(word&colmsk)>>15;
	//   row_=(word&rowmsk)>>8;
	//   if(printOn) cout<<" Fed "<<fed<<" Channel- "<<channel_<<" ROC(order)- "<<(roc_-1)<<" DCOL- "
	// 		  <<dcol_<<" Pixel- "<<pix_<<" (OR col-"<<col_<<" row-"<<row_<<") ADC- "<<adc_<<endl;
	// }
	//} else {
	  //int roc=0;
	  //string tbm;
	  //string modName0 = MyConvert::moduleNameFromFedChan(fed,fedChannel,roc,tbm);
	  //int layer0 = MyConvert::layerFromName(modName0);
	  //if(bpix && (layer != layer0)) cout<<"wrong layer "<<layer<<" "<<layer0<<endl;
	  //if(bpix && (modName != modName0)) cout<<"wrong module name "<<modName<<" "<<modName0<<endl;
	  
	if(layer==1) { // for L1 
	  col_=(word&colmsk)>>15;  // from 0 to 51
	  row_=(word&rowmsk)>>8;   // from 0 to 59
	  dcol_ = col_/2;  // for layer 1 just calculate the dcol from col 
	  if(printOn) {
	    cout<<" Fed "<<fed<<" Channel- "<<channel_<<" Mod "<<modName<<" ROC(order,from 0)- "<<(roc_-1)
		<<" col- "<<col_<<" row- "<<row_<<" ADC- "<<adc_
		<<" layer1 "
		<<endl;
	    //if(col_==0  && row_==0) cout<<"for layer 1 there can be pix 0/0 hits"<<endl;
	  }
	} else { // layer 2-4
	  int colEvenOdd = pix_%2;  // module(2), 0-1st sol, 1-2nd col.
	  // Transform
	  col_ = dcol_ * 2 + colEvenOdd; // col address, starts from 0
	  row_ = abs( int(pix_/2) - 80); // row addres, starts from 0
	  if(printOn) cout<<" Fed "<<fed<<" Channel- "<<channel_<<" Mod "<<modName<<" ROC(order)- "<<(roc_-1)<<" DCOL- "
			  <<dcol_<<" Pixel- "<<pix_<<" col- "<<col_<<" row- "<<row_<<" ADC- "<<adc_<<endl;
	}
	//}
	
	status=1;

	if(CHECK_PIXELS) {
	  printOn = (printErrors && ( (selectedChannel_==-1) || (selectedChannel_==channel_) ) );

	  // Check invalid ROC numbers
	  if(roc_>8 ) {  //inv ROC, per channel max 8 rocs
	    if(printOn) 
	      cout<<"Wrong roc number - Fed "<<fed
		  <<" chan/roc(order)/dcol/pix/adc = "<<channel_<<"/"
		  <<roc_-1<<"/"<<dcol_<<"/"<<pix_<<"/"<<adc_<<endl;
	    status = -4;	
	    errorStatuses.push_back(4);
	  }

	  // Check pixels
	  if(layer!=1 && pix_==0) {  // PIX=0
	    // Detect pixel 0 events
	    if(printOn) 
	      cout<<"Pix=0 - Fed "<<fed
		  <<" chan/roc(order)/dcol/pix/adc = "<<channel_<<"/"<<roc_-1<<"/"
		  <<dcol_<<"/"<<pix_<<"/"<<adc_
		  <<" ("<<col_<<","<<row_<<")"
		  <<" mod "<<modName<<" layer "<<layer<<endl;
	    count0++;
	    //stat1 = roc_-1;
	    //stat2 = count0;
	    status = -5;
	    errorStatuses.push_back(5);
	  }	
    
	  // ADC=0
	  if(adc_==0) {  // ADC=0
	    if(printOn) 
	      cout<<"ADC=0 - Fed "<<fed
		  <<" chan/roc(order)/dcol/pix/adc = "<<channel_<<"/"<<roc_-1<<"/"
		  <<dcol_<<"/"<<pix_<<"/"<<adc_
		  <<" ("<<col_<<","<<row_<<")"
		  <<" mod "<<modName<<" layer "<<layer<<endl;
	    count0++;
	    //stat1 = roc_-1;
	    //stat2 = count0;
	    status = -1;
	    errorStatuses.push_back(1);
	  }	
    
	  if( fed==fed0 && channel_==chan0 && roc_==roc0 && dcol_==dcol0 && pix_==pix0 ) {
	    // detect multiple pixels in sequence  
	    count0++;
	    if(printOn) 
	      cout<<"Double pixel - Fed "<<fed<<" chan/roc(order)/dcol/pix/adc = "
		  <<channel_<<"/"<<roc_-1<<"/"<<dcol_<<"/"
		  <<pix_<<"/"<<adc_<<" ("<<col_<<","<<row_<<") "
		  <<" mod "<<modName<<" layer "<<layer<<endl;
	    //stat1 = roc_-1;
	    //stat2 = count0;
	    errorStatuses.push_back(6);
	    status = -6;
	  }

	  const bool checkOrder = true;
	  if(checkOrder) {
	    if(fed!=fed0 || channel_!=chan0 || roc_!=roc0) {
	      dcol0=-1;
	    } else {
	      if(dcol_<dcol0) {
	     	 if(printOn) cout<<"Dcol number lower "<<dcol_<<" "<<dcol0
				 <<" for fed/chan/roc "<<fed<<" "<<channel_<<" "<<(roc_-1)
				 <<"pix/adc/col/row "<<pix_<<"/"<<adc_<<" ("<<col_<<","<<row_<<") "
				 <<" mod "<<modName<<" layer "<<layer<<endl;
		status = -7;
		errorStatuses.push_back(7);

	      } else if(dcol_==dcol0 && col_==col0 && layer!=1) { // same col, skip L1
		// check pixel (row) order
		if( (((col_%2)==0)&&(row_<row0) ) ||  // for even cols rows should go up  
		    (((col_%2)==1)&&(row_>row0) ) ) {  // for odd cols rows should go down  
		   if(printOn) cout<<"Row number lower "<<row_<<" "<<row0<<" col "<<col_<<" "<<col0
				       <<" for fed/chan/roc "<<fed<<"/"<<channel_
				       <<"/"<<roc_<<" layer "<<layer<<" "<<modName<<endl;
		  status = -3;
		  errorStatuses.push_back(3);

		} // check pixel
	      } // ccheck dcol
	    } // check fed/chan
	  } // if checkOrder 

	  fed0 = fed; chan0 =channel_; roc0 =roc_; dcol0 =dcol_; pix0=pix_; col0=col_; row0=row_;

	} // check pixels

      } // info

    } else { // channel

      cout<<" Wrong channel "<<channel_<<" : "
	  <<" for FED "<<fed<<" Word "<<hex<<word<<dec<<endl;
      return -2;

    }

    //} else if(roc_==25) {  // ROC? 
    //unsigned int chan = ((word&chnlmsk)>>26);
    //cout<<"Wrong roc 25 "<<" in fed/chan "<<fed<<"/"<<chan<<endl;
    //status=-4;

    // now roc=25 goes to error processing 

  } else {  // error word

    //cout<<"error word "<<hex<<word<<dec;
    status=error(word, fedChannel, fed, stat1, stat2, print);

  }

  return status;
}

////////////////////////////////////////////////////////////////////////////

class SiPixelRawDump : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  SiPixelRawDump( const edm::ParameterSet& cfg);
  ~SiPixelRawDump() {}
  void beginJob() override;
  //void beginRun(const edm::EventSetup&) {}
  void endJob() override;
  /// get data, convert to digis attach againe to Event
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void analyzeHits(int fed, int channel);
  void analyzeErrors(int fed, int channel, int errorType, int status1, int status2);
  void analyzeFinal(int fed);

private:
  edm::ParameterSet theConfig;
  edm::EDGetTokenT<FEDRawDataCollection> rawData;

  int printVerbosity;
  int selectedFED, selectedChannel;
  unsigned long long selectedEvent;
  bool bpixOnly;
  double printThreshold;
  int makeTree;
  int countEvents, countAllEvents;
  int countTotErrors;
  int lastLS, firstLS;
  float sumPixels, sumFedSize, sumFedPixels[n_of_FEDs];
  //std::vector< std::pair<int,int> > maskedChannels, maskedChannels0;
  int fedErrorsPerType[30][n_of_FEDs][n_of_Channels];
  int fedErrors[n_of_FEDs][n_of_Channels];
  //int fedErrorsENE[n_of_FEDs][n_of_Channels];
  //int fedErrorsTime[n_of_FEDs][n_of_Channels];
  //int fedErrorsOver[n_of_FEDs][n_of_Channels];
  //int fedErrorsPKAM[n_of_FEDs][n_of_Channels];
  //int fedErrorsAutoReset[n_of_FEDs][n_of_Channels];
  //int fedErrorsAutoMask[n_of_FEDs][n_of_Channels];
  bool fedErrorsAutoMaskInEvent[n_of_FEDs][n_of_Channels];
  bool fedErrorsMaskedInEvent[n_of_FEDs][n_of_Channels];
  //int fedErrorsMask[n_of_FEDs][n_of_Channels];
  //int decodeErrors[n_of_FEDs][n_of_Channels];
  //int decodeErrors000[n_of_FEDs][n_of_Channels];  // pix 0 problem
  //int decodeErrorsDouble[n_of_FEDs][n_of_Channels];  // double pix  problem
  //int decodeErrorsRow[n_of_FEDs][n_of_Channels];  // row order  problem
  //int decodeErrorsDcol[n_of_FEDs][n_of_Channels];  // dcol order  problem
  //int layerIndex[n_of_FEDs][n_of_Channels];  // layer number
  int errorType[30];
  int countErrors[30];
  int fedId0;
  int max1,max2,max3,max4,max0,maxfed1,maxfed2,maxfed3,maxfed4,maxfed0,maxchan1,maxchan2,maxchan3,maxchan4,maxchan0 ;
  // to distribute information 
  int run, bx, lumiBlock;
  unsigned long long eventCMSSW;
  int countPixelsBPix, countPixelsFPix;
  int countPixelsBPix1, countPixelsBPix2,countPixelsBPix3,countPixelsBPix4;
  int countErrorsInFed, countErrorsInFed1, countErrorsInFed2;
  //bool saveLast, saveFirst;
  int layer_, ring_;
  int maskedPerEvent_[5]; // count masked channels per event, layer5=fpix
  int eventId, stat1, stat2;
  int hitsCut, hitsCut2;
  int fedchannelsize[n_of_Channels];
  //int pixelsPerChannel[n_of_Channels];
  bool errorInChannel[30][n_of_Channels];
  bool forcePrint;

#ifdef OUTFILE
  ofstream outfile;
#endif

  TH1D *hsize,*hsize0, *hsize1, *hsize2, *hsize3;
#ifdef IND_FEDS
  TH1D *hsizeFeds[n_of_FEDs];
#endif
  TH1D *hlumi, *horbit, *hbx, *hlumi0, *hbx0, *hbx1, *hbx7;

  TH1D *hpixels, *hpixels0, *hpixels1, *hpixels2, *hpixels3, *hpixels4;
  TH1D *htotPixels,*htotPixels0, *htotPixels1, *htotPixels2, *htotPixels3, *htotPixels4, *htotPixels5, 
    *htotPixels6, *htotPixels7, *htotPixels8;
  TH1D *hhitsPerRoc[6], *hhitsPerChannel[6];
  // Profiles 
  TProfile *hhitsPerRocOrder[6];
  TProfile *htotPixelsls,*hbpixPixelsls,*hbpixPixels1ls,*hbpixPixels2ls,
    *hbpixPixels3ls,*hbpixPixels4ls,*hfpixPixelsls;  
  TProfile *htotPixelsbx,*hbpixPixelsbx,*hbpixPixels1bx,*hbpixPixels2bx,
    *hbpixPixels3bx,*hbpixPixels4bx,*hfpixPixelsbx; 
  //TProfile *hpix1bx,*hpix2bx,*hpix3bx,*hpix4bx,*hpixfbx; 
  TProfile *herrorType1ls, *herrorType2ls,*herrorType1bx,*herrorType2bx;
  TProfile *hmaskedL1ls,*hmaskedL2ls,*hmaskedL3ls,*hmaskedL4ls,*hmaskedFls;
  TProfile *hadc1ls,*hadc2ls,*hadc3ls,*hadc4ls,*hadc0ls; 
  TProfile *hadc1bx,*hadc2bx,*hadc3bx,*hadc4bx,*hadc0bx; 


  TProfile2D *hfedchannelsize,*hfedchannelsizeFull,*hfedchannelsizeEff,
    *hfedfibersizediff; //
  TProfile2D *hfedchannelsize1,*hfedchannelsize2,*hfedchannelsize3,*hfedchannelsize4; 
  TProfile2D *hfedfibersize1,*hfedfibersize2,*hfedfibersize3,*hfedfibersize4,
    *hfedfibersizef; 

  TH1D *hfedchannelsizeb,*hfedchannelsizeb1,*hfedchannelsizeb2,
    *hfedchannelsizeb3,*hfedchannelsizeb4,*hfedchannelsizef;
  TH1D *hfedfibersizeb1,*hfedfibersizeb2,*hfedfibersizeb3,*hfedfibersizeb4,
    *hfedfibersizefpix;
  TH1D *hfedfiberdiffb1,*hfedfiberdiffb2,*hfedfiberdiffb3,*hfedfiberdiffb4;

  TH1D *hadc1,*hadc2,*hadc3,*hadc4,*hadc0; 
  //TH2F *hchannelRoc, *hchannelRocs, *hchannelPixels, *hchannelPixPerRoc;
  TH2F *hchannelFED;
  TProfile2D *hchannelFEDWords;
  TH2F *hfed2dErrors, *hsize2d, *hmanyHits;
  TProfile *hsizels,*havsizebx,*hsizep;

  // errors 
  TH1D *herrors, *htotErrors;
  TH1D *herrorType1, *herrorType1Fed, *herrorType2, *herrorType2Fed;
  TH2F *hfed2DErrorsType1,*hfed2DErrorsType2;
  TH2F *hfedErrorType1ls,*hfedErrorType2ls;
  TH2F *hchanErrorType1ls;

  // Per erroor
  TH2F *hfed2DError[30];
  TH2F *hchanErrorPerLS[30];
  TProfile *herrorlsP[30];
  TH1D *herrorls[30];

  //per layer 
  TH2F *hfedChannelDefinition;
  TH2F *hpix0Map[4],*hdoubleMap[4],*hdcolLowMap[4],*hpixOrderMap[4],*hadc0Map[4],*hadc0RocMap[4];
  TH1D *htest, *htest1, *htest2, *htest3, *htest4, *htest5, *htest6;

  // pixels in events with errors
  TH1D *hpixelsInErrorChannel[30];

  // Per FED
#ifdef PER_FED
  TProfile2D *hfedChanLS[94], *hfedChanAutoMaskedLS[94];
#endif

#ifdef IND_FEDS
  TH2F *hfed2DErrors1ls,*hfed2DErrors2ls,*hfed2DErrors3ls,*hfed2DErrors4ls,*hfed2DErrors5ls,
    *hfed2DErrors6ls,*hfed2DErrors7ls,*hfed2DErrors8ls,*hfed2DErrors9ls,*hfed2DErrors10ls,*hfed2DErrors11ls,*hfed2DErrors12ls,
    *hfed2DErrors13ls,*hfed2DErrors14ls,*hfed2DErrors15ls,*hfed2DErrors16ls;
#endif

#ifdef USE_TREE
  TTree *tree;
  int eventT,lsT,bxT,fedT,channelT,rocT,colT,rowT,errorT,layerT,ladderT,moduleT,adcT;
  int errorFed, errorChan;
#endif
  
  MyDecode decode;
};
//----------------------------------------------------------------------------------
SiPixelRawDump::SiPixelRawDump( const edm::ParameterSet& cfg) : theConfig(cfg) {
  usesResource("TFileService");
  string label = theConfig.getUntrackedParameter<std::string>("InputLabel","source");
  // For the ByToken method
  rawData = consumes<FEDRawDataCollection>(label);
  makeTree=0; // no trees
  forcePrint=false;
} 
//----------------------------------------------------------------------------------------
void SiPixelRawDump::endJob() {
  // 1 - adc=0
  // 2 - wrong channel
  // 3 - wrong pix 
  // 4 - wrong roc
  // 5 - pix=0
  // 6 - double pixel
  // 7 - wrong dcol order
  // 8 - ROC reset
  // 9 - NTP
  // 10 - TO 
  // 11 - ene
  // 12 - nor
  // 13 - autoreset 
  // 14 - overflow 
  // 15 - cal
  // 16 - pkam  
  // 17 - masked
  // 18 - automasked
  // 19 - tbm reset 
  // 20 - noTrailer
  // 21 - SyncTrig
  // 22 - StackFull
  // 23 - clearEVT
  // 24 - SyncErr 

  static string errorName[30] = {
    " ","adc0","wrong channel","wrong pix","wrong roc","pix=0",
    " double-pix","wrong dcol","rocReset","NTP","TO",
    "ENE","NOR","autoreset","overflow",
    "Cal","pkam","masked","automasked","tbmReset",
    "noTrailer","SyncTrig","StackFull","clearEVT","SyncErr"
  };

  cout<<" Error codes"<<endl;
  cout<<"Index Name"<<endl;
  for(int i=0;i<25;++i) {
    cout<<i<<" "<<errorName[i]<<endl;
  }

  double tmp = sumPixels;
  if(countEvents>0) {
    sumPixels /= float(countEvents);
    sumFedSize /= float(countAllEvents);
    for(int i = 0; i < n_of_FEDs; ++i) {
      sumFedPixels[i] /= float(countEvents);
      hpixels4->Fill(float(i),sumFedPixels[i]); //pixels per fed/event 
    }
  }
    
  cout<<" Total/non-empty events " <<countAllEvents<<" / "<<countEvents<<" average number of pixels "<<sumPixels<<" ("<<tmp<<")"<<endl;

  cout<<" Average Fed size per event for all events (in 4-words) "<< (sumFedSize*2./static_cast<float>(n_of_FEDs)) 
      <<" total for all feds "<<(sumFedSize*2.) <<endl;

  cout<<" Size for ech FED per event in units of hit pixels:" <<endl;

  for(int i = 0; i < n_of_FEDs; ++i) cout<< sumFedPixels[i]<<" ";
  cout<<endl;

  int errorThreshold = int(countEvents*printThreshold);
  //if(errorThreshold<100) errorThreshold=100;

  cout<<" Total number of errors "<<countTotErrors<<" print threshold "<< errorThreshold << " total errors per fed channel"<<endl;

  cout<<" FED errors "<<endl<<"Fed  Channel ENE-Errors  TO-Errors  NOR-Errors      PKAM      AutoMask   NTP  AutoReset"
      <<endl;
  // New counters
  for(int i = 0; i < n_of_FEDs; ++i) {
    for(int j=0;j<n_of_Channels;++j) {
      int layer = decode.getLayer(i+1200,j+1);
      if(layer==0) layer=5; // for fpix  
      hfedChannelDefinition->Fill(float(i), float(j+1), float(layer)); //make the chan definition histo
      if( (fedErrors[i][j] > errorThreshold) ) {
	cout<<(i+fedId0)<<" - "<<setw(3)<<(j+1)
	    <<" - "<<setw(8)<<fedErrorsPerType[11][i][j]  // ENE
	    <<" - "<<setw(8)<<fedErrorsPerType[10][i][j]  //TO
	    <<" - "<<setw(8)<<fedErrorsPerType[12][i][j] //NOR
	    <<" - "<<setw(8)<<fedErrorsPerType[16][i][j]   // PKAM
	    <<" - "<<setw(8)<<fedErrorsPerType[18][i][j]  //Automask
	  //<<"/"  <<setw(8)<<fedErrorsPerType[17][i][j] //Mask
	    <<" - "<<setw(8)<<fedErrorsPerType[9][i][j] //NTP
	    <<" - "<<setw(8)<<fedErrorsPerType[13][i][j]<<endl; //Autoreset
      } //if error
    } // chans
  }  //feds

  // for(int i = 0; i < n_of_FEDs; ++i) {
  //   for(int j=0;j<n_of_Channels;++j) if( (fedErrors[i][j] > errorThreshold) ) {
  // 	cout<<(i+fedId0)<<" - "<<setw(3)<<(j+1)<<" -  "<<setw(8)<<fedErrors[i][j]<<" - "<<setw(8)<<fedErrorsENE[i][j]
  // 	    <<" -  "<<setw(8)<<fedErrorsTime[i][j]<<" - "<<setw(8)<<fedErrorsOver[i][j]<<" - "<<setw(8)<<fedErrorsPKAM[i][j]
  // 	    <<" - "<<setw(8)<<fedErrorsAutoMask[i][j]<<"/"<<setw(8)<<fedErrorsMask[i][j]<<" - "<<setw(8)<<fedErrorsAutoReset[i][j]<<endl;
  //   }
  // }


  cout<<" Decode errors "<<endl<<"Fed Channel ADC0  Pix_000 Double_Pix Row-order Dcol-order"<<endl;
  errorThreshold = int(countEvents*printThreshold);
  //if(errorThreshold<10) errorThreshold=10;
  for(int i = 0; i < n_of_FEDs; ++i) {
    for(int j=0;j<n_of_Channels;++j) {
      int tmp=0;
      for(int n=2;n<8;++n)  {tmp += fedErrorsPerType[n][i][j];}
      tmp += fedErrorsPerType[1][i][j]/100.; // scale adc0 errors by 1/100
      if(tmp>errorThreshold) // very arbitray                        
	cout<<" "<<(i+fedId0)<<" -  "<<(j+1)<<"   -  "
	    <<fedErrorsPerType[1][i][j]<<"  -    "     // roc
	    <<fedErrorsPerType[5][i][j]<<"  -   "   // pix=0
	    <<fedErrorsPerType[6][i][j]<<"  -  "  // double pix
	    <<fedErrorsPerType[3][i][j]<<"  -  " // bad row
	    <<fedErrorsPerType[7][i][j]  // bad dcol
	    <<endl;
    }
  }

  //cout<<" Decode errors "<<endl<<"Fed Channel Other Pix_000 Double_Pix Row-order Dcol-order"<<endl;
  // for(int i = 0; i < n_of_FEDs; ++i) {
  //   for(int j=0;j<n_of_Channels;++j) {
  //     int tmp = decodeErrors[i][j] + decodeErrors000[i][j] + decodeErrorsDouble[i][j] + decodeErrorsRow[i][j]+ decodeErrorsDcol[i][j];
  //     if(tmp>10) 
  // 	cout<<" "<<(i+fedId0)<<" -  "<<(j+1)<<"   -  "
  // 	    <<decodeErrors[i][j]<<"  -    "
  // 	    <<decodeErrors000[i][j]<<"  -   "
  // 	    <<decodeErrorsDouble[i][j]<<"  -  "
  // 	    <<decodeErrorsRow[i][j]<<"  -  "
  // 	    <<decodeErrorsDcol[i][j]
  // 	    <<endl;
  //   }
  // }

  cout<<" Total errors for all feds "<<endl<<" Type Name Num-Of-Errors"<<endl;
  for(int i=0;i<30;++i) {
    if( errorType[i]>0 && i!=17 ) cout<<"   "<<i<<" - "<<errorName[i]<<" - "<<errorType[i]<<endl;
  }
  cout<<"max pixels per channel L1/2/3/4/FPix - "
      <<max1<<" "<<max2<<" "<<max3<<" "<<max4<<" "<<max0
      <<maxfed1<<" "<<maxfed2<<" "<<maxfed3<<" "<<maxfed4<<" "<<maxfed0
      <<maxchan1<<" "<<maxchan2<<" "<<maxchan3<<" "<<maxchan4<<" "<<maxchan0
      <<endl;;

  float norm=1.;
  if(countEvents>0) norm=1./float(countEvents);
  for(int i=1;i<30;++i) {
    hfed2DError[i]->Scale(norm);
  } 

#ifdef OUTFILE
  outfile.close();
#endif

}
//----------------------------------------------------------------------
void SiPixelRawDump::beginJob() {

  printVerbosity = theConfig.getUntrackedParameter<int>("Verbosity",1);
  printThreshold = theConfig.getUntrackedParameter<double>("PrintThreshold",0.01); // threshold per event for printing errors
  selectedFED = theConfig.getUntrackedParameter<int>("selectedFED",-1);
  selectedChannel = theConfig.getUntrackedParameter<int>("selectedChannel",-1);
  selectedEvent = theConfig.getUntrackedParameter<long long>("selectedEvent",0); 
  // cut on number of hits per roc for warning  
  hitsCut = theConfig.getUntrackedParameter<int>("hitsCut",1000);  
  hitsCut2 = theConfig.getUntrackedParameter<int>("hitsCut2",1000);  
  bpixOnly = theConfig.getUntrackedParameter<bool>("bpixOnly",false);   
#ifdef USE_TREE
  makeTree = theConfig.getUntrackedParameter<int>("makeTree",0);   
#endif 
  
  cout<<" beginjob "<<printVerbosity<<" "<<printThreshold<<" select FED "<<selectedFED
      <<" select Event "<<selectedEvent<<" tree "<<makeTree<<endl;  

  if(printVerbosity>0) printErrors  = true;
  else printErrors = false;
  if(printVerbosity>1) printData  = true;
  else printData = false;
  if(printVerbosity>2) printHeaders  = true;
  else printHeaders = false;

  decode.setPrint(selectedFED, selectedChannel);

#ifdef PHASE1
  //std::pair<int,int> fedIds(1200,1338); // phase 1
  fedId0=1200;
#else // phase0
  //std::pair<int,int> fedIds(FEDNumbering::MINSiPixelFEDID, FEDNumbering::MAXSiPixelFEDID); //0
  fedId0=0;
#endif

  max1=max2=max3=max4=max0=0;
  maxfed1=maxfed2=maxfed3=maxfed4=maxfed0=0;
  maxchan1=maxchan2=maxchan3=maxchan4=maxchan0=0;
  countEvents=0;
  countAllEvents=0;
  countTotErrors=0;
  sumPixels=0.;
  sumFedSize=0;
  lastLS=0; firstLS=9999;
  //maskedChannels.clear();
  //maskedChannels0.clear();
  //string tbm=" ";
  //int roc=-1;
  for(int i = 0; i < n_of_FEDs; ++i) {
    sumFedPixels[i]=0;
    for(int j=0;j<n_of_Channels;++j) {
      //decodeErrors[i][j]=0; decodeErrors000[i][j]=0; decodeErrorsDouble[i][j]=0;
      //decodeErrorsRow[i][j]=0; decodeErrorsDcol[i][j]=0;
      fedErrors[i][j]=0; 
      //fedErrorsENE[i][j]=0; fedErrorsTime[i][j]=0; 
      //fedErrorsOver[i][j]=0;fedErrorsPKAM[i][j]=0;fedErrorsAutoReset[i][j]=0;
      //fedErrorsAutoMask[i][j]=0;fedErrorsMask[i][j]=0;
      fedErrorsAutoMaskInEvent[i][j]=false;
      fedErrorsMaskedInEvent[i][j]=false;
      for(int n=0;n<30;++n) {fedErrorsPerType[n][i][j]=0;}

      //cout<<"Build the layer index table. Is it used?"<<endl;
      // layerIndex[i][j]=-1;
      // if( i > fedIdBpixMax ) layerIndex[i][j]=0; // signal fpix
      // else {
      // 	// Get the module name and tbm type 
      // 	//string modName = MyConvert::moduleNameFromFedChan((i+fedId0),(j+1),roc,tbm);
      // 	string modName = decode.getModName((i+fedId0),(j+1));
      // 	if(modName != "") { // skip nonexistant (empty) channels 
      // 	  //int layer = MyConvert::layerFromName(modName);
      // 	  int layer = decode.getLayer( (i+fedId0), (j+1) );
      // 	  if(layer>=0 && layer<=4) layerIndex[i][j]=layer;
      // 	  else cout<<"error "<<(i+fedId0)<<" "<<(j+1)<<" "<<modName<<" "<<layer<<endl;
      // 	  //cout<<(i+fedId0)<<" "<<(j+1)<<" "<<modName<<" "<<layer<<endl;
      // 	}	
      // }

    } // CHAN
  } // fed
   
  for(int i=0;i<30;++i) errorType[i]=0;

  edm::Service<TFileService> fs;

  const float pixMax = 5999.5;   // pp value 
  const float totMax = 149999.5;  // pp value 
  //const float maxLink = 500.;    // pp value

  //const float pixMax = 19999.5;  // hi value 
  //const float totMax = 399999.5; // hi value 
  const float maxLink = 1000.;   // hi value
  const float maxChan = static_cast<float>(n_of_Channels) + 0.5;
  const int maxLS=1000;
  hsize  = fs->make<TH1D>( "hsize", "FED event size in words-4(incl err)", 6000, -0.5, pixMax);
  hsize0 = fs->make<TH1D>( "hsize0", "FED event size in words-4(zoomed)", 2000, -0.5, 1999.5);
  hsize1 = fs->make<TH1D>( "hsize1", "bpix FED event size in words-4", 6000, -0.5, pixMax);
  hsize2 = fs->make<TH1D>( "hsize2", "fpix FED event size in words-4", 6000, -0.5, pixMax);
  hsize3 = fs->make<TH1D>( "hsize3", "ave bpix FED event size in words-4", 6000, -0.5, pixMax);

  hpixels  = fs->make<TH1D>( "hpixels", "pixels per FED (zoomed)", 2000, -0.5, 1999.5);
  hpixels0 = fs->make<TH1D>( "hpixels0", "pixels per FED", 6000, -0.5, pixMax);
  hpixels1 = fs->make<TH1D>( "hpixels1", "pixels >0 per FED", 6000, -0.5, pixMax);
  hpixels2 = fs->make<TH1D>( "hpixels2", "pixels >0 per BPix FED", 6000, -0.5, pixMax);
  hpixels3 = fs->make<TH1D>( "hpixels3", "pixels >0 per Fpix FED", 6000, -0.5, pixMax);
  hpixels4 = fs->make<TH1D>( "hpixels4", "pixels per each FED", n_of_FEDs, -0.5, static_cast<float>(n_of_FEDs) - 0.5);

  htotPixels  = fs->make<TH1D>( "htotPixels", "pixels per event", 10000, -0.5, totMax);
  htotPixels0 = fs->make<TH1D>( "htotPixels0", "pixels per event, zoom low region", 20000, -0.5, 19999.5);
  htotPixels1 = fs->make<TH1D>( "htotPixels1", "pixels >0 per event", 10000, -0.5, totMax);
#ifdef CHECK_BX
  htotPixels2 = fs->make<TH1D>( "htotPixels2", "pixels per event for wrong BX", 10000, -0.5, totMax);
#endif
  htotPixels3 = fs->make<TH1D>( "htotPixels3", "tot pixels bpix ", 10000, -0.5, totMax);
  htotPixels4 = fs->make<TH1D>( "htotPixels4", "tot pixels fpix" , 10000, -0.5, totMax);
  htotPixels5 = fs->make<TH1D>( "htotPixels5", "tot pixels bpix1", 10000, -0.5, totMax);
  htotPixels6 = fs->make<TH1D>( "htotPixels6", "tot pixels bpix2", 10000, -0.5, totMax);
  htotPixels7 = fs->make<TH1D>( "htotPixels7", "tot pixels bpix3", 10000, -0.5, totMax);
  htotPixels8 = fs->make<TH1D>( "htotPixels8", "tot pixels bpix4", 10000, -0.5, totMax);

  hchannelFED = fs->make<TH2F>("hchannelFED", "channel-FED hits",
			       n_of_FEDs, -0.5, static_cast<float>(n_of_FEDs) - 0.5,
			       48,0.,48.);
  hchannelFEDWords = fs->make<TProfile2D>("hchannelFEDWords", "channel-FED words",
			       n_of_FEDs, -0.5, static_cast<float>(n_of_FEDs) - 0.5,
					  48,0.,48.,0.,10000.);
  hfedChannelDefinition = fs->make<TH2F>("hfedChannelDefinition", "define channel-FED 1,2,3,4,5",
			       n_of_FEDs, -0.5, static_cast<float>(n_of_FEDs) - 0.5,
			       48,0.,48.);

  hmanyHits = fs->make<TH2F>("hmanyHits", "channel-FED events with many hits",
			       n_of_FEDs, -0.5, static_cast<float>(n_of_FEDs) - 0.5,
			       48,0.,48.);  
#ifdef IND_FEDS
  hsizeFeds[0] = fs->make<TH1D>( "hsizeFed0", "FED 0 event size ", 1000, -0.5, pixMax);
  hsizeFeds[1] = fs->make<TH1D>( "hsizeFed1", "FED 1 event size ", 1000, -0.5, pixMax);
  hsizeFeds[2] = fs->make<TH1D>( "hsizeFed2", "FED 2 event size ", 1000, -0.5, pixMax);
  hsizeFeds[3] = fs->make<TH1D>( "hsizeFed3", "FED 3 event size ", 1000, -0.5, pixMax);
  hsizeFeds[4] = fs->make<TH1D>( "hsizeFed4", "FED 4 event size ", 1000, -0.5, pixMax);
  hsizeFeds[5] = fs->make<TH1D>( "hsizeFed5", "FED 5 event size ", 1000, -0.5, pixMax);
  hsizeFeds[6] = fs->make<TH1D>( "hsizeFed6", "FED 6 event size ", 1000, -0.5, pixMax);
  hsizeFeds[7] = fs->make<TH1D>( "hsizeFed7", "FED 7 event size ", 1000, -0.5, pixMax);
  hsizeFeds[8] = fs->make<TH1D>( "hsizeFed8", "FED 8 event size ", 1000, -0.5, pixMax);
  hsizeFeds[9] = fs->make<TH1D>( "hsizeFed9", "FED 9 event size ", 1000, -0.5, pixMax);
  hsizeFeds[10] = fs->make<TH1D>( "hsizeFed10", "FED 10 event size ", 1000, -0.5, pixMax);
  hsizeFeds[11] = fs->make<TH1D>( "hsizeFed11", "FED 11 event size ", 1000, -0.5, pixMax);
  hsizeFeds[12] = fs->make<TH1D>( "hsizeFed12", "FED 12 event size ", 1000, -0.5, pixMax);
  hsizeFeds[13] = fs->make<TH1D>( "hsizeFed13", "FED 13 event size ", 1000, -0.5, pixMax);
  hsizeFeds[14] = fs->make<TH1D>( "hsizeFed14", "FED 14 event size ", 1000, -0.5, pixMax);
  hsizeFeds[15] = fs->make<TH1D>( "hsizeFed15", "FED 15 event size ", 1000, -0.5, pixMax);
  hsizeFeds[16] = fs->make<TH1D>( "hsizeFed16", "FED 16 event size ", 1000, -0.5, pixMax);
  hsizeFeds[17] = fs->make<TH1D>( "hsizeFed17", "FED 17 event size ", 1000, -0.5, pixMax);
  hsizeFeds[18] = fs->make<TH1D>( "hsizeFed18", "FED 18 event size ", 1000, -0.5, pixMax);
  hsizeFeds[19] = fs->make<TH1D>( "hsizeFed19", "FED 19 event size ", 1000, -0.5, pixMax);
  hsizeFeds[20] = fs->make<TH1D>( "hsizeFed20", "FED 20 event size ", 1000, -0.5, pixMax);
  hsizeFeds[21] = fs->make<TH1D>( "hsizeFed21", "FED 21 event size ", 1000, -0.5, pixMax);
  hsizeFeds[22] = fs->make<TH1D>( "hsizeFed22", "FED 22 event size ", 1000, -0.5, pixMax);
  hsizeFeds[23] = fs->make<TH1D>( "hsizeFed23", "FED 23 event size ", 1000, -0.5, pixMax);
  hsizeFeds[24] = fs->make<TH1D>( "hsizeFed24", "FED 24 event size ", 1000, -0.5, pixMax);
  hsizeFeds[25] = fs->make<TH1D>( "hsizeFed25", "FED 25 event size ", 1000, -0.5, pixMax);
  hsizeFeds[26] = fs->make<TH1D>( "hsizeFed26", "FED 26 event size ", 1000, -0.5, pixMax);
  hsizeFeds[27] = fs->make<TH1D>( "hsizeFed27", "FED 27 event size ", 1000, -0.5, pixMax);
  hsizeFeds[28] = fs->make<TH1D>( "hsizeFed28", "FED 28 event size ", 1000, -0.5, pixMax);
  hsizeFeds[29] = fs->make<TH1D>( "hsizeFed29", "FED 29 event size ", 1000, -0.5, pixMax);
  hsizeFeds[30] = fs->make<TH1D>( "hsizeFed30", "FED 30 event size ", 1000, -0.5, pixMax);
  hsizeFeds[31] = fs->make<TH1D>( "hsizeFed31", "FED 31 event size ", 1000, -0.5, pixMax);
  hsizeFeds[32] = fs->make<TH1D>( "hsizeFed32", "FED 32 event size ", 1000, -0.5, pixMax);
  hsizeFeds[33] = fs->make<TH1D>( "hsizeFed33", "FED 33 event size ", 1000, -0.5, pixMax);
  hsizeFeds[34] = fs->make<TH1D>( "hsizeFed34", "FED 34 event size ", 1000, -0.5, pixMax);
  hsizeFeds[35] = fs->make<TH1D>( "hsizeFed35", "FED 35 event size ", 1000, -0.5, pixMax);
  hsizeFeds[36] = fs->make<TH1D>( "hsizeFed36", "FED 36 event size ", 1000, -0.5, pixMax);
  hsizeFeds[37] = fs->make<TH1D>( "hsizeFed37", "FED 37 event size ", 1000, -0.5, pixMax);
  hsizeFeds[38] = fs->make<TH1D>( "hsizeFed38", "FED 38 event size ", 1000, -0.5, pixMax);
  hsizeFeds[39] = fs->make<TH1D>( "hsizeFed39", "FED 39 event size ", 1000, -0.5, pixMax);
#endif

  //hevent = fs->make<TH1D>("hevent","event",1000,0,10000000.);
  //horbit = fs->make<TH1D>("horbit","orbit",100, 0,100000000.);
  hlumi0   = fs->make<TH1D>("hlumi0","lumi-section all",maxLS,0,float(maxLS));
  hlumi  = fs->make<TH1D>("hlumi","lumi-section pix>0",maxLS,0,float(maxLS));
 
  hbx    = fs->make<TH1D>("hbx",   "bx (cmssw) with hits",4000,0,4000.);  
  hbx0    = fs->make<TH1D>("hbx0",   "bx (cmssw) all",    4000,0,4000.);  
  hbx1    = fs->make<TH1D>("hbx1",   "bx fed payload",    4000,0,4000.);  
  //hbx2    = fs->make<TH1D>("hbx2",   "bx fed errors",    4000,0,4000.);  
  //hbx3    = fs->make<TH1D>("hbx3",   "bx fed errors",    4000,0,4000.);  
  //hbx4    = fs->make<TH1D>("hbx4",   "bx fed errors",    4000,0,4000.);  
  //hbx5    = fs->make<TH1D>("hbx5",   "bx fed errors",    4000,0,4000.);  
  //hbx6    = fs->make<TH1D>("hbx6",   "bx fed errors",    4000,0,4000.);  
#ifdef CHECK_BX
  hbx7    = fs->make<TH1D>("hbx7",   "bad (cmssw) bx",    4000,0,4000.);  
#endif
  hsize2d = fs->make<TH2F>( "hsize2d", "size in words vs fed",n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5, 100,0,1000); // ALL
  hsizep  = fs->make<TProfile>( "hsizep", "size in wordsvs fed",n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5,0,100000); // ALL
  //hsize2dls = fs->make<TH2F>( "hsize2dls", "size vs lumi",100,0,1000, 50,0.,500.); // ALL
  hsizels = fs->make<TProfile>("hsizels"," bpix fed size vs ls",          maxLS,0,float(maxLS),0,200000.);  
  htotPixelsls = fs->make<TProfile>("htotPixelsls"," tot pixels vs ls",   maxLS,0,float(maxLS),0,300000.);
  hbpixPixelsls = fs->make<TProfile>("hbpixPixelsls"," bpix pixels vs ls",maxLS,0,float(maxLS),0,300000.);
  hbpixPixels1ls = fs->make<TProfile>("hbpixPixels1ls","bpix l1 pix vs ls",maxLS,0,float(maxLS),0,300000.);
  hbpixPixels2ls = fs->make<TProfile>("hbpixPixels2ls","bpix l2 pix vs ls",maxLS,0,float(maxLS),0,300000.);
  hbpixPixels3ls = fs->make<TProfile>("hbpixPixels3ls","bpix l3 pix vs ls",maxLS,0,float(maxLS),0,300000.);
  hbpixPixels4ls = fs->make<TProfile>("hbpixPixels4ls","bpix l4 pix vs ls",maxLS,0,float(maxLS),0,300000.);
  hfpixPixelsls = fs->make<TProfile>("hfpixPixelsls"," fpix pixels vs ls",maxLS,0,float(maxLS),0,300000.);

  
  htotPixelsbx = fs->make<TProfile>("htotPixelsbx"," tot pixels vs bx", 4000,-0.5,3999.5,0,300000.);
  hbpixPixelsbx = fs->make<TProfile>("hbpixPixelsbx","bpix pixels vs bx", 4000,-0.5,3999.5,0,300000.);
  hfpixPixelsbx = fs->make<TProfile>("hfpixPixelsbx","fpix pixels vs bx", 4000,-0.5,3999.5,0,300000.);
  hbpixPixels1bx = fs->make<TProfile>("hbpixPixels1bx","bpix1 pixels vs bx", 4000,-0.5,3999.5,0,300000.);
  hbpixPixels2bx = fs->make<TProfile>("hbpixPixels2bx","bpix2 pixels vs bx", 4000,-0.5,3999.5,0,300000.);
  hbpixPixels3bx = fs->make<TProfile>("hbpixPixels3bx","bpix3 pixels vs bx", 4000,-0.5,3999.5,0,300000.);
  hbpixPixels4bx = fs->make<TProfile>("hbpixPixels4bx","bpix4 pixels vs bx", 4000,-0.5,3999.5,0,300000.);

  havsizebx = fs->make<TProfile>("havsizebx"," ave bpix fed size vs bx",4000,-0.5,3999.5,0,300000.);

  hfedchannelsize  = fs->make<TProfile2D>("hfedchannelsize", "pixels per fed&channel",
					  n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5,
					  n_of_Channels, 0.5,maxChan,0.0,10000.);  
  hfedchannelsizeFull = fs->make<TProfile2D>("hfedchannelsizeFull", "pixels per fed&channel >0",
					  n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5,
					  n_of_Channels, 0.5,maxChan,0.0,10000.);  
  hfedchannelsizeEff = fs->make<TProfile2D>("hfedchannelsizeEff", ">0packets fed&channel",
					  n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5,
					  n_of_Channels, 0.5,maxChan,0.0,10000.);  
  hfedchannelsize1 = fs->make<TProfile2D>("hfedchannelsize1", "pixels per fed&channel L1",
					  n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5,
					  n_of_Channels, 0.5,maxChan,0.0,10000.);  
  hfedchannelsize2 = fs->make<TProfile2D>("hfedchannelsize2", "pixels per fed&channel L2",
					  n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5,
					  n_of_Channels, 0.5,maxChan,0.0,10000.);  
  hfedchannelsize3 = fs->make<TProfile2D>("hfedchannelsize3", "pixels per fed&channel L3",
					  n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5,
					  n_of_Channels, 0.5,maxChan,0.0,10000.);  
  hfedchannelsize4 = fs->make<TProfile2D>("hfedchannelsize4", "pixels per fed&channel L4",
					  n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5,
					  n_of_Channels, 0.5,maxChan,0.0,10000.);  
  hfedchannelsizeb   = fs->make<TH1D>("hfedchannelsizeb", "pixels per bpix channel",  int(maxLink),0.0,maxLink);
  hfedchannelsizeb1  = fs->make<TH1D>("hfedchannelsizeb1", "pixels per bpix1 channel",int(maxLink),0.0,maxLink);
  hfedchannelsizeb2  = fs->make<TH1D>("hfedchannelsizeb2", "pixels per bpix2 channel",int(maxLink),0.0,maxLink);
  hfedchannelsizeb3  = fs->make<TH1D>("hfedchannelsizeb3", "pixels per bpix3 channel",int(maxLink),0.0,maxLink);
  hfedchannelsizeb4  = fs->make<TH1D>("hfedchannelsizeb4", "pixels per bpix4 channel",int(maxLink),0.0,maxLink);
  hfedchannelsizef   = fs->make<TH1D>("hfedchannelsizef", "pixels per fpix channel",  int(maxLink),0.0,maxLink);



  const int maxFiber=24; const float maxFiberF=23.5;
  hfedfibersizediff = fs->make<TProfile2D>("hfedfibersizediff", 
					   "fed&channel size diff",
					     n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5,
					     maxFiber, -0.5,maxFiberF,0.0,10000.);  

  hfedfibersize1 = fs->make<TProfile2D>("hfedfibersize1", "max chan size - fed&fibre L1",
					n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5,
					maxFiber, -0.5,maxFiberF,0.0,10000.);  
  hfedfibersize2 = fs->make<TProfile2D>("hfedfibersize2", "max chan size - fed&fibre L2",
					n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5,
					maxFiber, -0.5,maxFiberF,0.0,10000.);  
  hfedfibersize3 = fs->make<TProfile2D>("hfedfibersize3", "max chan size - fed&fibre L3",
					n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5,
					maxFiber, -0.5,maxFiberF,0.0,10000.);  
  hfedfibersize4 = fs->make<TProfile2D>("hfedfibersize4", "max chan size - fed&fibre L4",
					n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5,
					maxFiber, -0.5,maxFiberF,0.0,10000.);  
  hfedfibersizef = fs->make<TProfile2D>("hfedfibersizef", "max chan size - fed&fibre fpix",
					n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5,
					maxFiber, -0.5,maxFiberF,0.0,10000.);  
  hfedfibersizeb1  = fs->make<TH1D>("hfedfibersizeb1", "pixels per bpix1 channel max of fiber",int(maxLink),0.0,maxLink);
  hfedfibersizeb2  = fs->make<TH1D>("hfedfibersizeb2", "pixels per bpix2 channel max of fiber",int(maxLink),0.0,maxLink);
  hfedfibersizeb3  = fs->make<TH1D>("hfedfibersizeb3", "pixels per bpix3 channel max of fiber",int(maxLink),0.0,maxLink);
  hfedfibersizeb4  = fs->make<TH1D>("hfedfibersizeb4", "pixels per bpix4 channel max of fiber",int(maxLink),0.0,maxLink);
  hfedfibersizefpix= fs->make<TH1D>("hfedfibersizefpix", "pixels per fpix channel max of fiber",  int(maxLink),0.0,maxLink);

  hfedfiberdiffb1   = fs->make<TH1D>("hfedfiberdiffb1", "L1 packet diff",700,0.0,700.);
  hfedfiberdiffb2   = fs->make<TH1D>("hfedfiberdiffb2", "L2 packet diff",700,0.0,700.);
  hfedfiberdiffb3   = fs->make<TH1D>("hfedfiberdiffb3", "L3 packet diff",700,0.0,700.);
  hfedfiberdiffb4   = fs->make<TH1D>("hfedfiberdiffb4", "L4 packet diff",700,0.0,700.);

  hadc1 = fs->make<TH1D>("hadc1","adc lay 1",255,0.,255.);
  hadc2 = fs->make<TH1D>("hadc2","adc lay 2",255,0.,255.);
  hadc3 = fs->make<TH1D>("hadc3","adc lay 3",255,0.,255.);
  hadc4 = fs->make<TH1D>("hadc4","adc lay 4",255,0.,255.);
  hadc0 = fs->make<TH1D>("hadc0","adc fpix", 255,0.,255.);

  hadc1ls = fs->make<TProfile>("hadc1ls","adc1 vs ls",maxLS,0,float(maxLS),     0.,255.);
  hadc1bx = fs->make<TProfile>("hadc1bx","adc1 vs bx",4000,-0.5,3999.5,0.,255.);
  hadc2ls = fs->make<TProfile>("hadc2ls","adc2 vs ls",maxLS,0,float(maxLS),     0.,255.);
  hadc2bx = fs->make<TProfile>("hadc2bx","adc2 vs bx",4000,-0.5,3999.5,0.,255.);
  hadc3ls = fs->make<TProfile>("hadc3ls","adc3 vs ls",maxLS,0,float(maxLS),     0.,255.);
  hadc3bx = fs->make<TProfile>("hadc3bx","adc3 vs bx",4000,-0.5,3999.5,0.,255.);
  hadc4ls = fs->make<TProfile>("hadc4ls","adc4 vs ls",maxLS,0,float(maxLS),     0.,255.);
  hadc4bx = fs->make<TProfile>("hadc4bx","adc4 vs bx",4000,-0.5,3999.5,0.,255.);
  hadc0ls = fs->make<TProfile>("hadc0ls","adcf vs ls",maxLS,0,float(maxLS),     0.,255.);
  hadc0bx = fs->make<TProfile>("hadc0bx","adcf vs bx",4000,-0.5,3999.5,0.,255.);

  herrors = fs->make<TH1D>( "herrors", "FED errors per event/fed", 100, -0.5, 99.5);
  htotErrors = fs->make<TH1D>( "htotErrors", "Total errors per event", 1000, -0.5, 999.5);
  hfed2dErrors = fs->make<TH2F>( "hfed2dErrors", "error type versus fed#", n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs)-0.5,
			   21, -0.5, 20.5); // ALL

  herrorType1     = fs->make<TH1D>( "herrorType1", "fed errors per type", 
				    30, -0.5, 29.5);
  herrorType1Fed  = fs->make<TH1D>( "herrorType1Fed", "fed errors per FED", 
				    n_of_FEDs, -0.5, static_cast<float>(n_of_FEDs) - 0.5);
  //herrorType1Chan = fs->make<TH1D>( "herrorType1Chan", "errors-1(fed) per chan", 
  //				    n_of_Channels, 0.5,maxChan);
  hfed2DErrorsType1 = fs->make<TH2F>("hfed2DErrorsType1", "fed errors per FED&chan", 
	  n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5, n_of_Channels,0.5,maxChan);

  hfedErrorType1ls = fs->make<TH2F>( "hfedErrorType1ls", "FEDs with fed-errors vs lumi",
          maxLS,0,float(maxLS), n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5); // 
  hchanErrorType1ls = fs->make<TH2F>( "hchanErrorType1ls", "Chans with fed-errors vs lumi",
				      maxLS,0,float(maxLS), n_of_Channels,0.5,maxChan); // 
  herrorType1ls = fs->make<TProfile>("herrorType1ls","fed error vs ls",maxLS,0,float(maxLS),0,1000.);
  herrorType1bx = fs->make<TProfile>("herrorType1bx","fed error vs bx",4000,-0.5,3999.5,0,300000.);


  // errors 2
  herrorType2     = fs->make<TH1D>( "herrorType2", "readout decode errors per type", 
				    30, -0.5, 29.5);
  herrorType2Fed  = fs->make<TH1D>( "herrorType2Fed", "readout decode errors per FED", 
				    n_of_FEDs, -0.5, static_cast<float>(n_of_FEDs) - 0.5);

  //herrorType2Chan = fs->make<TH1D>( "herrorType2Chan", "readout errors type-2 (decode) per chan", 
  //				    n_of_Channels, 0.5,maxChan);
  hfed2DErrorsType2 = fs->make<TH2F>("hfed2DErrorsType2", "decode errors vs FED&chan", 
	  n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5, n_of_Channels, 0.5,maxChan);
  hfedErrorType2ls = fs->make<TH2F>( "hfedErrorType2ls", "FEDs with decode errors vs lumi",
          maxLS,0,float(maxLS), n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5); //
  herrorType2ls = fs->make<TProfile>("herrorType2ls","decode errors vs ls",maxLS,0,float(maxLS),0,1000.);
  herrorType2bx = fs->make<TProfile>("herrorType2bx","decode errors vs bx",4000,-0.5,3999.5,0,300000.);

  //hsizels = fs->make<TProfile>("hsizels"," bpix fed size vs ls",          maxLS,0,float(maxLS),0,200000.);  
  hmaskedL1ls = fs->make<TProfile>("hmaskedL1ls","L1 masked chans vs ls"
				    ,maxLS,0,float(maxLS),0,1000.);
  hmaskedL2ls = fs->make<TProfile>("hmaskedL2ls","L2 masked chans vs ls"
				    ,maxLS,0,float(maxLS),0,1000.);
  hmaskedL3ls = fs->make<TProfile>("hmaskedL3ls","L3 masked chans vs ls"
				    ,maxLS,0,float(maxLS),0,1000.);
  hmaskedL4ls = fs->make<TProfile>("hmaskedL4ls","L4 masked chans vs ls"
				    ,maxLS,0,float(maxLS),0,1000.);
  hmaskedFls = fs->make<TProfile>("hmaskedFls","FPix masked chans vs ls"
				    ,maxLS,0,float(maxLS),0,1000.);

  htest = fs->make<TH1D>("htest", "channel sum per fibre L1",100,0.,500.);
  htest1 = fs->make<TH1D>("htest1", "event diff",255,0.,255);
  htest2 = fs->make<TH1D>("htest2", "event diff",255,0.,255);
  htest3 = fs->make<TH1D>("htest3", "event diff ",512,-255.,255);
  htest4 = fs->make<TH1D>("htest4", "event diff ",512,-255.,255);
  htest5 = fs->make<TH1D>("htest5", "event diff ",512,-255.,255);

  string name, title;
  // roc order 
  for(int i=0;i<6;++i) {
    string num = std::to_string(i+1);
    string part="";
    if(i<4) part=" LYR"+to_string(i+1);
    else part=" RING"+std::to_string(i-3);
    name="hhitsPerRocOrder"+num; title="Hits Per Roc in"+part;        
    hhitsPerRocOrder[i]=fs->make<TProfile>(name.c_str(),title.c_str(),
					   8,0.,8.);
    name="hhitsPerRoc"+num; title="Hits Per Roc in"+part;        
    hhitsPerRoc[i] = fs->make<TH1D>(name.c_str(),title.c_str(),
			       1000, -0.5,999.5);
    name="hhitsPerChannel"+num; title="Hits Per Channel in"+part;
    hhitsPerChannel[i] = fs->make<TH1D>(name.c_str(),title.c_str(),
			       1000, -0.5,1999.5);
  }

  static string errorName[30] = {  // FIXME - defined twice
    " ","adc0","wrong channel","wrong pix","wrong roc","pix=0",
    " double-pix","wrong dcol","rocReset","NTP","timeout",
    "ENE","NOR","autoreset","overflow",
    "Cal","pkam","masked","automasked","tbmReset",
    "noTrailer","SyncTrig","StackFull","clearEVT","SyncErr"
  };

  for(int i=1; i<30; ++i) { // loop over error types  
    string num = std::to_string(i);
    name="herror"+num+"lsP"; title="errors vs ls, type "+errorName[i];        
    herrorlsP[i] = fs->make<TProfile>(name.c_str(),title.c_str(),maxLS,0.,float(maxLS),0.,1000.);
    name="herror"+num+"ls"; title="errors vs ls, type "+errorName[i];        
    herrorls[i] = fs->make<TH1D>(name.c_str(),title.c_str(),maxLS,0.,float(maxLS));
    name="hfed2DError"+num; title="Errors per fed/chan/event, type "+errorName[i];        
    hfed2DError[i] = fs->make<TH2F>(name.c_str(),title.c_str(),n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5, n_of_Channels, 0.5,maxChan);
    name="hchanErrorPerLS"+num; title="errors per chan, type "+errorName[i];        
    if((i==16)||(i==18)||(i>=9&&i<=12))
      hchanErrorPerLS[i] = fs->make<TH2F>(name.c_str(),title.c_str(),100,0.,100., n_of_Channels, 0.5,maxChan);
    name="hpixelsInErrorChannel"+num; title="Pixel hits in channel, for error type: "+errorName[i];        
    hpixelsInErrorChannel[i]=fs->make<TH1D>(name.c_str(),title.c_str(),600,0.,600.);
  }

#ifdef PER_FED
  const int nLS=100; // 100, number of lumi sections
  const float minLS=1., mLS=100.;
  //const float minLS=1051., mLS=1250.;
  //const float minLS=1251., mLS=1450.;
  for(int i=0;i<94;++i) {
    string num = std::to_string(i);
    name="hfedChanLS"+num; title="Channel size vs LS for FED "+num;        
    hfedChanLS[i] = fs->make<TProfile2D>(name.c_str(),title.c_str(),
					 nLS,minLS,mLS,
					 n_of_Channels,0.5,maxChan,0.0,10000.);
    name="hfedChanAutoMaskedLS"+num; title="Channel masked vs LS for FED "+num;        
    hfedChanAutoMaskedLS[i] = fs->make<TProfile2D>(name.c_str(),title.c_str(),
					 nLS,minLS,mLS,
				     	 n_of_Channels,0.5,maxChan,0.0,10000.);
  }
#endif

  string histoName[5] = {"hpix0Map","hdoubleMap","hdcolLowMap","hpixOrderMap","hadc0Map"};
  string titleName[5] = {"pix0 hits in L","double hits in L","dcol low hits in L","wrong pix order in L",
			 "adc0 hits in L"};
  int sizeH[4] = {13,29,45,65};
  float binH[4]={6.5,14.5,22.5,32.5};
  //string name, title;
  for(int i=0; i<4; ++i) { // loop over bpix layers 
    string num = std::to_string(i+1);
    name="hadc0RocMap"+num; title="ADC=0, ROC Map for L"+num;
    hadc0RocMap[i] = fs->make<TH2F>(name.c_str(),title.c_str(),52,0.,52.,80,0.,80.);
    for(int j=0; j<5; ++j) { // loop over error type 
      name=histoName[j]+num; title=titleName[j]+num;        
      if(j==0)      hpix0Map[i] = fs->make<TH2F>(name.c_str(),title.c_str(),9,-4.5,4.5,sizeH[i],-binH[i],binH[i]);
      else if(j==1) hdoubleMap[i] = fs->make<TH2F>(name.c_str(),title.c_str(),9,-4.5,4.5,sizeH[i],-binH[i],binH[i]);
      else if(j==2) hdcolLowMap[i] =fs->make<TH2F>(name.c_str(),title.c_str(),9,-4.5,4.5,sizeH[i],-binH[i],binH[i]);
      else if(j==3) hpixOrderMap[i]=fs->make<TH2F>(name.c_str(),title.c_str(),9,-4.5,4.5,sizeH[i],-binH[i],binH[i]);
      else if(j==4) hadc0Map[i]    =fs->make<TH2F>(name.c_str(),title.c_str(),9,-4.5,4.5,sizeH[i],-binH[i],binH[i]);
    }
  }


  //hpix1bx  = fs->make<TProfile>("hpix1bx", "l1 pix vs bx ",4000,-0.5,3999.5,0.0,1000000.);
  //hpix2bx  = fs->make<TProfile>("hpix2bx", "l2 pix vs bx ",4000,-0.5,3999.5,0.0,1000000.);
  //hpix3bx  = fs->make<TProfile>("hpix3bx", "l3 pix vs bx ",4000,-0.5,3999.5,0.0,1000000.);
  //hpix4bx  = fs->make<TProfile>("hpix4bx", "l4 pix vs bx ",4000,-0.5,3999.5,0.0,1000000.);
  //hpixfbx  = fs->make<TProfile>("hpixfbx", "fpix vs bx ",4000,-0.5,3999.5,0.0,1000000.);


#ifdef IND_FEDS
  hfed2DErrors1ls  = fs->make<TH2F>("hfed2DErrors1ls", "errors type 6 vs lumi",maxLS,0,float(maxLS), n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5); //
  //hfed2DErrors2ls  = fs->make<TH2F>("hfed2DErrors2ls", "errors type 6 vs lumi",maxLS,0,float(maxLS), n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5); //
  hfed2DErrors3ls  = fs->make<TH2F>("hfed2DErrors3ls", "errors type 6 vs lumi",maxLS,0,float(maxLS), n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5); //
  hfed2DErrors4ls  = fs->make<TH2F>("hfed2DErrors4ls", "errors type 6 vs lumi",maxLS,0,float(maxLS), n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5); //
  hfed2DErrors5ls  = fs->make<TH2F>("hfed2DErrors5ls", "errors type 6 vs lumi",maxLS,0,float(maxLS), n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5); //
  hfed2DErrors6ls  = fs->make<TH2F>("hfed2DErrors6ls", "errors type 6 vs lumi",maxLS,0,float(maxLS), n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5); //
  //hfed2DErrors7ls  = fs->make<TH2F>("hfed2DErrors7ls", "errors type 6 vs lumi",maxLS,0,float(maxLS), n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5); //
  //hfed2DErrors8ls  = fs->make<TH2F>("hfed2DErrors8ls", "errors type 6 vs lumi",maxLS,0,float(maxLS), n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5); //
  //hfed2DErrors9ls  = fs->make<TH2F>("hfed2DErrors9ls", "errors type 6 vs lumi",maxLS,0,float(maxLS), n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5); //
  hfed2DErrors10ls = fs->make<TH2F>("hfed2DErrors10ls","errors type 6 vs lumi",maxLS,0,float(maxLS), n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5); //
  hfed2DErrors11ls = fs->make<TH2F>("hfed2DErrors11ls","errors type 6 vs lumi",maxLS,0,float(maxLS), n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5); //
  hfed2DErrors12ls = fs->make<TH2F>("hfed2DErrors12ls","errors type 6 vs lumi",maxLS,0,float(maxLS), n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5); //
  hfed2DErrors13ls = fs->make<TH2F>("hfed2DErrors13ls","errors type 6 vs lumi",maxLS,0,float(maxLS), n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5); //
  hfed2DErrors14ls = fs->make<TH2F>("hfed2DErrors14ls","errors type 6 vs lumi",maxLS,0,float(maxLS), n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5); //
  hfed2DErrors15ls = fs->make<TH2F>("hfed2DErrors15ls","errors type 6 vs lumi",maxLS,0,float(maxLS), n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5); //
  hfed2DErrors16ls = fs->make<TH2F>("hfed2DErrors16ls","errors type 6 vs lumi",maxLS,0,float(maxLS), n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5); //
#endif


#ifdef USE_TREE
  if(makeTree>0) {
    tree = fs->make<TTree>("RawTree","RawTree");
    tree->Branch("event",&eventT,"event/I");
    tree->Branch("ls",&lsT,"ls/I");
    tree->Branch("bx",&bxT,"bx/I");
    tree->Branch("fed",&fedT,"fed/I");
    tree->Branch("channel",&channelT,"channel/I");
    tree->Branch("roc",&rocT,"roc/I");
    tree->Branch("module",&moduleT,"module/I");
    tree->Branch("ladder",&ladderT,"ladder/I");
    tree->Branch("layer",&layerT,"layer/I");
    tree->Branch("col",&colT,"col/I");
    tree->Branch("row",&rowT,"row/I");
    tree->Branch("adc",&adcT,"adc/I");
    tree->Branch("error",&errorT,"error/I");
  }
#endif 

#ifdef OUTFILE
  outfile.open("pixfed.csv");
  for(int i = 0; i < n_of_FEDs; ++i) {if(i<39) outfile<<i<<","; else outfile<<i<<endl;}
#endif

  countPixelsBPix=0;
  countPixelsBPix1=0, countPixelsBPix2=0,countPixelsBPix3=0,countPixelsBPix4=0;
  countPixelsFPix=0;

}
//-----------------------------------------------------------------------
void SiPixelRawDump::analyzeHits(int fedId, int fedChannel) {

  hchannelFED->Fill(float(fedId-fedId0),float(fedChannel-1));

  static int fed0=-1, chan0=-1, roc0=-1, layer0=-1;
  static int hitsPerRoc=0, hitsPerChannel=0;

  int adc = decode.get_adc();
  int roc = decode.get_roc();
  int layer = layer_;
  if(layer==0) { // for fpix
    if(ring_==1) layer=5;
    else if(ring_==2) layer=6;
    else cout<<"unknown ring "<<ring_<<endl;
  }

  //just for testing, delete later
  //int layer1 = decode.getLayer(fedId,fedChannel);
  //cout<<"getLayer in analyzeHits "<<layer_<<" "<<layer<<" "<<layer1<<endl;
  //if(layer!=layer1) cout<<"Wrong layer number "<<layer<<" "<<layer1<<endl;

  //cout<<fedId<<" "<<fedChannel<<" "<<roc<<" "<<layer<<endl;
  // testing only 
  if(0) {
  if(layer==1 && roc>2) cout<<"wrong roc number "<<roc<<" "<<layer<<endl;
  else if(layer==2 && roc>4) cout<<"wrong roc number "<<roc<<" "<<layer<<endl;
  else if(layer==3 && roc>8) cout<<"wrong roc number "<<roc<<" "<<layer<<endl;
  else if(layer==4 && roc>8) cout<<"wrong roc number "<<roc<<" "<<layer<<endl;
  else if(layer==5 && roc>8) cout<<"wrong roc number "<<roc<<" "<<layer<<endl;
  }

  // update channel count 
  //pixelsPerChannel[fedChannel-1]++;

  if( (fedId!=fed0) || (fedChannel!=chan0) || (roc!=roc0) ) { // new roc
    //cout<<"new roc "<<fedId<<" "<<fedChannel<<" "<<roc<<" "<<layer<<" "<<hitsPerRoc<<endl;
    if(roc0>=0) { // no first 

      // testing only 
      if(0) {
      if(layer0==1 && roc0>2) cout<<"wrong roc num "<<roc0<<" "<<layer0<<endl;
      else if(layer0==2 && roc0>4) cout<<"wrong roc num "<<roc0<<" "<<layer0<<endl;
      else if(layer0==3 && roc0>8) cout<<"wrong roc num "<<roc0<<" "<<layer0<<endl;
      else if(layer0==4 && roc0>8) cout<<"wrong roc num "<<roc0<<" "<<layer0<<endl;
      else if(layer0==5 && roc0>8) cout<<"wrong roc num "<<roc0<<" "<<layer0<<endl;
      }

      if(layer0<1 || layer0>6) {cout<<"error in layer number "<<layer0<<endl;
      } else {
	hhitsPerRoc[layer0-1]->Fill(float(hitsPerRoc));
	hhitsPerRocOrder[layer0-1]->Fill(float(roc0-1),float(hitsPerRoc));
      } // layer?
      //cout<<"Hits in ROC fed"<<fed0<<" chan "<<chan0<<" roc "<<roc0<<" lay "<<layer0<<" hits "<<hitsPerRoc<<endl;
      if(hitsPerRoc>hitsCut) cout<<"WARNING: Many hits in one roc: fed "<<fed0
				 <<" chan "<<chan0<<" roc-order "<<roc0
				 <<" hits "<<hitsPerRoc<<" layer "<<layer0
				 <<" event "<<countAllEvents<<"/"<<eventCMSSW<<" LS "<<lumiBlock
				 <<endl;
    } // not 1st 
    hitsPerRoc=0;

    if(fedChannel!=chan0 ) {  
      if(chan0>-1) { // not 1st time 
	if(layer0<1 || layer0>6) {cout<<"error in layer numeber "<<layer0<<endl;
	} else {
	  hhitsPerChannel[layer0-1]->Fill(float(hitsPerChannel));
	} // layer?
	if(hitsPerChannel>hitsCut2) {
	  hmanyHits->Fill(float(fedId-fedId0),float(fedChannel-1));
	  cout<<"WARNING: Many hits per channel: fed "<<fed0
	      <<" chan "<<chan0<<" roc-order "<<roc0
	      <<" hits "<<hitsPerChannel<<" layer "<<layer0
	      <<" event "<<countAllEvents<<"/"<<eventCMSSW<<" LS "<<lumiBlock
	      <<endl;
	} // many hits
      } // not 1st 
      hitsPerChannel=0;
    } // new channel

    fed0=fedId; chan0=fedChannel; roc0=roc; layer0=layer;
  } // new 

  hitsPerChannel++;
  hitsPerRoc++;
  //cout<<fedId<<" "<<fedChannel<<" "<<roc<<" "<<layer<<" "<<hitsPerRoc<<endl;
  if(layer==1)      
    {countPixelsBPix++;countPixelsBPix1++;hadc1->Fill(float(adc));hadc1ls->Fill(float(lumiBlock),float(adc));
      hadc1bx->Fill(float(bx),float(adc));}
  else if(layer==2) 
    {countPixelsBPix++;countPixelsBPix2++;hadc2->Fill(float(adc));hadc2ls->Fill(float(lumiBlock),float(adc));
      hadc2bx->Fill(float(bx),float(adc));}
  else if(layer==3) 
    {countPixelsBPix++;countPixelsBPix3++;hadc3->Fill(float(adc));hadc3ls->Fill(float(lumiBlock),float(adc));
      hadc3bx->Fill(float(bx),float(adc));}
  else if(layer==4) 
    {countPixelsBPix++;countPixelsBPix4++;hadc4->Fill(float(adc));hadc4ls->Fill(float(lumiBlock),float(adc));
      hadc4bx->Fill(float(bx),float(adc));}
  else if(layer==5 || layer==6)  // fpix 
    {countPixelsFPix++;hadc0->Fill(float(adc));hadc0ls->Fill(float(lumiBlock),float(adc));hadc0bx->Fill(float(bx),float(adc));}
  else {cout<<" invalid layer "<<layer<<endl;}

#ifdef USE_TREE
  if( (makeTree==6) || (makeTree>0 && makeTree==layer) ) {
    fedT=fedId;
    channelT=fedChannel;
    adcT=adc;
    layerT=layer;
    rocT = decode.get_roc();
    colT = decode.get_col();
    rowT = decode.get_row();
    string modName =   decode.getModName(fedId,fedChannel);
    ladderT = MyConvert::ladderFromName(modName);
    moduleT = MyConvert::moduleFromName(modName);
    if( (fedId!=errorFed) || (fedChannel!=errorChan) ) errorT=0; // otherwise keep it
    tree->Fill();

  }
#endif
  
}

//----------------------------------------------------------------------------
void SiPixelRawDump::analyzeErrors(int fedId, int fedChannel, int status, int stat1, int stat2) {
  // 2 - wrong channel
  // 3 - wrong pix or dcol 
  // 4 - wrong roc
  // 5 - pix=0
  // 6 - double pixel
  // 7 - wrong dcol order
  // 8 - ROC reset
  // 9 - NTP
  // 10 - timeout 
  // 11 - ene
  // 12 - nor
  // 13 - autoreset 
  // 14 - overflow 
  // 15 - trailer (not covered by others)
  // 16 - pkam  
  // 17 - masked
  // 18 - automasked
  // 19 - tbm reset 
  // 20 - noTrailer
  // 21 - FIFO 
  // 22 - StackFull
  // 23 - clearEVT
  // 24 - SyncErr/Trig 
  
#ifdef USE_TREE
  if(makeTree>0) {
    errorT=status;
    errorFed = fedId;
    errorChan = fedChannel;
  }
#endif

  if(status<30) {
    errorType[status]++; // count errors in the whole run 
    countErrors[status]++; // count errors in  one event  
    hfed2DError[status]->Fill(float(fedId-fedId0),float(fedChannel));
  }

  if(status!=17) hfed2dErrors->Fill(float(fedId-fedId0),float(status)); // fed # versus type, skip disabled 
  //else cout<<"disabled"<<endl;

  if(status>=8) {  // hard errors
    // Type - 1 Errors
    if(status!=17) { // skip disabled channels
      countErrorsInFed1++;
      fedErrors[fedId-fedId0][(fedChannel-1)]++; 
      if(status!=18) { // skip automasked channels 
	herrorType1->Fill(float(status));      
	herrorType1Fed->Fill(float(fedId-fedId0));
	hfedErrorType1ls->Fill(float(lumiBlock),float(fedId-fedId0)); 
	hchanErrorType1ls->Fill(float(lumiBlock),float(fedChannel)); 
	hfed2DErrorsType1->Fill(float(fedId-fedId0),float(fedChannel));
      }
    }

    if(status>=0 && status<30) {
      herrorls[status]->Fill(float(lumiBlock)); // 1D
      fedErrorsPerType[status][fedId-fedId0][(fedChannel-1)]++;
      errorInChannel[status][fedChannel-1]=true; 
   }

    switch(status) {

    case(8) : { // roc reset  
      break; }
      
    case(9) : { //  ntp
      hchanErrorPerLS[9]->Fill(float(lumiBlock),float(fedChannel));
      break; }
      
    case(10) : { // Timeout
      //htimeoutFed->Fill(float(fedId-fedId0));
      //htimeoutChan->Fill(float(fedChannel));
      //fedErrorsTime[fedId-fedId0][(fedChannel-1)]++;
      //herrorTimels->Fill(float(lumiBlock));
      hchanErrorPerLS[10]->Fill(float(lumiBlock),float(fedChannel));
      htest2->Fill(float(eventId%256));
      htest3->Fill(float(stat1));
      break; } 
      
    case(11) : {  // ENE
      //heneFed->Fill(float(fedId-fedId0));
      //fedErrorsENE[fedId-fedId0][(fedChannel-1)]++;
      hchanErrorPerLS[11]->Fill(float(lumiBlock),float(fedChannel));
      htest1->Fill(float(stat1));
      htest4->Fill(float(stat1-(eventId%256)));
      //hbx3->Fill(float(bx));
      break; }
      
    case(12) : {  // NOR
      hchanErrorPerLS[12]->Fill(float(lumiBlock),float(fedChannel));
      //hnorFed->Fill(float(fedId-fedId0));
      //fedErrorsOver[fedId-fedId0][(fedChannel-1)]++;   // use oveflow to count NORs for phase1 
      //hbx4->Fill(float(bx));
      break; }
      
    case(13) : {  // Autoreset
      //fedErrorsAutoReset[fedId-fedId0][(fedChannel-1)]++;
      break; }
      
    case(14) : {  // OVER
      break; }
      
    case(15) : {  // TBM Trailer
      break; }
      
    case(16) : { // pkam
      hchanErrorPerLS[16]->Fill(float(lumiBlock),float(fedChannel));
      //pkamInChannel[fedChannel-1]=true;
      //herrorPkamls->Fill(float(lumiBlock));
      //hpkamFed->Fill(float(fedId-fedId0));
      //fedErrorsPKAM[fedId-fedId0][(fedChannel-1)]++;
      break; }
      
    case(17) : { // masked 
      //fedErrorsMask[fedId-fedId0][(fedChannel-1)]++;
      //if( (countAllEvents>1) && (fedErrorsMask[fedId-fedId0][(fedChannel-1)]==1) )
      //cout<<" new masked channel "<<countAllEvents<<" ls "<<lumiBlock<<" fed "<<fedId<<" ch "<<fedChannel<<endl;
      //if(saveLast) maskedChannels.push_back(make_pair(fedId,fedChannel));
      //if(saveFirst)maskedChannels0.push_back(make_pair(fedId,fedChannel));
      fedErrorsMaskedInEvent[fedId-fedId0][(fedChannel-1)]=true;
      break; }
      
    case(18) : { // automasked 
      hchanErrorPerLS[18]->Fill(float(lumiBlock),float(fedChannel));
      //hautomaskedFed->Fill(float(fedId-fedId0));
      //fedErrorsAutoMask[fedId-fedId0][(fedChannel-1)]++;
      fedErrorsAutoMaskInEvent[fedId-fedId0][(fedChannel-1)]=true;
      //hbx5->Fill(float(bx));
      int index = layer_-1; if(layer_==0) index=4; // make fpix layer=5
      maskedPerEvent_[index]++;
      break; }
      
    case(19) : { // tbm reset        
      break; }
    } // end switch 

  
  } else if(status>0) {  // decode errors
    // Type 2 errors
    countErrorsInFed2++;
    hfedErrorType2ls->Fill(float(lumiBlock),float(fedId-fedId0)); // decode errors
    hfed2DErrorsType2->Fill(float(fedId-fedId0),float(fedChannel));
    herrorType2->Fill(float(status));
    herrorType2Fed->Fill(float(fedId-fedId0));
    //herrorType2Chan->Fill(float(fedChannel));

    // need layer, ladder, module 
    string modName = decode.getModName(fedId,fedChannel);
    int layer = decode.getLayer(fedId,fedChannel);  // 0 for fpix 
    //cout<<"getLayer in AnalyzeErrors "<<layer<<endl;
    int ladder = MyConvert::ladderFromName(modName);
    int module = MyConvert::moduleFromName(modName);
    //cout<<fedId<<" "<<fedChannel<<" "<<layer<<" "<<ladder<<" "<<module<<endl;

    if(status<30) {
      herrorls[status]->Fill(float(lumiBlock)); // 1D
      fedErrorsPerType[status][fedId-fedId0][(fedChannel-1)]++;
    }

    switch(status) {
      
    case(1) : {  // adc=0
      if(layer>0) {
	int col = decode.get_col();
	int row = decode.get_row();
	hadc0Map[layer-1]->Fill(float(module),float(ladder));
	hadc0RocMap[layer-1]->Fill(float(col),float(row));
      }
      break; }
      
    case(3) : {  //  inv. pix
      //decodeErrorsRow[fedId-fedId0][(fedChannel-1)]++;
      if(layer>0) hpixOrderMap[layer-1]->Fill(float(module),float(ladder));
      break; }
      
    case(4) : {  // inv roc
      //decodeErrors[fedId-fedId0][(fedChannel-1)]++;
      break; }
      
    case(5) : {  // pix=0
      //decodeErrors000[fedId-fedId0][(fedChannel-1)]++;
      if(layer>0) hpix0Map[layer-1]->Fill(float(module),float(ladder));
      //cout<<"pix0- "<<fedId<<" "<<fedChannel<<" "<<layer<<" "<<ladder<<" "<<module<<endl;
      break; }
      
    case(6) : {  // double pix
      //decodeErrorsDouble[fedId-fedId0][(fedChannel-1)]++;
      if(layer>0) hdoubleMap[layer-1]->Fill(float(module),float(ladder));
      //cout<<"double- "<<fedId<<" "<<fedChannel<<" "<<layer<<" "<<ladder<<" "<<module<<endl;
      break; }
      
    case(7) : {  // lower dcol
      //decodeErrorsDcol[fedId-fedId0][(fedChannel-1)]++;
      if(layer>0) hdcolLowMap[layer-1]->Fill(float(module),float(ladder));
      //cout<<"dcol- "<<fedId<<" "<<fedChannel<<" "<<layer<<" "<<ladder<<" "<<module<<endl;
      break;}
      
    default : {  // unknown
      //decodeErrors[fedId-fedId0][(fedChannel-1)]++;
      break; }
      
    }  // end switch
  } // end if

}
//-----------------------------------------------------------------------
void SiPixelRawDump::analyzeFinal(int fedId) {
   int sizeEven=0; int layer1st=-1; bool channel1st=false;
   for(int i=0;i<n_of_Channels;++i) {  // loop over channels
     int fedIndex=fedId-fedId0;
     int chanSize = fedchannelsize[i];
     int chanIndex=i+1;
     // here layer_ is not valid anymore, we are out of the error loop, have to get it again
     //int layer1 = layerIndex[(fedIndex)][i]; // fedChannel=i+1
     int layer = decode.getLayer(fedId,chanIndex);
     //if(layer>1 && (layer!=layer1)) cout<<"something wrong "<<layer<<" "<<layer1<<" "<<fedId<<" "<<i<<endl;


     // look at hits in channels with errors
     for(int j=0; j<30; ++j) {
       if( errorInChannel[j][i] ) {
	 //if(pixelsPerChannel[i]!=chanSize) cout<<"error in count"<<endl;
	 if(j==16 && chanSize>400) {
	   cout<<"real pkam in fed/chan: "<<fedId<<"/"<<(i+1)
	       <<" pixels "<<chanSize<<endl;
	   forcePrint=true;
	 }
	 hpixelsInErrorChannel[j]->Fill(float(chanSize));
       }
     }

     if(chanSize>0) {
       hfedchannelsizeFull->Fill( float(fedIndex), float(chanIndex), float(chanSize) );
#ifdef PER_FED
       if(fedIndex<94) hfedChanLS[fedIndex]->Fill(float(lumiBlock),float(chanIndex),float(chanSize));
#endif
     }
     if(fedErrorsAutoMaskInEvent[fedIndex][i] ) { // auto-masked, skip
       hfedchannelsizeEff->Fill( float(fedIndex), float(chanIndex), 0. ); //eff  , this measres the masked fraction 
#ifdef PER_FED
       if(fedIndex<94) hfedChanAutoMaskedLS[fedIndex]->Fill(float(lumiBlock),float(chanIndex),1.);
#endif
     } else if(fedErrorsMaskedInEvent[fedIndex][i] ) { // permanently masked, skip
       hfedchannelsizeEff->Fill( float(fedIndex), float(chanIndex), 0. ); //eff  , this measres the masked fraction 
#ifdef PER_FED
       if(fedIndex<94) hfedChanAutoMaskedLS[fedIndex]->Fill(float(lumiBlock),float(chanIndex),2.);
#endif
       
     } else {  // not masked, OK, histogram
       
#ifdef PER_FED
       if(fedIndex<94) hfedChanAutoMaskedLS[fedIndex]->Fill(float(lumiBlock),float(chanIndex),0.);
#endif
       // do only for not-masked channels
       hfedchannelsize->Fill( float(fedIndex), float(chanIndex), float(chanSize) );
       hfedchannelsizeEff->Fill( float(fedIndex), float(chanIndex), 1. );
       
	if((fedIndex)<fedIdBpixMax) {
	  hfedchannelsizeb->Fill( float(chanSize) );
	  if(layer==4)      {
	    if(chanSize>0)hfedchannelsize4->Fill( float(fedIndex), float(chanIndex), float(chanSize) );
	    hfedchannelsizeb4->Fill( float(chanSize) );  // layer 4
	    if(chanSize> max4) {max4=chanSize;maxfed4=fedIndex; maxchan4=chanIndex;}
	  } else if(layer==3) {
	    if(chanSize>0)hfedchannelsize3->Fill( float(fedIndex), float(chanIndex), float(chanSize) );
	    hfedchannelsizeb3->Fill( float(chanSize) );  // layer 3
	    if(chanSize> max3) {max3=chanSize;maxfed3=fedIndex; maxchan3=chanIndex;}
	  } else if(layer==2) {
	    if(chanSize>0)hfedchannelsize2->Fill( float(fedIndex), float(chanIndex), float(chanSize) );
	    hfedchannelsizeb2->Fill( float(chanSize) );  // layer 2
	    if(chanSize> max2) {max2=chanSize;maxfed2=fedIndex; maxchan2=chanIndex;}
	  } else if(layer==1) {
	    if(chanSize>0)hfedchannelsize1->Fill( float(fedIndex), float(chanIndex), float(chanSize) );
	    hfedchannelsizeb1->Fill( float(chanSize) );  // layer 1
	    if(chanSize> max1) {max1=chanSize; maxfed1=fedIndex; maxchan1=chanIndex;}
	  } else if(layer==-1) { continue;  // empty channel
	  } else cout<<" Cannot be "<<layer<<" "<<fedId<<" "<<(chanIndex)<<endl;
	} else  { // fpix
	  hfedchannelsizef->Fill( float(chanSize) );  // fpix
	  if(chanSize> max0) max0=chanSize;
	}    
      } // if automasked 

      // get the higher channel count per fiber
      if(i%2==0) {  // 1st channel in a fiber 
	sizeEven=chanSize;
	layer1st = layer;
	channel1st=true;

      } else { // 2nd channel of the same fiber 

	if(layer != layer1st) {
	  cout<<"something wrong with fiber-channel "
	      <<layer<<" "<<layer1st<<" "<<fedIndex<<" "<<i<<endl;
	  continue; // skip
	}
	if(!channel1st) {
	  cout<<"something wrong, no first  fiber-channel "
	      <<layer<<" "<<layer1st<<" "<<fedIndex<<" "<<i<<endl;
	  continue; // skip
	}


	// Find the larger channel size within 1 fiber 
	channel1st=false;
	int sizeDiff = -1.0;
	int sizeSum = sizeEven + chanSize;
	if(layer==1) htest->Fill(float(sizeSum));
	if(sizeEven>0. && chanSize>0.) {
	  sizeDiff=abs(chanSize-sizeEven);
	}
	float f= float(i/2)+1.;
	if(sizeDiff>=0.) hfedfibersizediff->Fill( float(fedIndex), float(f), float(sizeDiff));
	sizeEven=max(sizeEven,chanSize);
	if(sizeEven>0) {
	  if(layer==4)      {
	    hfedfibersize4->Fill( float(fedIndex), float(f), float(sizeEven) );
	    hfedfibersizeb4->Fill( float(sizeEven) );  // layer 4
	    if(sizeDiff>=0.) hfedfiberdiffb4->Fill( float(sizeDiff) );  // layer 4
	  } else if(layer==3) {
	    hfedfibersize3->Fill( float(fedIndex), float(f), float(sizeEven) );
	    hfedfibersizeb3->Fill( float(sizeEven) );  // layer 3
	    if(sizeDiff>=0.) hfedfiberdiffb3->Fill( float(sizeDiff) );  // layer 3
	  } else if(layer==2) {
	    hfedfibersize2->Fill( float(fedIndex), float(f), float(sizeEven) );
	    hfedfibersizeb2->Fill( float(sizeEven) );  // layer 2
	    if(sizeDiff>=0.) hfedfiberdiffb2->Fill( float(sizeDiff) );  // layer 2
	  } else if(layer==1) {
	    hfedfibersize1->Fill( float(fedIndex), float(f), float(sizeEven) );
	    hfedfibersizeb1->Fill( float(sizeEven) );  // layer 1
	    if(sizeDiff>=0.) hfedfiberdiffb1->Fill( float(sizeDiff) );  // layer 1
	  } else  {  // fpix
	    hfedfibersizef->Fill( float(fedIndex), float(f), float(sizeEven) );
	    hfedfibersizefpix->Fill(float(sizeEven) );  // fpix
	  } // end layer
	} // size>0 

      } // per fiber

    }  // channel

}


//----------------------------------------------------------------------------
// This is called for each event
// Loops ober raw data in every pixel FED
void SiPixelRawDump::analyze(const  edm::Event& ev, const edm::EventSetup& es) {
  const bool printEventInfo = false;
  //const bool print = false;

#ifdef PHASE1
  std::pair<int,int> fedIds(1200,1338); // phase 1
#else // phase0
  std::pair<int,int> fedIds(FEDNumbering::MINSiPixelFEDID, FEDNumbering::MAXSiPixelFEDID); //0
#endif

  // Access event information
  run       = ev.id().run();
  eventCMSSW  = ev.id().event();  // CMSSW event # , unsigned long long 
  lumiBlock = ev.luminosityBlock();
  bx        = ev.bunchCrossing(); // CMSSW bx
  //int orbit     = ev.orbitNumber();
  //event = eventCMSSW;
  //static unsigned long long oldEvent=0; // ,LS=0;
  
  countAllEvents++;
  hlumi0->Fill(float(lumiBlock));
  hbx0->Fill(float(bx));
  //horbit->Fill(float(orbit));

  if(selectedEvent>0 && eventCMSSW!=selectedEvent) return; //skip 
 
#ifdef USE_TREE
  if(makeTree>0) {
    eventT=eventCMSSW;
    lsT=lumiBlock;
    bxT=bx;
  }
#endif

  if(printEventInfo  || printVerbosity>1) {
    // if(countAllEvents<100 || (countAllEvents&1000)==0 )
    //   cout<<" Run "<<run<<" LS "<<lumiBlock<<" event "<<event<<" bx "<<bx
    // 	  <<" all "<<countAllEvents<<endl;
    //if( lumiBlock != LS) {
    cout<<endl<<"RAW-Data: Run "<<run<<" LS "<<lumiBlock<<" event(cmssw) "
	<<eventCMSSW<<" bx "<<bx
	<<" event# "<<countAllEvents<<endl;
    //if((printVerbosity>3) && (eventCMSSW<oldEvent) ) 
    //cout<<"   Lower event number: Run "<<run<<" LS "<<lumiBlock<<" event "<<eventCMSSW<<" bx "<<bx
    //	  <<" all "<<countAllEvents<<" "<<oldEvent<<endl;
    //oldEvent=eventCMSSW;
  }

  if(printHeaders) 
    cout<<endl<<"Event = "<<countAllEvents<<" CMSSW Event number "<<eventCMSSW<<"/"<<hex<<eventCMSSW<<dec<<" Run "<<run
	<<" LS "<<lumiBlock<<" bx "<<bx<<endl;


  // Get lumi info (does not work for raw)
//  edm::LuminosityBlock const& iLumi = ev.getLuminosityBlock();
//   edm::Handle<LumiSummary> lumi;
//   iLumi.getByLabel("lumiProducer", lumi);
//   edm::Handle<edm::ConditionsInLumiBlock> cond;
//   float intlumi = 0, instlumi=0;
//   int beamint1=0, beamint2=0;
//   iLumi.getByLabel("conditionsInEdm", cond);
//   // This will only work when running on RECO until (if) they fix it in the FW
//   // When running on RAW and reconstructing, the LumiSummary will not appear
//   // in the event before reaching endLuminosityBlock(). Therefore, it is not
//   // possible to get this info in the event
//   if (lumi.isValid()) {
//     intlumi =(lumi->intgRecLumi())/1000.; // integrated lumi per LS in -pb
//     instlumi=(lumi->avgInsDelLumi())/1000.; //ave. inst lumi per LS in -pb
//     beamint1=(cond->totalIntensityBeam1)/1000;
//     beamint2=(cond->totalIntensityBeam2)/1000;
//   } else {
//     std::cout << "** ERROR: Event does not get lumi info\n";
//   }
//   cout<<instlumi<<" "<<intlumi<<" "<<lumiBlock<<endl;
//   hinstl->Fill(float(lumiBlock),float(instlumi));
//   hintgl->Fill(float(lumiBlock),float(intlumi));


  edm::Handle<FEDRawDataCollection> buffers;
  //static std::string label = theConfig.getUntrackedParameter<std::string>("InputLabel","source");
  //static std::string instance = theConfig.getUntrackedParameter<std::string>("InputInstance","");  
  //ev.getByLabel( label, instance, buffers);
  ev.getByToken(rawData , buffers);  // the new bytoken 

  typedef uint32_t Word32;
  typedef uint64_t Word64;
  int status=0;
  int countPixels=0;
  eventId = -1;
  int countErrorsPerEvent=0;
  int countErrorsPerEvent1=0;
  int countErrorsPerEvent2=0;
  double aveFedSize = 0.;
  float countBpixFeds=0;
  stat1=-1; stat2=-1;
  //int fedchannelsize[n_of_Channels];
  bool wrongBX=false;
  for(int i=0;i<30;++i) countErrors[i] = 0;
  countPixelsFPix=0; countPixelsBPix=0; countPixelsBPix1=0; countPixelsBPix2=0; countPixelsBPix3=0;countPixelsBPix4=0;
  for(int i=0;i<5;++i) {maskedPerEvent_[i]=0;} // per layer (with fpix)

  forcePrint=false;
  // clear auto-mask array for each event
  for(int i = 0; i < n_of_FEDs; ++i) {
    for(int j=0;j<n_of_Channels;++j) {
      fedErrorsAutoMaskInEvent[i][j]=false; fedErrorsMaskedInEvent[i][j]=false;
    }
  }

#ifdef DO_CHANNEL_ORDER
  int fedIdOld=-1;
#endif
  // Loop over FEDs
  for (int fedId = fedIds.first; fedId <= fedIds.second; fedId++) {

    if(bpixOnly && fedId>1293) continue;  // skip fpix feds if required
    if(selectedFED>-1 && fedId!=selectedFED) continue; // skip if not selected 

#ifdef DO_CHANNEL_ORDER
    if (fedId!=fedIdOld) {
      if(fedId<fedIdOld) cout<<"ERROR: FED Id wrong order "<<fedId<<" "<<fedIdOld
			     <<" event "<<countAllEvents<<"/"<<eventCMSSW<<" LS "<<lumiBlock
			     <<endl;
      fedIdOld=fedId;
    }
#endif

    //edm::DetSetVector<PixelDigi> collection;
    //PixelDataFormatter::Errors errors;
    //get event data for this fed
    const FEDRawData& rawData = buffers->FEDData( fedId );

    if(printHeaders) cout<<"Get data For FED = "<<fedId<<" size in bytes "<<rawData.size()<<endl;
    if(rawData.size()==0) continue;  // skip if not data for this fed

    for(int i=0;i<n_of_Channels;++i){
      fedchannelsize[i]=0; //pixelsPerChannel[i]=0; 
      for(int j=0;j<30;++j) errorInChannel[j][i]=false;
    }

    int nWords = rawData.size()/sizeof(Word64);
    //cout<<" size "<<nWords<<endl;

    sumFedSize += float(nWords);    

    hsize->Fill(float(2*nWords)); // fed buffer size in words (32bit)
    hsize0->Fill(float(2*nWords)); // fed buffer size in words (32bit)
    if((fedId-fedId0)<fedIdBpixMax) {  // bpix
      hsize1->Fill(float(2*nWords)); // bpix fed buffer size in words (32bit)
      aveFedSize += double(2.*nWords);
      countBpixFeds++;
    } else hsize2->Fill(float(2*nWords)); // fpix fed buffer size in words (32bit)

#ifdef IND_FEDS
    hsizeFeds[fedId-fedId0]->Fill(float(2*nWords)); // size, includes errors and dummy words
#endif
    hsize2d->Fill(float(fedId-fedId0),float(2*nWords));  // 2d 
    hsizep->Fill(float(fedId-fedId0),float(2*nWords)); // profile 
    if((fedId-fedId0)<fedIdBpixMax) 
      hsizels->Fill(float(lumiBlock),float(2*nWords)); // bpix versu sls

    // check headers
    const Word64* header = reinterpret_cast<const Word64* >(rawData.data()); 
    //cout<<hex<<*header<<dec<<endl;

    unsigned int bxid = 0;
    eventId = decode.header(*header, fedId, printHeaders, bxid);  // return fed event number 
#ifdef CHECK_BX
    if(bx != int(bxid) ) { 
      wrongBX=true;
      if(printErrors && printBX) 
	cout<<" Inconsistent BX: for cmssw event "<<eventCMSSW<<" (fed-header event "<<eventId<<"/"<<hex<<eventId<<dec
	    <<") for LS "<<lumiBlock
	    <<" for run "<<run<<" for bx "<<bx<<" fed bx "<<bxid<<endl;
    }
    if(bx<0) bx=bxid; // if cmssw bx=-1 use the fed bx (for pilot)
#endif
    hbx1->Fill(float(bxid));


    const Word64* trailer = reinterpret_cast<const Word64* >(rawData.data())+(nWords-1);
    //cout<<hex<<*trailer<<dec<<endl;
    status = decode.trailer(*trailer,fedId, printHeaders);

    countErrorsInFed=0;countErrorsInFed1=0;countErrorsInFed2=0; 
    int countPixelsInFed=0;
    int fedChannel = 0;
    int num=0;
#ifdef USE_TREE
    errorFed=-1; errorChan=-1; // cleat the error-hit assocuation 
#endif
    int countPerChannel=0, fedChannelOld=-1;
    // Loop over payload words
    for (const Word64* word = header+1; word != trailer; word++) { // loop ober word8
      static const Word64 WORD32_mask  = 0xffffffff;

      for(int ipart=0;ipart<2;++ipart) {  // loop over two word4 
	Word32 w = 0;
	if(ipart==0) {
	  w =  *word       & WORD32_mask;  // 1st word
	  //w1=w;
	} else if(ipart==1) {
	  w =  *word >> 32 & WORD32_mask;  // 2nd word
	}

	num++;
	if(printVerbosity>3) cout<<" "<<num<<" "<<hex<<w<<dec<<endl;
	status = decode.data(w,fedChannel, fedId, stat1, stat2, printData);
	if(selectedChannel>-1 && fedChannel!=selectedChannel) continue;

	layer_ = decode.getLayer(fedId,fedChannel); // get layer number, 0 for fpix  
	if(layer_==0) {ring_ = decode.getFpixRing(fedId,fedChannel);
	} else {ring_=0;}

	if(printDebug) {
	  if(status==-16) { // pkams
	    cout<<fedId<<" "<<fedChannel<<" "<<layer_
		<<" event "<<eventCMSSW<<"/"<<eventId<<endl;
	  }
	}

	//cout<<"getlayer in Analyze "<<layer_<<" "<<status<<endl;
	if(fedChannel!=fedChannelOld) {
	  if(countPerChannel>0  && fedChannelOld>-1) 
	    hchannelFEDWords->Fill((fedId-fedId0),fedChannelOld,float(countPerChannel));

#ifdef DO_CHANNEL_ORDER
	  if(fedChannel<fedChannelOld) 
	    cout<<"ERROR: Channel out of order "<<fedChannel<<" "<<fedChannelOld
		<<" for fed "<<fedId
		<<" event "<<countAllEvents<<"/"<<eventCMSSW<<" LS "<<lumiBlock
		<<endl;
#endif
	  countPerChannel=0;
	  fedChannelOld=fedChannel;
	}
	countPerChannel++;

	htest5->Fill(float((eventId%256)-(eventCMSSW%256)));
	if(status>0) {  // ok, it is data
	  countPixels++;
	  countPixelsInFed++;
	  fedchannelsize[fedChannel-1]++;
	  analyzeHits(fedId, fedChannel);

	} else if(status<0) {  // error word
	  status=abs(status);
	  //if(status==17  && 1) {  //permanent masked channel 
	  //cout<<"IS status ever 17? "<<fedId<<" "<<fedChannel<<endl;
	  //}
	  if(status!=17 || !SKIP_PERMANENT_MASK) {  // skip disabled channels
	    countErrorsInFed++;
	    if(printErrors) {
	      cout<<"    Bad status for FED: "<<fedId
		  <<" local event "<<countAllEvents
		  <<" FED Event# "<<eventId<<"/(mod256)"<<(eventId%256)
		  <<" CMSSW Event# "<<eventCMSSW<<"/(mod256)"<<(eventCMSSW%256)
		  <<" chan "<<fedChannel<<" status "<<status<<endl;
	    } // if print 
	  } 
	  vector<int>* statuses = decode.getStatuses();
	  //cout<<"Statuses "<<statuses->size()<<endl;
	  for(vector<int>::iterator i=statuses->begin();i!=statuses->end();++i) {
	    int stat = *i; 
	    //if(stat==17  && 1) {  //permanent masked channel 
	    //cout<<"status 17? "<<fedId<<" "<<fedChannel<<" "<<lumiBlock<<endl;
	    //}
	    analyzeErrors(fedId, fedChannel, stat, stat1, stat2);
	  } // for loop 

	} // error/data
      } // for  1/2 word
    } // loop over longlong  words

    countTotErrors += countErrorsInFed;
    countErrorsPerEvent += countErrorsInFed;
    countErrorsPerEvent1 += countErrorsInFed1;
    countErrorsPerEvent2 += countErrorsInFed2;

    //convert data to digi (dummy for the moment)
    //formatter.interpretRawData( dummyErrorBool, fedId, rawData, collection, errors);
    //cout<<dummyErrorBool<<" "<<digis.size()<<" "<<errors.size()<<endl;

    if(countPixelsInFed>0)  {
      sumFedPixels[fedId-fedId0] += countPixelsInFed;
    }

    hpixels->Fill(float(countPixelsInFed));
    hpixels0->Fill(float(countPixelsInFed));
    if(countPixelsInFed>0) {
      hpixels1->Fill(float(countPixelsInFed));
      if( (fedId-fedId0) <fedIdBpixMax) hpixels2->Fill(float(countPixelsInFed));
      else                              hpixels3->Fill(float(countPixelsInFed));
    }
    herrors->Fill(float(countErrorsInFed));

    // final analysis 
    analyzeFinal(fedId);

    if(0) {
    int sizeEven=0; int layer1st=-1; bool channel1st=false;
    for(int i=0;i<n_of_Channels;++i) {  // loop over channels

      int fedIndex=fedId-fedId0;
      int chanSize = fedchannelsize[i];
      int chanIndex=i+1;
      // here layer_ is not valid anymore, we are out of the error loop, have to get it again
      //int layer1 = layerIndex[(fedIndex)][i]; // fedChannel=i+1
      int layer = decode.getLayer(fedId,chanIndex);
      //if(layer>1 && (layer!=layer1)) cout<<"something wrong "<<layer<<" "<<layer1<<" "<<fedId<<" "<<i<<endl;

      if(chanSize>0) {
	hfedchannelsizeFull->Fill( float(fedIndex), float(chanIndex), float(chanSize) );
#ifdef PER_FED
	if(fedIndex<94) hfedChanLS[fedIndex]->Fill(float(lumiBlock),float(chanIndex),float(chanSize));
#endif
      }
      if(fedErrorsAutoMaskInEvent[fedIndex][i] ) { // auto-masked, skip
	hfedchannelsizeEff->Fill( float(fedIndex), float(chanIndex), 0. ); //eff  , this measres the masked fraction 
#ifdef PER_FED
	if(fedIndex<94) hfedChanAutoMaskedLS[fedIndex]->Fill(float(lumiBlock),float(chanIndex),1.);
#endif
      } else if(fedErrorsMaskedInEvent[fedIndex][i] ) { // permanently masked, skip
	hfedchannelsizeEff->Fill( float(fedIndex), float(chanIndex), 0. ); //eff  , this measres the masked fraction 
#ifdef PER_FED
	if(fedIndex<94) hfedChanAutoMaskedLS[fedIndex]->Fill(float(lumiBlock),float(chanIndex),2.);
#endif
	
      } else {  // not masked, OK, histogram

#ifdef PER_FED
	if(fedIndex<94) hfedChanAutoMaskedLS[fedIndex]->Fill(float(lumiBlock),float(chanIndex),0.);
#endif
	// do only for not-masked channels
	hfedchannelsize->Fill( float(fedIndex), float(chanIndex), float(chanSize) );
	hfedchannelsizeEff->Fill( float(fedIndex), float(chanIndex), 1. );
	
	if((fedIndex)<fedIdBpixMax) {
	  hfedchannelsizeb->Fill( float(chanSize) );
	  if(layer==4)      {
	    if(chanSize>0)hfedchannelsize4->Fill( float(fedIndex), float(chanIndex), float(chanSize) );
	    hfedchannelsizeb4->Fill( float(chanSize) );  // layer 4
	    if(chanSize> max4) {max4=chanSize;maxfed4=fedIndex; maxchan4=chanIndex;}
	  } else if(layer==3) {
	    if(chanSize>0)hfedchannelsize3->Fill( float(fedIndex), float(chanIndex), float(chanSize) );
	    hfedchannelsizeb3->Fill( float(chanSize) );  // layer 3
	    if(chanSize> max3) {max3=chanSize;maxfed3=fedIndex; maxchan3=chanIndex;}
	  } else if(layer==2) {
	    if(chanSize>0)hfedchannelsize2->Fill( float(fedIndex), float(chanIndex), float(chanSize) );
	    hfedchannelsizeb2->Fill( float(chanSize) );  // layer 2
	    if(chanSize> max2) {max2=chanSize;maxfed2=fedIndex; maxchan2=chanIndex;}
	  } else if(layer==1) {
	    if(chanSize>0)hfedchannelsize1->Fill( float(fedIndex), float(chanIndex), float(chanSize) );
	    hfedchannelsizeb1->Fill( float(chanSize) );  // layer 1
	    if(chanSize> max1) {max1=chanSize; maxfed1=fedIndex; maxchan1=chanIndex;}
	  } else if(layer==-1) { continue;  // empty channel
	  } else cout<<" Cannot be "<<layer<<" "<<fedId<<" "<<(chanIndex)<<endl;
	} else  { // fpix
	  hfedchannelsizef->Fill( float(chanSize) );  // fpix
	  if(chanSize> max0) max0=chanSize;
	}    
      } // if automasked 

      // get the higher channel count per fiber
      if(i%2==0) {  // 1st channel in a fiber 
	sizeEven=chanSize;
	layer1st = layer;
	channel1st=true;

      } else { // 2nd channel of the same fiber 

	if(layer != layer1st) {
	  cout<<"something wrong with fiber-channel "
	      <<layer<<" "<<layer1st<<" "<<fedIndex<<" "<<i<<endl;
	  continue; // skip
	}
	if(!channel1st) {
	  cout<<"something wrong, no first  fiber-channel "
	      <<layer<<" "<<layer1st<<" "<<fedIndex<<" "<<i<<endl;
	  continue; // skip
	}


	// Find the larger channel size within 1 fiber 
	channel1st=false;
	int sizeDiff = -1.0;
	int sizeSum = sizeEven + chanSize;
	if(layer==1) htest->Fill(float(sizeSum));
	if(sizeEven>0. && chanSize>0.) {
	  sizeDiff=abs(chanSize-sizeEven);
	}
	float f= float(i/2)+1.;
	if(sizeDiff>=0.) hfedfibersizediff->Fill( float(fedIndex), float(f), float(sizeDiff));
	sizeEven=max(sizeEven,chanSize);
	if(sizeEven>0) {
	  if(layer==4)      {
	    hfedfibersize4->Fill( float(fedIndex), float(f), float(sizeEven) );
	    hfedfibersizeb4->Fill( float(sizeEven) );  // layer 4
	    if(sizeDiff>=0.) hfedfiberdiffb4->Fill( float(sizeDiff) );  // layer 4
	  } else if(layer==3) {
	    hfedfibersize3->Fill( float(fedIndex), float(f), float(sizeEven) );
	    hfedfibersizeb3->Fill( float(sizeEven) );  // layer 3
	    if(sizeDiff>=0.) hfedfiberdiffb3->Fill( float(sizeDiff) );  // layer 3
	  } else if(layer==2) {
	    hfedfibersize2->Fill( float(fedIndex), float(f), float(sizeEven) );
	    hfedfibersizeb2->Fill( float(sizeEven) );  // layer 2
	    if(sizeDiff>=0.) hfedfiberdiffb2->Fill( float(sizeDiff) );  // layer 2
	  } else if(layer==1) {
	    hfedfibersize1->Fill( float(fedIndex), float(f), float(sizeEven) );
	    hfedfibersizeb1->Fill( float(sizeEven) );  // layer 1
	    if(sizeDiff>=0.) hfedfiberdiffb1->Fill( float(sizeDiff) );  // layer 1
	  } else  {  // fpix
	    hfedfibersizef->Fill( float(fedIndex), float(f), float(sizeEven) );
	    hfedfibersizefpix->Fill(float(sizeEven) );  // fpix
	  } // end layer
	} // size>0 

      } // per fiber

    }  // channel
    } // if(0) 
#ifdef OUTFILE
    // print number of bytes per fed, CSV
    if(fedId == fedIds.second) outfile<<(nWords*8)<<endl;
    else                       outfile<<(nWords*8)<<",";  
#endif

  } // loop over feds

  htotPixels->Fill(float(countPixels));
  htotPixels0->Fill(float(countPixels));
  htotPixels3->Fill(float(countPixelsBPix));
  htotPixels4->Fill(float(countPixelsFPix));
  htotPixels5->Fill(float(countPixelsBPix1));
  htotPixels6->Fill(float(countPixelsBPix2));
  htotPixels7->Fill(float(countPixelsBPix3));
  htotPixels8->Fill(float(countPixelsBPix4));

  hmaskedL1ls->Fill(float(lumiBlock),float(maskedPerEvent_[0]));
  hmaskedL2ls->Fill(float(lumiBlock),float(maskedPerEvent_[1]));
  hmaskedL3ls->Fill(float(lumiBlock),float(maskedPerEvent_[2]));
  hmaskedL4ls->Fill(float(lumiBlock),float(maskedPerEvent_[3]));
  hmaskedFls->Fill(float(lumiBlock),float(maskedPerEvent_[4]));

  //hpix1bx->Fill(float(bx),float(countPixelsBPix1));
  //hpix2bx->Fill(float(bx),float(countPixelsBPix2));
  //hpix3bx->Fill(float(bx),float(countPixelsBPix3));
  //hpix4bx->Fill(float(bx),float(countPixelsBPix4));
  //hpixfbx->Fill(float(bx),float(countPixelsFPix));

#ifdef CHECK_BX
  if(wrongBX && printBX && !phase1) {
    cout<<" Inconsistent BX: for event "<<eventCMSSW<<" (fed-header event# "<<eventId<<") for LS "<<lumiBlock
	<<" for run "<<run<<" for bx "<<bx<<" pix= "<<countPixels<<endl;
    htotPixels2->Fill(float(countPixels));
    hbx7->Fill(float(bx));
  }
#endif
  htotErrors->Fill(float(countErrorsPerEvent));

  htotPixelsls->Fill(float(lumiBlock),float(countPixels));
  hbpixPixelsls->Fill(float(lumiBlock),float(countPixelsBPix));
  hbpixPixels1ls->Fill(float(lumiBlock),float(countPixelsBPix1));
  hbpixPixels2ls->Fill(float(lumiBlock),float(countPixelsBPix2));
  hbpixPixels3ls->Fill(float(lumiBlock),float(countPixelsBPix3));
  hbpixPixels4ls->Fill(float(lumiBlock),float(countPixelsBPix4));
  hfpixPixelsls->Fill(float(lumiBlock),float(countPixelsFPix));
  htotPixelsbx->Fill(float(bx),float(countPixels));
  hbpixPixelsbx->Fill(float(bx),float(countPixelsBPix));
  hbpixPixels1bx->Fill(float(bx),float(countPixelsBPix1));
  hbpixPixels2bx->Fill(float(bx),float(countPixelsBPix2));
  hbpixPixels3bx->Fill(float(bx),float(countPixelsBPix3));
  hbpixPixels4bx->Fill(float(bx),float(countPixelsBPix4));
  hfpixPixelsbx->Fill(float(bx),float(countPixelsFPix));

  herrorType1ls->Fill(float(lumiBlock),float(countErrorsPerEvent1));
  herrorType2ls->Fill(float(lumiBlock),float(countErrorsPerEvent2));

  for(int i=1; i<30; ++i) {
    herrorlsP[i]->Fill(float(lumiBlock),float(countErrors[i])); // profile 
  }

  herrorType1bx->Fill(float(bx),float(countErrorsPerEvent1));
  herrorType2bx->Fill(float(bx),float(countErrorsPerEvent2));

  aveFedSize /= countBpixFeds;  // bpix average size in words 
  hsize3->Fill(aveFedSize); // bpix 
  havsizebx->Fill(float(bx),aveFedSize); //bpix 

  if(forcePrint || (printErrors && countErrorsPerEvent>0)) {
    cout<<"EVENT cmssw/fed: "<<eventCMSSW<<"/"<<eventId<<" count events with hits= "<<countEvents
	<<", pixels in event = "<<countPixels<<" errors = "<<countErrorsPerEvent<<endl;
    forcePrint=false;
  }

  if(countPixels>0) {
    hlumi->Fill(float(lumiBlock));
    hbx->Fill(float(bx));
    htotPixels1->Fill(float(countPixels));
    countEvents++;
    sumPixels += countPixels;
    //int dummy=0;
    //cout<<" : ";
    //cin>>dummy;
  }  // end if

 
} // end analyze

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(SiPixelRawDump);
