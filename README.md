#L1 Builder

The purpose of this script is to allow someone who has a set of images under an img folder and that follow a sequence (Example: img/1.png img/2.png img/3.png) to convert that into html pages that are linked in that order.
So the above list of images would generate:<br>
index1.html<br>
index2.html<br>
index3.html<br>

Each one of the index files points to the next one.<br>
###Whats the catch?

You need to have the following file/folder structure<br>

* makeElOne.py (file)
* www (folder)
	* img (folder)

Thats it!<br>
The generated index files will go under the www folder.
Enjoy!
