

cv::Mat img;
std::string windowName = "Video Feed";

cv::namedWindow(windowName);
cv::VideoCapture vStream(0);

if (!vStream.isOpened()) {
    std::cout << "Failed to open video stream.\n";
}

while (true) {
    vStream >> img;

    cv::imshow(windowName, img);
    cv::waitKey(25);	
}