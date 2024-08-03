pdal_deli_1_1_3.py pipeline provides approach to processing LiDAR data, from initial classification
reset through conditional reclassification based on ground and height analysis.
General Structure and Functionality
• readers.las: This stage initializes reading from a LAS file. The "filename"
parameter specifies the path to the input LAS file,
• filters.assign: This filter is used to initially set all points' classifications to 0. The
"assignment" directive Classification[:]=0 applies this classification universally
across all points, effectively resetting any pre-existing classifications.
• filters.smrf: Simplified Morphological Filter (SMRF) is used to identify ground
points from non-ground points based on their geometric features. Parameters like
"scalar", "slope", "threshold", "window", and "cell" are configured to tailor the
filter's sensitivity and accuracy to the specifics of the input data.
• filters.hag_nn: The Height Above Ground Nearest Neighbor filter calculates
each point's height relative to the nearest ground points. This is particularly
useful for applications that require understanding the vertical structure of the
point cloud, such as vegetation analysis or building extraction. The "count"
parameter specifies how many nearest neighbors to consider when calculating
the average ground level.
• Another filters.assign: This time, it uses the "value" parameter to conditionally
reclassify points based on their calculated Height Above Ground
(HeightAboveGround). Points are classified as 2 if they are 1 meter or less above
ground, and as 5 if they are more than 1 m above ground. This step is crucial for
differentiating between low vegetation or minor terrain undulations and objects
that significantly protrude from the ground, like trees or structures.
• writers.las: This stage writes the processed and reclassified point cloud to an
output LAZ file. The "filename" parameter specifies the path to the output file.
• run_pipeline: This function is defined to take the JSON string that defines the
pipeline, convert it into a PDAL pipeline object, and execute it.


pdal_deli_1_1_4 script process a classified point cloud (modified output from first pipline in .las
format) by removing noise specifically classified as noise (class 7) and thinning the data
to manage its density.
General Structure and Functionality
• LAS File Reader (readers.las): Loads the LAS file containing the point cloud
data.
• filename specifies the path to the LAS file to be processed.
Noise Removal:
• (filters.outlier): Uses a statistical approach to identify and remove outliers based
on the distribution of nearest neighbor distances.
• mean_k: The number of nearest neighbors to consider (set to 8), which
influences the calculation of mean distance and standard deviation.
• multiplier: Determines the threshold for classifying points as outliers, set to 3
times the standard deviation.
Reclassification of Noise Points (filters.assign):
• Reclassifies points previously identified as noise (class 7) to unclassified (class
0), making them neutral in subsequent analyses.
• Uses a conditional statement to change the classification of noise points.
Data Thinning (filters.decimation):
• Reduces the overall number of points in the dataset to decrease processing load
and improve manageability.
• Retains every tenth point (step = 10), effectively decimating the dataset and
reducing its density by approximately 90%.
LAS File Writer (writers.las):
• Saves the processed point cloud to a new LAZ file.
• filename sets the destination for the output file, reflecting the modifications made
by the pipeline.
Execution Function (run_pipeline):
• A function that takes the defined JSON pipeline --> PDAL Pipeline object, and
executes the processing steps.


Link to pdal documentation: https://pdal.io/en/2.7-maintenance/about.html
