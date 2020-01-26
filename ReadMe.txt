1) Basic packages list :

sudo apt-get install build-essential libgtk2.0-dev libjpeg-dev libtiff4-dev libjasper-dev libopenexr-dev cmake python-dev python-numpy python-tk libtbb-dev libeigen2-dev yasm libfaac-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev libqt4-dev libqt4-opengl-dev sphinx-common texlive-latex-extra libv4l-dev libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev 

2) 
   Get Open CV version. Download from :

https://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.10/opencv-2.4.10.zip 	

3) Install OpenCV as follows: 
 
 a) unzip opencv-2.4.10.zip

 b) cd opencv-2.4.10

 c) mkdir build
 
 d) cd build

 e) cmake -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=ON -D WITH_QT=ON -D WITH_OPENGL=ON -D WITH_FFMPEG=OFF ..

 f) make 

 g) sudo make install


4) Now take the face recognition software

  a) Unzip the package

  b) goto th build directory
  
    # cd build

  c) Issue Following Command

      cmake ../

  d) make

  e) Execute ./WebcamFaceRec


5)Install database

sudo apt-get install libmysqlcppconn-dev

sudo apt-get install mysql-server mysql-client
sudo apt-get install libmysqlclient-dev



6) sudo pip install -U scikit-image

 sudo apt-get install pip

 sudo apt-get install pip*

 sudo apt-get install python-pip

 sudo apt-get install python-scipy

 sudo pip install scipy

 sudo apt-get update

 sudo apt-get install python-scipy
 
 sudo apt-get install python-numpy

 sudo pip install -U scikit-image

 sudo apt-get install python-dateutils

 sudo apt-get install python-dateutil*

 sudo apt-get install python-scipy*

 sudo apt-get install python-scipy-dev
 
 sudo apt-get install python-scipy-dbg

 sudo apt-get install python-measure

 sudo apt-get install python-measure*

 sudo pip install measure

 sudo pip install measure*

 sudo pip install matplotlib


7) Make two folders where your code is located  

  # This contains the Stored images of all Student when u use recognition mode only

  mkdir testImage  
 
 # This contains the Stored images of all Student when u have gone through normal mode

  mkdir studentImages    
  
  8) Follow video to run the program
  
  9) Executable file in /build

