import cv2
from ultralytics import YOLO
print("Starting Wrong Way Detection...")
model=YOLO("yolo11n.pt")
cap=cv2.VideoCapture("road.mp4")
if not cap.isOpened():
   print("ERROR:road.mp4 cannot be opened!")
   input("Press Enter to exit...")
   exit()
print("Video opened successfully!")

previous_positions={}
while True:
   ret,frame=cap.read()
if not ret:
   printf("Video finished.")
   break
frame=cv2.resize(frame,(960,540))
results=model.track(
  frame,
  persist=True,
  classes=[2,3,5,7],
  conf=0.25,
  imgsz=640,
  verbose=False
}
annotated_frame=results[0].plot()
cv2.putText(
   annotated_frame,
   "AI-BASED WRONG WAY VEHICLE DETECTION",
   (20,40),
   cv2.FONT_HERSHEY_SIMPLEX,
   0.8,
   (0,255,255),
   2
)

vehicle_found=False
wrong_way=False

boxes=results[0].boxes
if boxes is not None and len(boxes)>0:
  for box in boxes:
     vehicle_found=True
     x1,y1,x2,y2=box.xyxy[9].cpu().numpy()
     cx=int((x1+x2)/2)
     cy=int((y1+y2)/2)
     if box.id is not None:
        track_id=int(box.id[0])
        if track_id in previous_positions:
        old_y=previous_position[track_id]
        if cy<old_y-5:
           wrong_way=True
      previous_position[track_id]=cy
if not vehicle_found:
  cv2.putText(
     annotated_frame,
     "No Vehicle Detected",
     (20,85),
     cv2.FONT_HERSHEY_SIMPLEX,
     0.8,
     (0,0,255),
     2
   )
    elif wrong_way:
     cv2.putText(
       annotated_frame,
       "WARNING:WRONG WAY VEHICLE!",
       (20,85),
       cv2.FONT_HERSHEY_SIMPLEX,
       0.8,
       (0,0,255),
       2
     )
       cv2.putText(
       annotated_frame,
     "Safety Response: CONTROLLED STOP",",
     (20,125),
     cv2.FONT_HERSHEY_SIMPLEX,
     0.7,
     (0,165,255),
     2
   )
  else:
     cv2.putText(
     annotated_frame,
     "Vehicle Detected",
     (20,85),
     cv2.FONT_HERSHEY_SIMPLEX,
     0.8,
     (0,255,0),
     2
   ) 
     cv2.putText(
     annotated_frame,
     "Direction: Normal",
     (20,125),
     cv2.FONT_HERSHEY_SIMPLEX,
     0.7,
     (255,255,255),
     2
   )
    cv2.imshow(
     "AI WRONG WAY VEHICLE DETECTION", 
     annotated_frame
    )
    if cv2.waitKey(20)&0xFF==ord("q"):
       break
    cap.release()
    cv2.destroyAllWindows()
    print("Program completed.")
    input("Press Enter to close...")
