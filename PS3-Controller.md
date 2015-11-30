#PS3 Controller

The $ denotes the beginning of a line of code to be entered in the Terminal. 
First make sure your Pi is up to date (This may take a while depending on your pi):
	
	$sudo apt-get update
	
Then make install the bluetooth dongle support. This is different for each dongle so I will let you do that part.
There are tutorials all over the place explaining what to do.

Next install the bluetooth support (Drivers, compilers and such) this one will take a long time so get comfortable:   

	$ denotes a new line. this first one is a long line.
	$sudo apt-get install bluez-utils bluez-compat bluez-hcidump checkinstall libusb-dev libbluetooth-dev joystick
      
Once this is done you will need to download and compile the controller utility:

	$wget http://www.pabr.org/sixlinux/sixpair.c
    	$gcc -o sixpair sixpair.c -lusb

Next connect the PS3 controller to the Pi using the USB cable and type the following
    
    	$sudo ./sixpair

If this is successful, it will return something like this:

	Current Bluetooth master: 00:10:60:57:15:C7
 	Setting master bd_addr to: 00:10:60:57:15:C7 

If no controller is connected, a message will pop up saying "No controller found on USB busses". In my experience I only     needed to run the sudo ./sixpair command once for each controller, as long as you haven't reset it. Now run the following 		to download sixad, the controller manager.
    
    	$wget http://sourceforge.net/projects/qtsixa/files/QtSixA%201.5.1/QtSixA-1.5.1-src.tar.gz
    	$sudo tar xfvz QtSixA-1.5.1-src.tar.gz
    	$cd QtSixA-1.5.1/sixad
    	$sudo make
    	$sudo mkdir -p /var/lib/sixad/profiles
    	$sudo checkinstall

Once that is done, run the following to allow the controller mangager to run at boot. Now when you reboot the Pi, sixad will automatically run.

	$sudo update-rc.d sixad defaults
#PS3 Controller
Finally, unplug the controller and reboot the system.

	$sudo reboot

Once it is up and running again, sixad will already be running so all you have to do is press the PS button. If it does not connect or doesnt recognize it, first try restarting sixad.

    	$sudo sixad --stop
    	$sudo sixad --start
    
At this point it will prompt you to press the PS button. When you do so it will display this if it connected successfully.
This will be displayed on the screen.

	sixad-bin[2535]: started
	sixad-bin[2535]: sixad started, press the PS button now
	sixad-bin[2535]: unable to connect to sdp session
	sixad-bin[2535]: Connected Sony Computer Entertainment Wireless Controller

If it still wont connect then try plugging the controller in again and running.

	$sudo ./sixpair

Each time you start the pi, you simply have to press the PS button on the controller to connect it, as long as you ran the update -rc command above. However if you want to connect a second controller on boot up, in the terminal just type 
	$sixad --stop
	$sixad --start
Then press the PS button on the second controller.

