#L1 Builder

The purpose of this script is to allow someone who has a set of images under an img folder and that follow a sequence to convert that into html pages that are linked in that order.<br><br>
Example: img/1.png img/2.png img/3.png <br>
Would generate:<br><br>
index1.html<br>
index2.html<br>
index3.html<br>

Each one of the index files has an anchor tag that surrounds the image and on click will take you to the next one.<br>
###Whats the catch?

You need to have the following file/folder structure<br>

* makeElOne.py (file)
* www (folder)
	* img (folder)

Thats it!<br>

##How to use?
Download or fork the contents of this repository. Puth the makeElOne.py file next to the www folder of your application.
The generated index files will go under the www folder.
Enjoy!
