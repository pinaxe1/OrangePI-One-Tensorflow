'''
The program expect presence of /dev/video1 device which is turn created by v4l2loopback and receiving feed grom vidcopy
to activate device next 7 commands should be performed on OrangePi Armbian

sudo sunxi-pio -m "PG11<1><0><1><1>"
sudo modprobe gc2035
sudo modprobe vfe_v4l2
sleep 5
sudo modprobe v4l2loopback
cd ~/vidcopy
./vidcopy -w 800 -h 600 -r 30 -i /dev/video0 -o /dev/video1 -f UYVY
'''

import cv2
c = cv2.VideoCapture(1)

while(1):sudo
  _,f = c.read()
  cv2.imshow('Camera Orange Pi',f)
  k = cv2.waitKey(5)
  if k==1048603:
      #Esc key to stop, or 27 depending your keyboard
      #Touche ESC appuyee. le code peut dependre du clavier. Normalement 27
      break
  elif k==-1:
      continue
  #uncomment to know the code of of the key pressed
  #Decommenter pour connaitre le code de la touche pressee
  #else:
      #print k

cv2.destroyAllWindows()
