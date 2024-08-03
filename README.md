# PDAL Pipeline Documentation

## PDAL Pipeline `pdal_deli_1_1_3.py`

This pipeline provides an approach to processing LiDAR data, from initial classification reset through conditional reclassification based on ground and height analysis.

### General Structure and Functionality

- **readers.las**:
  - Initializes reading from a LAS file.
  - `filename`: Specifies the path to the input LAS file.

- **filters.assign**:
  - This filter is used to initially set all points' classifications to 0.
  - `assignment` directive: `Classification[:]=0` applies this classification universally across all points, effectively resetting any pre-existing classifications.

- **filters.smrf** (Simplified Morphological Filter):
  - Used to identify ground points from non-ground points based on their geometric features.
  - Parameters: `scalar`, `slope`, `threshold`, `window`, `cell` are configured to tailor the filter's sensitivity and accuracy.

- **filters.hag_nn** (Height Above Ground Nearest Neighbor):
  - Calculates each point's height relative to the nearest ground points.
  - `count`: Specifies how many nearest neighbors to consider.

- **Another filters.assign**:
  - Uses the `value` parameter to conditionally reclassify points based on their calculated Height Above Ground (HeightAboveGround).
  - Points are classified as 2 if they are 1 meter or less above ground, and as 5 if they are more than 1 m above ground.

- **writers.las**:
  - Writes the processed and reclassified point cloud to an output LAZ file.
  - `filename`: Specifies the path to the output file.

- **run_pipeline**:
  - Takes the JSON string that defines the pipeline, converts it into a PDAL pipeline object, and executes it.

## PDAL Pipeline `pdal_deli_1_1_4.py`

This script processes a classified point cloud (modified output from the first pipeline in .las format) by removing noise specifically classified as noise (class 7) and thinning the data to manage its density.

### General Structure and Functionality

- **LAS File Reader (readers.las)**:
  - Loads the LAS file containing the point cloud data.
  - `filename`: Specifies the path to the LAS file to be processed.

- **Noise Removal (filters.outlier)**:
  - Uses a statistical approach to identify and remove outliers based on the distribution of nearest neighbor distances.
  - `mean_k`: Number of nearest neighbors to consider (set to 8), which influences the calculation of mean distance and standard deviation.
  - `multiplier`: Determines the threshold for classifying points as outliers, set to 3 times the standard deviation.

- **Reclassification of Noise Points (filters.assign)**:
  - Reclassifies points previously identified as noise (class 7) to unclassified (class 0).
  - Uses a conditional statement to change the classification of noise points.

- **Data Thinning (filters.decimation)**:
  - Reduces the overall number of points in the dataset to decrease processing load and improve manageability.
  - Retains every tenth point (step = 10), effectively decimating the dataset.

- **LAS File Writer (writers.las)**:
  - Saves the processed point cloud to a new LAZ file.
  - `filename`: Sets the destination for the output file.

- **Execution Function (run_pipeline)**:
  - A function that takes the defined JSON pipeline, converts it into a PDAL pipeline object, and executes the processing steps.

[PDAL Documentation](https://pdal.io/en/2.7-maintenance/about.html)
