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
                "type": "filters.outlier",
                "method": "statistical",
                "mean_k": 8,
                "multiplier": 3
            },
            {
                "type": "filters.assign",
                "value": [
                    "Classification = 0 WHERE Classification == 7"
                ]
            },
            {
                "type": "filters.decimation",
                "step": 10
            },
            {
                "type": "writers.las",
                "filename": "%s"
            }
        ]
    }
    """ % (input_filename.replace("\\", "/"), output_filename.replace("\\", "/"))
    return pipeline_json

def run_pipeline(pipeline_json):
    pipeline = pdal.Pipeline(pipeline_json)
    pipeline.execute()

# Input and output filenames
input_filename = r'path\to\pdalpy\data\classified_points_final.las'
output_filename = r'path\to\pdalpy\data\thinned_points.laz'

# Create the pipeline
pipeline_json = create_pipeline(input_filename, output_filename)

# Run the pipeline
run_pipeline(pipeline_json)
