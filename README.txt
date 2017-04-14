Author: Sirajus Salekin
=====================================================================
Setup:

To fulfill the dependencies, make install.sh file exexcutable by
typing "chmod +x install.sh", and then run "./install.sh"

If you want to install the dependencies manually, enter
the following commands:

	sudo pip install matplotlib
	sudo pip install ascii_graph
	sudo pip install validators

You should be ready to use the program now.
========================================================================

How to use the program:

1. cd to program directory

2. Type in the following command on termina:
	 python driver.py [file location]
   File could be located anywhere, but make sure to type the address correctly.
   For a web url, use full address, e.g. "http://norvig.com/big.txt"

3. If you want to enter a file that contains stop words, use the following format:
	python driver.py [file location] [stop file location]
   Note: stop_file can only be accessed locally.
   Note: stop_file is expected to be formatted one stop word per line, in a .txt file.

4. There will be instructions onscreen, follow them.

5. If you choose to see graphical histogram, you need to close the figure window before 
   trying with another set of options.

6. If you want to use different set of input files, quit the program and enter them 
   on command line directly
