#include <opencv2/core/core.hpp>
    #include <opencv2/imgproc/imgproc.hpp>
    #include <opencv2/highgui/highgui.hpp>
    #include <opencv2/opencv.hpp>

    using namespace cv;

    int main(int, char**) {
        cv::VideoCapture vcap;
        cv::Mat image;
        const std::string videoStreamAddress = "rtmp://192.168.173.1:1935/live/test.flv";
        if(!vcap.open(videoStreamAddress)) {
            std::cout << "Error opening video stream or file" << std::endl;
            return -1;
        }

        cv::namedWindow("Output Window");
        cv::Mat edges;
        for(;;) {
            if(!vcap.read(image)) {
                std::cout << "No frame" << std::endl;
                cv::waitKey();
            }
            cv::imshow("Output Window", image);
            if(cv::waitKey(1) >= 0) break;
        }
    }