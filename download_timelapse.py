from goprocam import GoProCamera
from goprocam import constants

gpCam = GoProCamera.GoPro()
while True:
	TIMER=1
	gpCam.downloadLastMedia(gpCam.take_photo(TIMER), 'static/img.JPG') #10 second timelapse. 
