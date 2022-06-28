## Android Camera to PC

### This allows you to use your Android phone as webcam on your PC without installing any shady stuff.

1. Requirements:

	On your PC:
	- OBS - https://obsproject.com/
	- Python3

	On your Phone:
	- [android apk: andythebreaker/camerax_color_detect](https://github.com/andythebreaker/camerax_color_detect)
	- [download from github](https://github.com/andythebreaker/camerax_color_detect/files/8709069/app-release.zip)
	
	On your Server:
	- [node-media-server](https://www.npmjs.com/package/node-media-server)
	- [REF](https://hackmd.io/@andythebreaker/rJ66DIzQt#%E4%BC%BA%E6%9C%8D%E5%99%A8)

2. How to use:

#### on server

- `mkdir any_name`
- `cd any_name`
- `npm install node-media-server`
- `vi app.js`
- copy code from https://hackmd.io/@andythebreaker/rJ66DIzQt#codenodejs
- edit code port

	- Run `pip install -r requirements.txt`
	- Go to `webcam.py` and change url to `rtmp://yourip:yourport`
	- Run IP Webcam app and then start `webcam.py`
	- Open OBS and add new `Window Capture` and add camera window
	- Under the `Controls` in OBS windows, click `Start Virtaul Camera`
	- Now go to app that you want to use camera with and just select `OBS-Camera`

1. Notes:
   
	- 15 sec delay
