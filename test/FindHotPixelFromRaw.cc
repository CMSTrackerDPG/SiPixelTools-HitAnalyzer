/** \class SiPixelRawDumper_H
 * To find hot pixels from raw data
 * Works in  v352
 * Modify for phase1.
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

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <iomanip>

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
#include <TProfile.h>
#include <TProfile2D.h>


namespace {
  const bool DEBUG=false;
  const bool printErrors  = false;
  const bool printData    = false;
  const bool printHeaders = false;
  int count0=0, count1=0, count2=0, count3=0, count4=0;
  const int FEDs=139;
  const int fedId0=1200;
  const bool findHot=true;
}

using namespace std;

// Include the helper decoding class
/////////////////////////////////////////////////////////////////////////////
class MyDecode {
public:
  MyDecode() {}
  ~MyDecode() {}
  static int error(int error, bool print=false);
  static int data(int error, int &channel, int &roc, int &dcol, int &pix, int &adc, bool print=false);
  static int header(unsigned long long word64, bool print);
  static int trailer(unsigned long long word64, bool print);
private:
};
/////////////////////////////////////////////////////////////////////////////
int MyDecode::header(unsigned long long word64, bool printFlag) {
  int fed_id=(word64>>8)&0xfff;
  int event_id=(word64>>32)&0xffffff;
  unsigned int bx_id=(word64>>20)&0xfff;
//   if(bx_id!=101) {
//     cout<<" Header "<<" for FED "
//   <<fed_id<<" event "<<event_id<<" bx "<<bx_id<<endl;
//     int dummy=0;
//     cout<<" : ";
//     cin>>dummy;
//   }
  if(printFlag) cout<<" Header "<<" for FED "
             <<fed_id<<" event "<<event_id<<" bx "<<bx_id<<endl;
  
  return event_id;
}
//
int MyDecode::trailer(unsigned long long word64, bool printFlag) {
  int slinkLength = int( (word64>>32) & 0xffffff );
  int crc         = int( (word64&0xffff0000)>>16 );
  int tts         = int( (word64&0xf0)>>4);
  int slinkError  = int( (word64&0xf00)>>8);
  if(printFlag) cout<<" Trailer "<<" len "<<slinkLength
             <<" tts "<<tts<<" error "<<slinkError<<" crc "<<hex<<crc<<dec<<endl;
  return slinkLength;
}
//
// Decode error FIFO
// Works for both, the error FIFO and the SLink error words. d.k. 25/04/07
int MyDecode::error(int word, bool printFlag) {
  int status = -1;
  const unsigned int  errorMask      = 0x3e00000;
  const unsigned int  dummyMask      = 0x03600000;
  const unsigned int  gapMask        = 0x03400000;
  const unsigned int  timeOut        = 0x3a00000;
  const unsigned int  eventNumError  = 0x3e00000;
  const unsigned int  trailError     = 0x3c00000;
  const unsigned int  fifoError      = 0x3800000;

//  const unsigned int  timeOutChannelMask = 0x1f;  // channel mask for timeouts
  //const unsigned int  eventNumMask = 0x1fe000; // event number mask
  const unsigned int  channelMask = 0xfc000000; // channel num mask
  const unsigned int  tbmEventMask = 0xff;    // tbm event num mask
  const unsigned int  overflowMask = 0x100;   // data overflow
  const unsigned int  tbmStatusMask = 0xff;   //TBM trailer info
  const unsigned int  BlkNumMask = 0x700;   //pointer to error fifo #
  const unsigned int  FsmErrMask = 0x600;   //pointer to FSM errors
  const unsigned int  RocErrMask = 0x800;   //pointer to #Roc errors
  const unsigned int  ChnFifMask = 0x1f;   //channel mask for fifo error
  const unsigned int  Fif2NFMask = 0x40;   //mask for fifo2 NF
  const unsigned int  TrigNFMask = 0x80;   //mask for trigger fifo NF

 const int offsets[8] = {0,4,9,13,18,22,27,31};

 //cout<<"error word "<<hex<<word<<dec<<endl;

  if( (word&errorMask) == dummyMask ) { // DUMMY WORD
    //cout<<" Dummy word";
    return 0;
  } else if( (word&errorMask) == gapMask ) { // GAP WORD
    //cout<<" Gap word";
    return 0;
  } else if( (word&errorMask)==timeOut ) { // TIMEOUT
     // More than 1 channel within a group can have a timeout error
     unsigned int index = (word & 0x1F);  // index within a group of 4/5
     unsigned int chip = (word& BlkNumMask)>>8;
     int offset = offsets[chip];
     if(printErrors) {
       cout<<"Timeout Error- channels: ";
       for(int i=0;i<5;i++) {
      if( (index & 0x1) != 0) {
        int chan = offset + i + 1;
        cout<<chan<<" ";
      }
      index = index >> 1;
       }
       cout<<endl;
     }
     //end of timeout  chip and channel decoding
     
  } else if( (word&errorMask) == eventNumError ) { // EVENT NUMBER ERROR
    unsigned int channel =  (word & channelMask) >>26;
    unsigned int tbm_event   =  (word & tbmEventMask);
    
    if(printErrors) cout<<"Event Number Error- channel: "<<channel<<" tbm event nr. "
                     <<tbm_event<<endl;
    
  } else if( ((word&errorMask) == trailError)) {
    unsigned int channel =  (word & channelMask) >>26;
    unsigned int tbm_status   =  (word & tbmStatusMask);
    if(word & RocErrMask)
      if(printErrors) cout<<"Number of Rocs Error- "<<"channel: "<<channel<<" "<<endl;
    if(word & FsmErrMask)
      if(printErrors) cout<<"Finite State Machine Error- "<<"channel: "<<channel
                       <<" Error status:0x"<<hex<< ((word & FsmErrMask)>>9)<<dec<<" "<<endl;
    if(word & overflowMask)
      if(printErrors) cout<<"Overflow Error- "<<"channel: "<<channel<<" "<<endl;
    //if(!((word & RocErrMask)|(word & FsmErrMask)|(word & overflowMask)))
    if(tbm_status!=0)
      if(printErrors) cout<<"Trailer Error- "<<"channel: "<<channel<<" TBM status:0x"
                       <<hex<<tbm_status<<dec<<" "<<endl;

  } else if((word&errorMask)==fifoError) {
    if(printErrors) { 
      if(word & Fif2NFMask) cout<<"A fifo 2 is Nearly full- ";
      if(word & TrigNFMask) cout<<"The trigger fifo is nearly Full - ";
      if(word & ChnFifMask) cout<<"fifo-1 is nearly full for channel"<<(word & ChnFifMask);
      cout<<endl;
    }
  } else {
    cout<<" Unknown error?";
  }

  //unsigned int event   =  (word & eventNumMask) >>13;
  //unsigned int tbm_status   =  (word & tbmStatusMask);
  //if(event>0) cout<<":event: "<<event;
  //cout<<endl;

  return status;
}
///////////////////////////////////////////////////////////////////////////
int MyDecode::data(int word, int &c, int &r, int &d, int &p, int &a, bool printFlag) {
  
  //const int ROCMAX = 24;
  const unsigned int plsmsk = 0xff;   // pulse height
  const unsigned int pxlmsk = 0xff00; // pixel index
  const unsigned int dclmsk = 0x1f0000;

  //#ifdef PHASE1
  //const unsigned int rocmsk  = 0x1e00000;  // 4 bits 
  //const unsigned int chnlmsk = 0xfe000000; // 7 bits 
  //const unsigned int rocshift = 21;
  //const unsigned int linkshift = 25;

  // for layer-1
  const unsigned int rowmsk = 0x7f00; 
  const unsigned int colmsk = 0x1f8000;

  //#endif
  // for both phase0 and phase1
  const unsigned int rocmsk  = 0x3e00000;   // 5 bits
  const unsigned int chnlmsk = 0xfc000000; // 6 bits 
  const unsigned int rocshift = 21;
  const unsigned int linkshift = 26;

  int status = 0;

  int roc = ((word&rocmsk)>>rocshift); // rocs start from 1
  // Check for embeded special words
  if(roc>0 && roc<25) {  // valid ROCs go from 1-24
    //if(print) cout<<"data "<<hex<<word<<dec;
    int channel = ((word&chnlmsk)>>linkshift);

    if(channel>0 && channel<=48) {  // valid channels 1-48
      //cout<<hex<<word<<dec;
      int dcol=(word&dclmsk)>>16;
      int pix=(word&pxlmsk)>>8;
      int adc=(word&plsmsk);
      //fedChannel = channel_;
      //int col = convertToCol(dcol,pix);
      //int row  = convertToRow(pix);

      // for L1 
      int col1=(word&colmsk)>>15;
      int row1=(word&rowmsk)>>8;
      
      // test the unfold, make sure that we can get the l1 col/row
      int tmp = (dcol<<16) + (pix<<8);
      int col11 = (tmp&colmsk)>>15;
      int row11 = (tmp&rowmsk)>>8;
      if(col1!=col11) cout<<" col not equal "<<col1<<" "<<col11<<endl;
      if(row1!=row11) cout<<" row not equal "<<row1<<" "<<row11<<endl;


      // will need here a loopup table which can distuinguish layer 1 links
      // to decide if we read dcol/pis or col/row
      if(printFlag) 
	cout<<" Channel- "<<channel<<" ROC- "<<(roc-1)
	    <<" DCOL- "<<dcol<<" Pixel- "<<pix
	    <<" (OR for L1 col-"<<col1<<" row-"<<row1
	    <<") ADC- "<<adc<<endl;
      
      c = channel;
      r = roc-1; // start roc counting from 0
      d = dcol;
      p = pix;
      a = adc;
      status++;	

    } else { // channel

      cout<<" Wrong channel "<<channel<<" : "
	  <<" Word "<<hex<<word<<dec<<endl;
      return -2;

    }

  } else if(roc==25) {  // ROC? 
    //unsigned int chan = ((word&chnlmsk)>>26);
    //cout<<"Wrong roc 25 "<<" in chan "<<"/"<<chan<<endl;
    //status=error(word);
    status=-4;

  } else {  // error word

    //cout<<"error word "<<hex<<word<<dec;
    status=error(word);

  }

  return status;
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Class to get names
class MyConvert {
public:
  MyConvert() {}
  ~MyConvert() {}
  static string rocModuleNameFromFedChan(int fed,int fedChan, int roc, string & tbm);
  static int layerFromName(string name);

private:
};

// layer number form module name 
int MyConvert::layerFromName(string modName) {
  int layer=0;

  if     ( modName.find("_LYR1_") != string::npos ) layer=1;  
  else if( modName.find("_LYR2_") != string::npos ) layer=2;  
  else if( modName.find("_LYR3_") != string::npos ) layer=3;  
  else if( modName.find("_LYR4_") != string::npos ) layer=4;  

  return layer;
}

// Method returns the module name and the tbm type as strings
// input: int fed, fedChan
// output: string name, tbm ("A" or "B")
string MyConvert::rocModuleNameFromFedChan(int fed0,int fedChan0, int roc0, string & tbm0) {
  if ( fed0<1200 || fed0>1338) return " ";
  //if ( fed0<32 && (fedChan0<1 || fedChan0>36) ) return " ";  // barrel channels not bigger than 36
  //if ( fed0>31 && (fedChan0<1 || fedChan0>24) ) return " ";  // endcap channels not bigger than 24

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
  //int fedOld=-1, fedChanOld=-1; // rocOld=-1;
  bool found = false;
  //int rocNumber;

  for(int i=0;i<100000;++i) {
    //bool print = false;

    // first get the name, then  decide whether it is barrel and endcap
    infile>>name;
    infile>>tbm>>fec>>mfec>>mfecChan>>hub>>port>>rocId>>fed>>fedChan>>rocOrder;
    
    if(name==" ")continue;

    // if (name[0]=='F') {
    //     // endcap doesn't have the TBM token to read
    //     infile>>fec>>mfec>>mfecChan>>hub>>port>>rocId>>fed>>fedChan>>rocOrder;
    // } else {
    //     infile>>tbm>>fec>>mfec>>mfecChan>>hub>>port>>rocId>>fed>>fedChan>>rocOrder;
    // }
    
    if ( infile.eof() != 0 ) {
      cout<< " end of file " << endl;
      break;;
    } else if (infile.fail()) { // check for errors
      cout << "Cannot read data file" << endl;
      return(" ");
    }

    if (fed0<1294) {
      //barrel module name requested, do not use the roc0 parameter
      // skip same fed/channel
      //if(fed==fedOld && fedChanOld==fedChan) continue;
      //fedOld = fed;
      //fedChanOld = fedChan;

      if(fed==fed0 && fedChan==fedChan0 && rocOrder==roc0) {  // found
	//if(fed==fed0 && fedChan==fedChan0) {  // found
	found = true;
	tbm0=tbm;
	// strip out the _ROC section from the name because it is not needed to identify the ROC number
	modName = name;
	// string::size_type idx;
	// idx = name.find("_ROC");
	// if(idx != string::npos) {
	//   modName = name.substr(0,idx);
	//   string rocName = name[idx+4];
	//   rocNumber = atoi(rocName);
	// }
	break;
      }

    } else {
        // endcap module name requested, use the roc0 parameter
        //if(fed==fedOld && fedChanOld==fedChan && rocOld==rocOrder) continue;

        if(fed==fed0 && fedChan==fedChan0 && rocOrder==roc0) {  // found
            found = true;
            tbm0=tbm;
            // do not strip anything from the endcap name because it is needed to identify the ROC number
            modName = name; 
            break;
        }
        //fedOld = fed;
        //fedChanOld = fedChan;
        //rocOld = rocOrder;
    }
  }  // end line loop
  
  infile.close();  
  if(!found) cout<<" Module not found "<<fed0<<" "<<fedChan0<<endl;

  return modName;

}

//////////////////////////////////////////////////////////////////////////////////////////////////////////

const int NumPixels = 100000;
const int NumROCs = 500;
class HotPixels {
public:
  HotPixels() {
    count=0; 
    for(int i=0;i<NumPixels;++i) {array[i]=0; data[i]=0;}
    for(int i=0;i<NumROCs;++i) {rocs[i]=0;} 
    for(int i=0;i<4;++i) {countInLayers[i]=0.;countPixInLayers[i]=0.;} 
    for(int i=0;i<4;++i) {countInLayersCut[i]=0.;countPixInLayersCut[i]=0.;} 
  }

  ~HotPixels() {
  }
  int update(int channel, int roc, int dcol, int pix); 
  int code(int channel, int roc, int dcol, int pix); 
  void decode(int index, int &channel, int &roc, int &dcol, int &pix); 
  //void print(int, int, double);
  void print(int, int, double, TH2F*);
  void printROCs(int, int);
  double printLayers(double &l1, double &l2, double &l3, double&l4);
  double printPixLayers(double &l1, double &l2, double &l3, double&l4);
  double printLayersCut(double &l1, double &l2, double &l3, double&l4);
  double printPixLayersCut(double &l1, double &l2, double &l3, double&l4);
  int get_counts(int i) {if(i<count) return data[i]; else return -1;}
  int get_countsROC(int i) {if(i<NumROCs) return rocs[i]; else return -1;}
  int codeROC(int channel, int roc); 
  void decodeROC(int index, int &channel, int &roc); 

private:
  int count;
  int array[NumPixels];
  int data[NumPixels];
  int rocs[NumROCs];
  double countInLayers[4];
  double countPixInLayers[4];
  double countInLayersCut[4];
  double countPixInLayersCut[4];
};
// return numbr of noisy pixels per layer 
double HotPixels::printPixLayersCut(double &l1,double &l2,double &l3,double &l4) {
  l1 = countPixInLayersCut[0];
  l2 = countPixInLayersCut[1];
  l3 = countPixInLayersCut[2];
  l4 = countPixInLayersCut[3];
  double l=l1+l2+l3+l4;
  //    for(int i=0;i<4;++i) {cout<<countInLayers[i]<<" ";} cout<<endl; 
  return l;
}
// return number of hits in noisy pixels 
double HotPixels::printLayersCut(double &l1,double &l2,double &l3,double &l4) {
  l1 = countInLayersCut[0];
  l2 = countInLayersCut[1];
  l3 = countInLayersCut[2];
  l4 = countInLayersCut[3];
  double l=l1+l2+l3+l4;
  //    for(int i=0;i<4;++i) {cout<<countInLayers[i]<<" ";} cout<<endl; 
  return l;
}
double HotPixels::printPixLayers(double &l1,double &l2,double &l3,double &l4) {
  l1 = countPixInLayers[0];
  l2 = countPixInLayers[1];
  l3 = countPixInLayers[2];
  l4 = countPixInLayers[3];
  double l=l1+l2+l3+l4;
  //    for(int i=0;i<4;++i) {cout<<countInLayers[i]<<" ";} cout<<endl; 
  return l;
}
// return number of hits in noisy pixels 
double HotPixels::printLayers(double &l1,double &l2,double &l3,double &l4) {
  l1 = countInLayers[0];
  l2 = countInLayers[1];
  l3 = countInLayers[2];
  l4 = countInLayers[3];
  double l=l1+l2+l3+l4;
  //    for(int i=0;i<4;++i) {cout<<countInLayers[i]<<" ";} cout<<endl; 
  return l;
}
int HotPixels::code(int channel, int roc, int dcol, int pix) {
  // pix 0 - 182, dcol 0 - 26 , roc 0-7, chan 1- 48
  int index = pix + 1000 * dcol + 100000 * roc + 10000000 * channel;
  return index;
}
void HotPixels::decode(int index, int &channel, int &roc, int &dcol, int &pix) {
  //int index = pix + 1000 * dcol + 100000 * roc + 10000000 * channel;
  channel =  index/10000000;
  roc     = (index%10000000)/100000;
  dcol    = (index%100000)/1000;
  pix     = (index%1000);
}
int HotPixels::codeROC(int channel, int roc) {
  // pix 0 - 182, dcol 0 - 26 , roc 0 -15, chan 1-36
  //int index = roc + 100 * channel;
  if(roc>9) cout<<" complain about roc "<<roc<<endl;
  int index = roc + 10 * channel;
  return index;
}
void HotPixels::decodeROC(int index, int &channel, int &roc) {
  //int index = pix + 1000 * dcol + 100000 * roc + 10000000 * channel;
  //channel = index/100;
  //roc     = (index%100);
  channel = index/10;
  roc     = (index%10);
}
int HotPixels::update(int channel, int roc, int dcol, int pix) {
  int ret = 0;
  int index = code(channel, roc, dcol, pix);
  //cout<<channel<<"   "<<roc<<"    "<<dcol<<"    "<<pix<<"    "<<index<<endl;
  bool found = false;
  for(int i=0;i<count;++i) {
    if(index == array[i]) {
      data[i]++;
      ret=data[i];
      found=true;
      break;
    }
  }
  if(!found) {
    if(count>=NumPixels) {
      cout<<" array too small "<<count<<" "<<endl;
    } else {
      data[count] =1;
      array[count]=index;
      count++;
      ret=1;
    }
  }
  return ret;
}
void HotPixels::print(int events, int fed_id, double fraction, TH2F* hfedchannelp) {
  // for layer-1
  const unsigned int rowmsk = 0x7f00; 
  const unsigned int colmsk = 0x1f8000;
  int channel=0, rocOrder=0, dcol=0, pix=0;
  int num =0;
  int cut1 = events/100;
  int cut2 = events/1000;
  int cut3 = events/10000;

  int cut = int(events * fraction);
  if(cut<2) cut=2;

  if(fed_id==1200) {
    cout<<" Threshold for "<<fraction<<" is "<<cut<<" cuts for 1% "<<cut1<<" 0.1% "<<cut2<<" 0.01% "<<cut3<<endl;
    cout<<"fed chan     module                   tbm roc dcol  pix  colR ";
    cout<<"rowR count  num roc-local"<<endl;
    //cout<<" fed chan name tbm rocp dcol pix colR rowR count num roc "<<endl;
  }

  for(int i=0;i<count;++i) { // loop over pixels with hits 

    if(data[i]<=0) {cout<<" no counts "<<data[i]<<endl; continue;}
    count4++;

    int index = array[i];
    if(index<=0) {cout<<" index wrong "<<index<<endl; continue;}

    decode(index, channel, rocOrder, dcol, pix);

    hfedchannelp->Fill(float(fed_id-1200),float(channel),float(data[i]));
    //if(fed_id==1253 && channel==44) cout<<rocOrder<<" "<<dcol<<" "<<pix<<" "<<data[i]<<endl;

    // Get the module name and tbm type 
    string modName = " ",tbm=" ";
    int rocNumber=-1;
    string  name = MyConvert::rocModuleNameFromFedChan(fed_id,channel,rocOrder,tbm);
    string::size_type idx;
    idx = name.find("_ROC");
    if(idx != string::npos) {
      modName = name.substr(0,idx);
      string rocName = name.substr(idx+4,name.length());
      rocNumber = atoi(rocName.c_str());
    }
    
    int realRocNum = -1;
    int colROC = -1, rowROC = -1; // layer0 = 0;
    int layer = MyConvert::layerFromName(name);
    //string::size_type id;
    //if     ( modName.find("_LYR1_") != string::npos ) layer0=1;  
    //else if( modName.find("_LYR2_") != string::npos ) layer0=2;  
    //else if( modName.find("_LYR3_") != string::npos ) layer0=3;  
    //else if( modName.find("_LYR4_") != string::npos ) layer0=4;  
    //if(layer!=layer0) cout<<" big nig error"<<endl;
    

    // all hits 
    if(layer>0 &&layer<5) {
	countInLayers[layer-1] += data[i];countPixInLayers[layer-1]++;
    }
    // hits above cut
    if(data[i]>cut) { // check the number of hits is above the threshold cut
      num++;
      count0++;

      // update later count 
      if(layer>0 &&layer<5) {
	countInLayersCut[layer-1] += data[i];
	countPixInLayersCut[layer-1]++;
      }

      // Below there is code to find the real ROC number, it is just for 
      // verification, the real ROC number is already known from the roc
      // order. Keep for testsing 
      
      if( layer==1 ) { // layer  1
	//cout<<" this is layer 1 "<<modName<<endl;
	// this is still wrong as it does not take the bit change into account WHAT DOES THIS MEAN?

	int tmp = (dcol<<16) + (pix<<8);
	colROC = (tmp&colmsk)>>15;
	rowROC = (tmp&rowmsk)>>8;

	// Find F or H L1 module flavour
	bool fModule = false;// this is an h-module 
	if( modName.find("F_MOD") != string::npos) fModule=true;


	if(fModule) { // F-module 

	  if     (tbm=="A1") realRocNum = rocOrder; // shift for TBM-N
	  else if(tbm=="A2") realRocNum = rocOrder + 2; // shift for TBM-N
	  else if(tbm=="B1") realRocNum = rocOrder + 12; // shift for TBM-N
	  else if(tbm=="B2") realRocNum = rocOrder + 14; // shift for TBM-N
	  else cout<<" unknown "<<tbm<<endl;

	} else { // H-module

	  if     (tbm=="A1") realRocNum = rocOrder + 4; // shift for TBM-N
	  else if(tbm=="A2") realRocNum = rocOrder + 6; // shift for TBM-N
	  else if(tbm=="B1") realRocNum = rocOrder + 8; // shift for TBM-N
	  else if(tbm=="B2") realRocNum = rocOrder + 10; // shift for TBM-N
	  else cout<<" unknown "<<tbm<<endl;

	}

      }  else {

	// First find if we are in the first or 2nd col of a dcol.
	int colEvenOdd = pix%2;  // module(2), 0-1st sol, 1-2nd col.
	// Transform
	colROC = dcol * 2 + colEvenOdd; // col address, starts from 0
	rowROC = abs( int(pix/2) - 80); // row addres, starts from 0
	//cout<<index<<" ";

	if(layer==2) {
	  if     (tbm=="A1") realRocNum = rocOrder; // shift for TBM-N
	  else if(tbm=="A2") realRocNum = rocOrder + 4; // shift for TBM-N
	  else if(tbm=="B1") realRocNum = rocOrder + 8; // shift for TBM-N
	  else if(tbm=="B2") realRocNum = rocOrder + 12; // shift for TBM-N
	  else cout<<" unknown "<<tbm<<endl;


	} else if (layer==3 || layer==4)  {
	  if(tbm=="A1") realRocNum = rocOrder; // shift for TBM-N
	  else if(tbm=="A2") realRocNum = rocOrder + 8; // shift for TBM-N
	  else cout<<" unknown "<<tbm<<endl;
	
	} else if (layer==0)  {
	  if(tbm=="A") realRocNum = rocOrder; // shift for TBM-N
	  else if(tbm=="B") realRocNum = rocOrder + 8; // shift for TBM-N
	  else cout<<" unknown "<<tbm<<endl;
	}

      }

      if(rocNumber != realRocNum) cout<<"ERROR - something wrong in roc number "
				     <<rocNumber<<" "<<realRocNum<<endl; 

      if (modName[0]=='F') {
          cout<<setw(3) <<fed_id   << " "   << setw(3) << channel    << " "  << setw(30) << modName << "  "
                        << tbm << " "   << setw(3) << rocNumber << "  " << setw(3)  << dcol    << "  " << setw(3)
                        << pix     << "   " << setw(3) << colROC     << "  " << setw(3)  << rowROC  << "  " << setw(4)
	      << data[i] << "  "  << setw(3) << num        << "  " << setw(3)  << rocOrder <<endl;
	  // << " "<<name<<" "<<realRocNum<<endl;

      } else {  // Bpix

	//string::size_type idx = modName.find("_ROC");
	//string name = (idx!=string::npos)? modName.substr(0,(idx)) : modName;
          cout<<setw(3) <<fed_id   << " "   << setw(3) << channel    << " "  << setw(30) << modName << "  "
                        << tbm     << " "   << setw(3) << rocNumber << "  " << setw(3)  << dcol    << "  " << setw(3)
                        << pix     << "   " << setw(3) << colROC     << "  " << setw(3)  << rowROC  << "  " << setw(4)
	      << data[i] << "  "  << setw(3) << num        << "  " << setw(3)  << rocOrder  << endl;
	  //" "<<name<<" "<<realRocNum<<endl;

       }

    } // if

    if(data[i]>cut1) count1++;
    if(data[i]>cut2) count2++;
    if(data[i]>cut3) {
      count3++;
      // save for noisy rocs list 
      int indexROC = codeROC(channel,rocOrder);
      if(indexROC<NumROCs) rocs[indexROC]++;
      else cout<<"roc index too big "<<indexROC<<endl;
    }
  } // for

  //cout<<num<<" total 'noisy' pixels above the cut = "<<cut<<endl;
  // // noisy ROCs
  // for(int n=0;n<4000;++n) {
  //   if(rocs[n]>0) {
  //     int chanR=0, rocR=0;
  //     decodeROC(n,chanR, rocR);
  //     cout<<" channel "<<chanR<<" roc "<<rocR<<" "<<rocs[n]<<endl;
  //     rocs[n]=0;
  //   } // if
  // } // for


}

void HotPixels::printROCs(int fed_id, int cut) {
  int channel=0, rocOrder=0;

  if(fed_id==1200) {
    cout<<" Noisy ROCs, Threshold = "<<cut<<endl;
    cout<<"fed chan     module                   tbm roc count "<<endl;   
  }

  // if(fed_id==32) {
  //   cout << endl;
  //   cout<<" Noisy ROCs, Threshold = "<<cut<<endl;
  //   cout<<"fed chan     module                     plq roc count "<<endl;
  // }

  // noisy ROCs
  for(int n=0;n<NumROCs;++n) {
    if(rocs[n]>0) {
      if(rocs[n]>cut) {
	decodeROC(n,channel, rocOrder);
	// Get the module name and tbm type 
	string modName = " ",tbm=" ";
	int rocNumber=-1;
	// this is maodule and roc name 
	string name = MyConvert::rocModuleNameFromFedChan(fed_id,channel,rocOrder,tbm);
	string::size_type idx;
	idx = name.find("_ROC");
	if(idx != string::npos) {
	  modName = name.substr(0,idx);
	  string rocName = name.substr(idx+4,name.length());
	  rocNumber = atoi(rocName.c_str());
	}

	// just for testin of the real roc number 
	int realRocNum = -1;
        if (modName[0]=='F') {
          //endcap module: retrieve the ROC number from the name
	  if(tbm=="A") realRocNum = rocOrder; // shift for TBM-N
	  else if(tbm=="B") realRocNum = rocOrder + 8; // shift for TBM-N
	  else cout<<" unknown "<<tbm<<endl;

        } else { // bpix 

	  int layer = MyConvert::layerFromName(modName);
	  //int layer0=-1;
	  //string::size_type id;
	  //if     ( modName.find("_LYR1_") != string::npos ) layer0=1;  
	  //else if( modName.find("_LYR2_") != string::npos ) layer0=2;  
	  //else if( modName.find("_LYR3_") != string::npos ) layer0=3;  
	  //else if( modName.find("_LYR4_") != string::npos ) layer0=4;  
	  //if(layer!=layer0) cout<<" big big error"<<endl;
	  //cout<<" bpix "<<layer<<" "<<modName<<endl;

	  if( layer==1 ) { // layer  1
	    //cout<<" this is layer 1 "<<modName<<endl;
	    bool fModule = false;// this is an h-module 
	    if( modName.find("F_MOD") != string::npos) fModule=true;
	    
	    if(fModule) { // F-module 
	      
	      if     (tbm=="A1") realRocNum = rocOrder; // shift for TBM-N
	      else if(tbm=="A2") realRocNum = rocOrder + 2; // shift for TBM-N
	      else if(tbm=="B1") realRocNum = rocOrder + 12; // shift for TBM-N
	      else if(tbm=="B2") realRocNum = rocOrder + 14; // shift for TBM-N
	      else cout<<" unknown "<<tbm<<endl;
	      
	    } else { // H-module
	      
	      if     (tbm=="A1") realRocNum = rocOrder + 4; // shift for TBM-N
	      else if(tbm=="A2") realRocNum = rocOrder + 6; // shift for TBM-N
	      else if(tbm=="B1") realRocNum = rocOrder + 8; // shift for TBM-N
	      else if(tbm=="B2") realRocNum = rocOrder + 10; // shift for TBM-N
	      else cout<<" unknown "<<tbm<<endl;
	      
	    }
	    
	  }  else {
	    
	    if(layer==2) {
	      //cout<<" layer2 "<<endl;
	      if     (tbm=="A1") realRocNum = rocOrder; // shift for TBM-N
	      else if(tbm=="A2") realRocNum = rocOrder + 4; // shift for TBM-N
	      else if(tbm=="B1") realRocNum = rocOrder + 8; // shift for TBM-N
	      else if(tbm=="B2") realRocNum = rocOrder + 12; // shift for TBM-N
	      else cout<<" unknown "<<tbm<<endl;
	      
	    } else if (layer==3 || layer==4)  {
	      //cout<<" layer3/4 "<<endl;
	      if(tbm=="A1") realRocNum = rocOrder; // shift for TBM-N
	      else if(tbm=="A2") realRocNum = rocOrder + 8; // shift for TBM-N
	      else cout<<" unknown "<<tbm<<endl;
	    }
	    
	  }
	  if(rocNumber != realRocNum) cout<<"ERROR - something wrong in roc number "
				     <<rocNumber<<" "<<realRocNum<<endl; 

          cout<<setw(3)<<fed_id<<" "<<setw(3)<<channel<<" "<<setw(30)<<modName<<"  "<<tbm<<"  "
              <<rocNumber<<" ("<<rocOrder<<") "<<rocs[n]<<endl;
        }

      }
      rocs[n]=0;
    } // if
  } // for


}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Main program
class FindHotPixelFromRaw : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:

  /// ctor
  FindHotPixelFromRaw( const edm::ParameterSet& cfg) : theConfig(cfg) {
    usesResource("TFileService");
    //consumes<FEDRawDataCollection>(theConfig.getUntrackedParameter<std::string>("InputLabel","source"));
    string label = theConfig.getUntrackedParameter<std::string>("InputLabel","source");
    // For the ByToken method
    rawData = consumes<FEDRawDataCollection>(label);
} 
  ~FindHotPixelFromRaw() {}
  void beginJob() override;
  //void beginRun(const edm::EventSetup&) {}
  void endJob() override;
  /// get data, convert to digis attach againe to Event
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void analyzeHits(int fed, int channel, int roc, 
		   int dcol, int pix, int adc);
  void histogramHits(int fed);

private:
  edm::ParameterSet theConfig;
  edm::EDGetTokenT<FEDRawDataCollection> rawData;

  int countEvents, countAllEvents;
  int countTest;
  int lumiBlock;
  float sumPixels, sumFedPixels[FEDs];
  HotPixels hotPixels[FEDs];
  double fraction_;
  int PixelsCount[FEDs][48][8];
  int MAXFED; // last fed
  int eventId;

  TH1D *hls, *hls1, *hls2;
  TH1D *hsize0, *hsize1, *hsize2, *hsize3;
  TH2F *hchannelRoc, *hchannelRocs, *hchannelPixels, *hchannelPixPerRoc;
  TH1D *hrocs, *hpixels, *hpixPerRoc;
  TH1D *hrow1, *hrow2,*hcol1, *hcol2,*hadc1, *hadc2; 
  //TH1D *hcol11, *hadc11; 
  TH2F *hfedchannelp, *hfedchannel;

  // many pixels 
  TH2F *hcolRow;
  TH2F *hfedchannel1, *hfedchannel2, *hfedchannel3;
  TH2F *hchannelRoc1;

};

void FindHotPixelFromRaw::endJob() {
  if(countEvents>0) {
    sumPixels /= float(countEvents);
    for(int i=0;i<FEDs;++i) sumFedPixels[i] /= float(countEvents);
  }
  
  cout<<" Total/non-empty events " <<countAllEvents<<" / "<<countEvents<<" average number of pixels "<<sumPixels<<endl;

  for(int i=0;i<FEDs;++i) {
    //hotPixels[i].print(countAllEvents,i+fedId0,fraction_);
    hotPixels[i].print(countAllEvents,i+fedId0,fraction_,hfedchannelp);
    for(int n=0; n<1000000;++n) {
      float counts= float(hotPixels[i].get_counts(n));
      float tmp = counts/float(countAllEvents);
      if(counts>0) hsize0->Fill(tmp);
      //if(counts>-1) hsize0->Fill(tmp);
      //else break;
      // if(counts>10) cout<<i<<" "<<n<<" "<<counts<<" "<<tmp<<endl;
    }
  }

  cout<<" Number of noisy pixels: for selected cut "<<count0<<" for cut at 1% "<<count1<<" for 0.1% "<<count2<<" for 0.01% "<<count3<<endl;

  // print noisy ROCs
  const int cutROC=40;
  for(int i=0;i<FEDs;++i) {
    for(int n=0; n<NumROCs;++n) {
      float counts= float(hotPixels[i].get_countsROC(n));
      if(counts>0) hsize1->Fill(counts);
      //if(counts>0) cout<<i<<" "<<n<<" "<<counts<<endl;
    }
    hotPixels[i].printROCs(i+fedId0,cutROC);
  }

  double tl1=0, tl2=0, tl3=0, tl4=0;
  double tpl1=0, tpl2=0, tpl3=0, tpl4=0;
  double cl1=0, cl2=0, cl3=0, cl4=0;
  double pl1=0, pl2=0, pl3=0, pl4=0;
  cout<<"For pixel hits above the selected threshold for fraction "<<fraction_<<endl;
  for(int i=1200; i<1294;++i) {
    double c = hotPixels[i-1200].printLayersCut(cl1,cl2,cl3,cl4);
    double cp = hotPixels[i-1200].printPixLayersCut(pl1,pl2,pl3,pl4);
    tl1 += cl1; tl2 += cl2; tl3 += cl3; tl4 += cl4;
    tpl1 += pl1; tpl2 += pl2; tpl3 += pl3; tpl4 += pl4;
    if(c>0.) cout<<"for fed "<<i
		 <<" hit count "<<cl1<<" "<<cl2<<" "<<cl3<<" "<<cl4
		 <<" pixel count "<<pl1<<" "<<pl2<<" "<<pl3<<" "<<pl4
		 <<endl;

  }
  cout<<"Total hits for fraction> "<<fraction_<<" is: hits "
      <<tl1<<" "<<tl2<<" "<<tl3<<" "<<tl4  
      <<" pixels: "<<tpl1<<" "<<tpl2<<" "<<tpl3<<" "<<tpl4<<endl;  

  tl1=0, tl2=0, tl3=0, tl4=0;
  tpl1=0, tpl2=0, tpl3=0, tpl4=0;
  cl1=0, cl2=0, cl3=0, cl4=0;
  pl1=0, pl2=0, pl3=0, pl4=0;
  cout<<"For all pixel hits, no fraction cut "<<endl;
  for(int i=1200; i<1294;++i) {
    double c = hotPixels[i-1200].printLayers(cl1,cl2,cl3,cl4);
    double cp = hotPixels[i-1200].printPixLayers(pl1,pl2,pl3,pl4);
    tl1 += cl1; tl2 += cl2; tl3 += cl3; tl4 += cl4;
    tpl1 += pl1; tpl2 += pl2; tpl3 += pl3; tpl4 += pl4;
    if(c>0.) cout<<"for fed "<<i
		 <<" hit count "<<cl1<<" "<<cl2<<" "<<cl3<<" "<<cl4
		 <<" pixel count "<<pl1<<" "<<pl2<<" "<<pl3<<" "<<pl4
		 <<endl;

  }
  cout<<"Total hits count "<<tl1<<" "<<tl2<<" "<<tl3<<" "<<tl4  
      <<" pixels "<<tpl1<<" "<<tpl2<<" "<<tpl3<<" "<<tpl4<<endl;  

  cout<<"all hit pixels "<<count4<<" for a specific channel "<<countTest<<endl;
}

void FindHotPixelFromRaw::beginJob() {
  countEvents=0;
  countAllEvents=0;
  countTest=0;
  sumPixels=0.;
  for(int n=0;n<FEDs;++n) {
    sumFedPixels[n]=0;
    for(int i=0;i<48;++i) {for(int j=0;j<8;++j) PixelsCount[n][i][j]=0;}
  }
  // Define the fraction for noisy pixels
  fraction_ = theConfig.getUntrackedParameter<double>("Fraction",0.001); 
  MAXFED = theConfig.getUntrackedParameter<int>("MAXFED",1293);
  //MAXFED=1293;
  cout<<" The noise fraction is "<<fraction_<<" FED range until "<<MAXFED<<endl;

  edm::Service<TFileService> fs;
  hls = fs->make<TH1D>( "hls", "lumi sections", 100, 0.0, 100.);
  hls1 = fs->make<TH1D>( "hls1", "lumi sections with many pxels per event", 100, 0.0, 100.);
  hls2 = fs->make<TH1D>( "hls2", "lumi sections with many pxels per roc", 100, 0.0, 100.);

  hsize0 = fs->make<TH1D>( "hsize0", "Noisy pixel rate", 10000, 0.0, 1.0);
  hsize1 = fs->make<TH1D>( "hsize1", "Noisy pixels per roc", 1000, -0.5, 999.5);
  hsize2 = fs->make<TH1D>( "hsize2", "Noisy pixels per event", 1000, -0.5, 999.5);
  hsize3 = fs->make<TH1D>( "hsize3", "Pixels per event", 1000, -0.5, 999.5);

  hrocs = fs->make<TH1D>( "hrocs", "rocs per channel", 10, -0.5, 9.5);
  hpixels = fs->make<TH1D>( "hpixels", "pixels per channel", 200, -0.5, 199.5);
  hpixPerRoc = fs->make<TH1D>( "hpixPerRocs", "pixels per roc", 100, -0.5, 99.5);

  //TH2F *hchannelRoc, *hchannelRocs, *hchannelPixels, *hchannelPixPerRoc;
  hchannelRoc = fs->make<TH2F>("hchannelRoc", "roc in a channel",48,0.,48.,9, -0.5,8.5);
  hchannelRocs = fs->make<TH2F>("hchannelRocs", "num of rocs in a channel",48,0.,48.,9, -0.5,8.5);
  hchannelPixels = fs->make<TH2F>("hchannelPixels", "pixels in a channel",48,0.,48.,200, -0.5,199.5);
  hchannelPixPerRoc = fs->make<TH2F>("hchannelPixPerRoc", "pixels in a roc",48,0.,48.,100, -0.5,199.5);

  const int n_of_FEDs = 139;
  const int n_of_Channels = 48+1;
  const float maxChan = static_cast<float>(n_of_Channels) - 0.5 + 1.0;
  hfedchannel  = fs->make<TH2F>("hfedchannel", "pixels per fed&channel",
				n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5,
				n_of_Channels, -0.5,maxChan);  
  hfedchannelp  = fs->make<TH2F>("hfedchannelp", "pixels per fed&channel",
                                          n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5,
                                          n_of_Channels, -0.5,maxChan);  


  hrow1 = fs->make<TH1D>( "hrow1", "pixel rows, l1",   101, -1.5, 99.5);
  hrow2 = fs->make<TH1D>( "hrow2", "pixel rows, l2-4", 101, -1.5, 99.5);
  hcol1 = fs->make<TH1D>( "hcol1", "pixel cols, l1",   101, -1.5, 99.5);
  hcol2 = fs->make<TH1D>( "hcol2", "pixel cols, l2-4", 101, -1.5, 99.5);
  hadc1 = fs->make<TH1D>( "hadc1", "pixel adc, l1",    300, -0.5, 299.5);
  hadc2 = fs->make<TH1D>( "hadc2", "pixel adc, l2-4",  300, -0.5, 299.5);

  //hcol11 = fs->make<TH1D>( "hcol11", "pixel cols, l1",   101, -1.5, 99.5);
  //hadc11 = fs->make<TH1D>( "hadc11", "pixel adc, l1",    300, -0.5, 299.5);

  // many pixels
  hfedchannel1  = fs->make<TH2F>("hfedchannel1", "many pixels per roc fed&channel",
				n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5,
				n_of_Channels, -0.5,maxChan);  
  hfedchannel2  = fs->make<TH2F>("hfedchannel2", "many pixels per channel fed&channel",
				n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5,
				n_of_Channels, -0.5,maxChan);  
  hfedchannel3  = fs->make<TH2F>("hfedchannel3", "many rocs per channel fed&channel",
				n_of_FEDs,-0.5,static_cast<float>(n_of_FEDs) - 0.5,
				n_of_Channels, -0.5,maxChan);  

  hchannelRoc1 = fs->make<TH2F>("hchannelRoc1", "many pixels per roc roc/chann",48,0.,48.,9, -0.5,8.5);
  hcolRow = fs->make<TH2F>("hcollRow", "many pixels per roc",52,0.,51.,80, 0.,79.);
  //hcolRow = fs->make<TH2F>("hcollRow", "many pixels per roc",26,0.,25.,160, 0.,159.);

}
//-----------------------------------------------------------------------
void FindHotPixelFromRaw::histogramHits(int fed) {
  const int cutPixPerRoc=20;
  const int cutPixPerChan=100;
  const int cutRocsPerChan=4;

  int nPixPerChannel=0, nRocsPerChannel=0; // , nPixPerRoc=0;
  int n = fed-1200; // fed index
  for(int i=0;i<48;++i) {
    nRocsPerChannel=0;
    nPixPerChannel=0;

    for(int j=0;j<8;++j) {
      int count = PixelsCount[n][i][j];
      if(count>0) {
	nPixPerChannel += count;	
	nRocsPerChannel++;
	hchannelRoc->Fill(float(i),float(j),float(count));
	if(count>cutPixPerRoc) {
	  cout<<"many pixels per ROC "<<count<<" fed "<<fed<<" chan "<<i
	      <<" roc "<<j<<" for event "<<eventId<<endl;
	  hfedchannel1->Fill(float(n),float(i));
	  hchannelRoc1->Fill(float(i),float(j));
	  hls2->Fill(float(lumiBlock));
	}
      } // if
      hpixPerRoc->Fill(float(count));
      hchannelPixPerRoc->Fill(float(i),float(count) );
      PixelsCount[n][i][j]=0;
    } // roc

    hchannelRocs->Fill(float(i),float(nRocsPerChannel));
    hchannelPixels->Fill(float(i),float(nPixPerChannel));
    hrocs->Fill(float(nRocsPerChannel));
    hpixels->Fill(float(nPixPerChannel));
    if(nPixPerChannel>cutPixPerChan) {
      hfedchannel2->Fill(float(n),float(i));
      cout<<"many pixels per chan "<<nPixPerChannel<<" fed "<<fed<<" chan "<<i
	  <<" for event "<<eventId<<endl;
    }
    if(nRocsPerChannel>cutRocsPerChan) {
      hfedchannel3->Fill(float(n),float(i));
      cout<<"many rocs per chan "<<nRocsPerChannel<<" fed "<<fed<<" chan "<<i
	  <<" for event "<<eventId<<endl;
    }

  } // channel

  return;
}
//-----------------------------------------------------------------------
void FindHotPixelFromRaw::analyzeHits(int fed, int channel, 
				      int roc, int dcol, int pix, int adc) {
  //TH2F *hchannelRoc, *hchannelRocs, *hchannelPixels, *hchannelPixPerRoc;
  static int fed0=-1, channel0=-1, roc0=-1;
  static int numPixPerChannel=0, numRocsPerChannel=0, numPixPerRoc=0;
  // for layer-1
  const unsigned int rowmsk = 0x7f00; 
  const unsigned int colmsk = 0x1f8000;
  //if(fed!=1200) return;

  // count pixels per roc, channels go from 1 to 48
  PixelsCount[fed-1200][channel-1][roc]++;

  // some how I have to get the layer number in an efficient way  
  string tbm;
  // this is very inefficient 
  string  name = MyConvert::rocModuleNameFromFedChan(fed,channel,roc,tbm);
  int layer = MyConvert::layerFromName(name);

  if(layer==1) { // layer 1
    //cout<<" layer 1: "<<roc<<" "<<dcol<<" "<<pix<<" "<<adc<<endl;
    // do a customise computation of col/row from dcol/pix, move to data() later 
    int tmp = (dcol<<16) + (pix<<8);
    int colROC = (tmp&colmsk)>>15;
    int rowROC = (tmp&rowmsk)>>8;

    //cout<<" layer 1: "<<roc<<" "<<colROC<<" "<<rowROC<<" "<<adc<<endl;

    hrow1->Fill(float(rowROC));
    hcol1->Fill(float(colROC));
    hadc1->Fill(float(adc));

    // if(rowROC==80) {
    //   hcol11->Fill(float(colROC));
    //   hadc11->Fill(float(adc));
    // }

  } else { // layers 2,3,4

    // First find if we are in the first or 2nd col of a dcol.
    int colEvenOdd = pix%2;  // module(2), 0-1st sol, 1-2nd col.
    // Transform
    int colROC = dcol * 2 + colEvenOdd; // col address, starts from 0
    int rowROC = abs( int(pix/2) - 80); // row addres, starts from 0

    //cout<<" layer 2-4: "<<roc<<" "<<colROC<<" "<<rowROC<<" "<<adc<<endl;

    hrow2->Fill(float(rowROC));
    hcol2->Fill(float(colROC));
    hadc2->Fill(float(adc));

  }

  //if(count>20) hcolRow->Fill(float(col),float(row));
  //return;

  hchannelRoc->Fill(float(channel),float(roc));
  
  if(fed!=fed0) { // new fed
    //cout<<" new fed "<<endl;
    numPixPerChannel=1;
    numRocsPerChannel=1;

    fed0=fed;
    channel0=-1;
    roc0=-1;
  } else { // old fed
    //cout<<" old fed "<<endl;

    if(channel!=channel0) { // new channel
      //cout<<" new channel "<<endl;
      if(numRocsPerChannel>0) hchannelRocs->Fill(float(channel),float(numRocsPerChannel));
      if(numPixPerChannel>0)  hchannelPixels->Fill(float(channel),float(numPixPerChannel));

      numPixPerChannel=1;
      numRocsPerChannel=1;

      channel0=channel;
      roc0=-1;
    } else { // old channel
      //cout<<" old channel "<<endl;
      numPixPerChannel++;
      
      if(roc!=roc0) { // new roc
	//cout<<" new roc"<<endl;
	numRocsPerChannel++;
	if(numPixPerRoc>0)  hchannelPixPerRoc->Fill(float(channel),float(numPixPerRoc));
	numPixPerRoc=1;
	roc0=roc;
      } else {
	//cout<<" old roc "<<endl;
	numPixPerRoc++;
      } // roc 

    } // channel

  } // fed

  //cout<<fed<<" "<<channel<<" "<<roc<<" "<<dcol<<" "<<pix<<endl;
  return;
}
//--------------------------------------------------------------------------
void FindHotPixelFromRaw::analyze(const  edm::Event& ev, const edm::EventSetup& es) {
  const int maxPixelsPerEvent = 100;
  // Access event information
  //run       = ev.id().run();
  long eventCMSSW  = ev.id().event();  // CMSSW event # , unsigned long long 
  lumiBlock = ev.luminosityBlock();
  //bx        = ev.bunchCrossing(); // CMSSW bx
  //int orbit     = ev.orbitNumber();
  hls->Fill(float(lumiBlock));

  edm::Handle<FEDRawDataCollection> buffers;
  //static std::string label = theConfig.getUntrackedParameter<std::string>("InputLabel","source");
  //static std::string instance = theConfig.getUntrackedParameter<std::string>("InputInstance","");
  //ev.getByLabel( label, instance, buffers);
  ev.getByToken(rawData , buffers);  // the new bytoken 

  //std::pair<int,int> fedIds(FEDNumbering::MINSiPixelFEDID, FEDNumbering::MAXSiPixelFEDID);
  std::pair<int,int> fedIds(1200, MAXFED);
  
  //PixelDataFormatter formatter(0); // to get digis
  //bool dummyErrorBool;
  
  typedef uint32_t Word32;
  typedef uint64_t Word64;
  int status=0;
  int countPixels=0;
  int countErrors=0;
  eventId = -1;
  int channel=-1, roc=-1, dcol=-1, pix=-1, adc=-1;
  
  countAllEvents++;
  if(printHeaders) cout<<" Event = "<<countEvents<<" "<<eventCMSSW<<" ls "<<lumiBlock<<endl;  
  //edm::DetSetVector<PixelDigi> collection; // for digis only

  // Loop over FEDs
  for (int fedId = fedIds.first; fedId <= fedIds.second; fedId++) {

    if(printHeaders) cout<<" For FED = "<<fedId<<endl;

    if( (fedId-fedId0)>FEDs ) {cout<<" skip fed, id too big "<<fedId<<endl; continue;}
    //if(fedId != 1263) continue; // select just 1 fed

    PixelDataFormatter::Errors errors;
    
    //get event data for this fed
    const FEDRawData& rawData = buffers->FEDData( fedId );
    
    int nWords = rawData.size()/sizeof(Word64);
    if(DEBUG) cout<<" size "<<nWords<<endl;

    if(rawData.size()==0) continue;  // skip if not data for this fed    

    // check headers
    const Word64* header = reinterpret_cast<const Word64* >(rawData.data()); 
    if(DEBUG) cout<<hex<<*header<<dec<<endl;
    eventId = MyDecode::header(*header, printHeaders);
    //if(fedId = fedIds.first) 

    const Word64* trailer = reinterpret_cast<const Word64* >(rawData.data())+(nWords-1);
    if(DEBUG) cout<<hex<<*trailer<<dec<<" "<<eventId<<endl;
    status = MyDecode::trailer(*trailer,printHeaders);

    int countPixelsInFed=0;
    int countErrorsInFed=0;
    // Loop over payload words
    for (const Word64* word = header+1; word != trailer; word++) {
      static const Word64 WORD32_mask  = 0xffffffff;
      Word32 w = 0;
      for(int n=0; n<2; ++n) { // 2 words in a long word
	if(n==0) w = *word         & WORD32_mask;
	else     w = (*word >> 32) & WORD32_mask;

	status = MyDecode::data(w, channel, roc, dcol, pix, adc, printData);
	//if(fedId==1253 && channel==44) cout<<status<<" "<<roc<<" "<<dcol<<" "<<pix<<endl;
	if(status>0) {
	  //int rocOrder=0, col=-1, row=-1; 
	  //string tbm;
	  //string  name = MyConvert::rocModuleNameFromFedChan(fedId,channel,rocOrder,tbm);
	  //int layer = MyConvert::layerFromName(name);
	  //if(fedId==1253 && channel==44) cout<<roc<<" "<<dcol<<" "<<pix<<endl;
	  //if(fedId==1207 && channel==47 && roc==3) countTest++;  // just testing
	  countPixels++;
	  countPixelsInFed++;
	  hfedchannel->Fill(fedId-fedId0,channel);
	  if(findHot) {
	    int count = hotPixels[fedId-fedId0].update(channel,roc,dcol,pix);
	    // if(count>1) {
	    //   cout<<fedId<<" "<<channel<<" "<<roc<<" "
	    // 	  <<dcol<<" "<<pix<<" "<<count<<endl;
	    //   // assume layers2-4
	    //   int colROC = (dcol * 2) + (pix%2); // col address, starts from 0
	    //   int rowROC = abs( int(pix/2) - 80); // row addres, starts from 0
	    //   hcolRow->Fill(float(colROC),float(rowROC));
	    // }
	  } else {
	    analyzeHits(fedId,channel,roc,dcol,pix,adc);
	  }
	} else if(status<0) countErrorsInFed++;
      } // for 2 words
      //cout<<hex<<w1<<" "<<w2<<dec<<endl;
    } // loop over words
    
    countErrors += countErrorsInFed;
    
    //convert data to digi (dummy for the moment)
    //formatter.interpretRawData( dummyErrorBool, fedId, rawData,  collection, errors);
    //cout<<dummyErrorBool<<" "<<digis.size()<<" "<<errors.size()<<endl;
    
    if(countPixelsInFed>0)  {
      sumFedPixels[fedId-fedId0] += countPixelsInFed;
    }

    // if(fedId==1200) histogramHits(fedId); // do for one fed only
    histogramHits(fedId);
 
  } // loop over feds

  hsize2->Fill(float(countPixels));
  if(countPixels>0) {
    //cout<<"EVENT: "<<countEvents<<" "<<eventId<<" pixels "<<countPixels<<" errors "<<countErrors<<endl;
    sumPixels += countPixels;
    countEvents++;
    hsize2->Fill(float(countPixels));
    if(countPixels>maxPixelsPerEvent) hls1->Fill(float(lumiBlock));

    //int dummy=0;
    //cout<<" : ";
    //cin>>dummy;
  } // if

}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(FindHotPixelFromRaw);
