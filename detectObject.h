/*****************************************************************************
*   Face Recognition using Eigenfaces or Fisherfaces
*****************************************************************************/

#pragma once


#include <stdio.h>
#include <iostream>
#include <vector>

// Include OpenCV's C++ Interface
#include "opencv2/opencv.hpp"


using namespace cv;
using namespace std;


// Search for just a single object in the image, such as the largest face, storing the result into 'largestObject'.
void detectLargestObject(const Mat &img, CascadeClassifier &cascade, Rect &largestObject, int scaledWidth = 320);


// Search for many objects in the image, such as all the faces, storing the results into 'objects'.
void detectManyObjects(const Mat &img, CascadeClassifier &cascade, vector<Rect> &objects, int scaledWidth = 320);
