import pdal

def create_pipeline(input_filename, output_filename):
    pipeline_json = """
    {
        "pipeline": [
            {
                "type": "readers.las",
                "filename": "%s"
            },
            {
                "type": "filters.assign",
                "assignment": "Classification[:]=0"
            },
            {
                "type": "filters.smrf",
                "scalar": 1.2,
                "slope": 0.2,
                "threshold": 0.45,
                "window": 16,
                "cell": 1.0
            },
            {
                "type": "filters.hag_nn",
                "count": 10
            },
            {
                "type": "filters.assign",
                "value": [
                    "Classification = 2 WHERE HeightAboveGround <= 1",
                    "Classification = 5 WHERE HeightAboveGround > 1"
                ]
            },
            {
                "type": "writers.las",
                "filename": "%s"
            }
        ]
    }
    """ % (input_filename.replace("\\", "\\\\"), output_filename.replace("\\", "\\\\"))
    return pipeline_json

def run_pipeline(pipeline_json):
    pipeline = pdal.Pipeline(pipeline_json)
    pipeline.execute()

# Input and output filenames
input_filename = r'path\to\pdalpy\data\NEONDSSampleLiDARPointCloud.las'
output_filename = r'path\to\pdalpy\data\classified_points_final_hag.laz'

# Create the pipeline
pipeline_json = create_pipeline(input_filename, output_filename)

# Run the pipeline
run_pipeline(pipeline_json)
