import cv2
import numpy as np
 
# Create a VideoCapture object
cap = cv2.VideoCapture("videos/VID_20200107_191220.mp4")
 
frame_count = 172
totalFrames = 0
skip_frames = 10
# Check if camera opened successfully
if (cap.isOpened() == False): 
  print("Unable to read camera feed")
 
while(True):
  ret, frame = cap.read()
 
  if ret == True: 

    if totalFrames % skip_frames == 0:
     
      # Write the frame into the file 'output.avi'
      #out.write(frame)
      image_path = "dataset/"+str(frame_count)+".jpg"

      cv2.imwrite(image_path,frame)
      frame_count+=1
      # Display the resulting frame    
      cv2.imshow('frame',frame)
   
      # Press Q on keyboard to stop recording
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
  # Break the loop
  else:
    break 
  totalFrames+=1
 
# When everything done, release the video capture and video write objects
cap.release()
#out.release()
 
# Closes all the frames
cv2.destroyAllWindows() 