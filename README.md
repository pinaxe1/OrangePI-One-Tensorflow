# OrangePI-One-Tensorflow
OrangePI One 
HOW-TO install Armbian Stretch, Tensorflow, and so on.

From  https://dl.armbian.com/orangepione/archive/
download Armbian_5.69_Orangepione_Debian_stretch_next_4.19.13.7Z
Unpack with 7zip
With  balena Etcher write image Armbian_5.69_Orangepione_Debian_stretch_next_4.19.13.img to a flash card. 
Even 2Gb card is enough
Start Armbian.
user: root
password: 1234
System will ask to change default password and create a non administrative user.
Update and upgrade system.

sudo apt-get update
sudo apt-get upgrade

sudo shutdown -r now
------------------------------------------------------------------------------
Now installing Tensorflow.

sudo apt-get install python3-dev python3-pip 
sudo apt install libatlas-base-dev
pip3 install -U virtualenv 

Nexts two lines supposed to fix virtualenv but seems make it just worse ===
sudo apt install command-not-found
sudo update-command-not-found
                                                                        ===
Standard TF installation wouldn't work so download a wheel from dropbox.
wget https://www.dropbox.com/s/gy4kockdbdyx85j/tensorflow-1.0.1-cp35-cp35m-linux_armv7l.whl
original https://github.com/samjabrahams/tensorflow-on-raspberry-pi/issues/92
or something from https://github.com/lhelontra/tensorflow-on-arm/releases

It wouldn't work without virtualenv. If venv is not activated pip3 install will produce an error.
So create and activate venv 

virtualenv --system-site-packages -p python3 ./venv

if virtualenv wouldn't start run it as
python3 virtualenv --system-site-packages -p python3 ./venv

source ./venv/bin/activate


Install numpy before tensorflow. For some reason pip3 hangs if numpy installed by TF Wheel.

pip3 install --upgrade numpy
pip3 install --upgrade tensorflow-1.0.1-cp35-cp35m-linux_armv7l.whl

Check if a TF installed correctly
run python
import tensorflow as tf
a= tf.constant(2)
b=tf.constant(3)
c=tf.add(a,b)
se=tf.Session()
se.run(c)
5
========================================================================
Fcn-Mobilenet reqires SciPy and Pillow Not that it relies on those too much but requiers.
SciPy and Pillow would not install with Pip into venv
So install them global
sudo apt install python3-scipy
sudo apt install python3-Pillow
If Pillow still would not install use script to install it dependencies

Script to install Pillow dependencies
https://github.com/python-pillow/Pillow/blob/master/depends/debian_8.2.sh
------------
#!/bin/sh

#
# Installs all of the dependencies for Pillow for Debian 8.2
# for both system Pythons 2.7 and 3.4
#
# Also works for Raspbian Jessie
#

sudo apt-get -y install python-dev python-setuptools \
    python3-dev python-virtualenv cmake
sudo apt-get -y install libtiff5-dev libjpeg62-turbo-dev zlib1g-dev \
     libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev \
     python-tk python3-tk libharfbuzz-dev libfribidi-dev

./install_openjpeg.sh
./install_imagequant.sh
./install_raqm.sh
------------

To get rid of pillow and scipy use pyPNG lib
https://github.com/drj11/pypng/ 

========================================================================
And here arre couple of useful Linux commands 
to download files from Web
wget -r -nH -nc http://192.168.1.12/Data_zoo/camvid/
wget -r -nH -nc http://192.168.1.12/logs/
wget -r -nH -nc http://192.168.1.12/Model_zoo/


to show images without X server GUI
apt install fbi
fbi logs/*.png

