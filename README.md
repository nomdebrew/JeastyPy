# JeastyPy
Computer vision application to classify yeast cells.

<h2>Yeast Problems</h2>
<p>
	<img src="20170218_120230.jpg" height="240" style="transfor: rotate(90deg);">
	Too little yeast can result in skunky beer, overly fruity beer, stalled fermentation
	<img src="20170209_074020.jpg" height="240">
	Too much yeast can result in little flavor, blow off, volume loss
</p>


<h2>Data Collecting and Preprocessing</h2>
<p>The data was captured from a camera through a traditional benchtop microscope. The image was then cropped down to the portion that contains the relavent information. The individual cells then had bounding boxes drawn around them and were classified as alive or dead. Lastly the cells were seperated from the rest of the image.<p>
<p>
	<img src="/yeast_cell_data/raw_files/20181115_101011.jpg" height="240">
	<img src="bounding_box.png" height="240">
	<img src="tensorflow/test_images/alive278.jpg" height="240">
</p>


<h2>Classification: Alive vs. Dead</h2>
<h3>Alive Cells</h3>
<p>
	<img src="tensorflow/test_images/alive60.jpg" height="240">
	<img src="tensorflow/test_images/alive278.jpg" height="240">
	<img src="tensorflow/test_images/alive856.jpg" height="240">
</p>
<h3>Dead Cells</h3>
<p>
	<img src="tensorflow/test_images/dead27.jpg" height="240">
	<img src="tensorflow/test_images/dead62.jpg" height="240">
	<img src="tensorflow/test_images/dead649.jpg" height="240">
</p>




<p>
	<img src="lievito1.jpg" height="240">
	<img src="lievito2.jpg" height="240">
</p>