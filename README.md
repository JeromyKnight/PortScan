# PortScan
port scanner built using socket and tkinter libraries, a simple tool designed to help locate network printers.

Designed to quickly locate network printers using arp-ping to CIDR range of local subnet.

By default it should detect the IP, format CIDR notation, and populate the IP field.

Default port is 9100 as this is the most common port used by network printers, but there are alternative ports and I often will use port 80 to look for built in web page if i can't locate with a standrad port.

Delay is how long to wait for a response from the ip/port being scanned. The default of .1 seems to be reliable and scan completes in about 30 seconds. You can shorten this but it will reduce accuracy. Be careful making it longer, at a 1 second delay it would take about 5 minutes to run.

In the dist folder you will find a standalone .exe file created with pyinstaller for use on Windows machines.
