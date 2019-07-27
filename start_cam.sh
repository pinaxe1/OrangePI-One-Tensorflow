sudo sunxi-pio -m "PG11<1><0><1><1>"
sudo modprobe gc2035
sudo modprobe vfe_v4l2
sleep 5
sudo modprobe v4l2loopback
cd ~/vidcopy
./vidcopy -w 800 -h 600 -r 30 -i /dev/video0 -o /dev/video1 -f UYVY
