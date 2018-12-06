
<h1>JeastyPy: Computer vision application to classify yeast cells.</h1>
	<h2>What is JeastyPy</h2>
	<h3>Yeast Problems</h3>
	<p>
		<img src="20170218_120230.jpg" height="240" style="transfor: rotate(90deg);">
		Too little yeast can result in skunky beer, overly fruity beer, stalled fermentation
		<img src="20170209_074020.jpg" height="240">
		Too much yeast can result in little flavor, blow off, volume loss
	</p>


	<h3>Data Collecting and Preprocessing</h3>
	<p>The data was captured from a camera through a traditional benchtop microscope. The image was then cropped down to the portion that contains the relavent information. The individual cells then had bounding boxes drawn around them and were classified as alive or dead. Lastly the cells were seperated from the rest of the image.<p>
	<p>
		<img src="/yeast_cell_data/raw_files/20181115_101011.jpg" height="240">
		<img src="bounding_box.png" height="240">
		<img src="tensorflow/test_images/alive278.jpg" height="240">
	</p>

	<h3>Yeast viability and what it is</h3>
	<p>Viability is the ratio of living cells to the total number of cells. This is usually done by a lab technician using a stain like methylene blue, a microscope, and a hemocytomet to count and classify the cells. Detailed instrucition can be found on <a href="https://www.whitelabs.com/beer/cell-counting-viability-testing">WhiteLabs website</a></p>

	<h3>Classification: Alive vs. Dead</h3>
	<h4>Alive Cells</h4>
	<p>
		<img src="tensorflow/test_images/alive60.jpg" height="120">
		<img src="tensorflow/test_images/alive278.jpg" height="120">
		<img src="tensorflow/test_images/alive856.jpg" height="120">
	</p>
	<h4>Dead Cells</h4>
	<p>
		<img src="tensorflow/test_images/dead27.jpg" height="120">
		<img src="tensorflow/test_images/dead62.jpg" height="120">
		<img src="tensorflow/test_images/dead649.jpg" height="120">
	</p>



	<h3>Yeast vitality, lesser known</h3>
	<p>Vitality is a measure of how active a cell or group of cells are. There are two ways common ways this is achived. Firstly is performing a small scale fermentation with the yeast in question. The CO2 off gased is captured and measured. This takes about 24 hours to get results, but in that time the original yeast sample viability and vitality have dropped. The second solution is to use a stain that is not processed homogeniously. For this we use methylene blue again. Methylene blue works by being absorbed into all cells and staining them. Living, helathy cell will reduce the methylene blue to clear, while the dead cells stay blue, as used for viability testing. However this can also be used for Vitality testing in real time as the degree of blue tint can determin the vitality. The issue being that it is dificult to differentiate between subtle changes in saturation of blue.</p>
	<p>By using computer vision not only can we address calculating viability, but also vitality as a computer can differintiate all the distinctive shades of blue</p>
	<p>
		<img src="lievito1.jpg" height="240">
		<img src="lievito2.jpg" height="240">
	</p>
	
	<h2>How it works</h2>

