import pysera

result = pysera.process_batch(
    image_input="./Examples/Data/dicom/image",
    mask_input="./Examples/Data/dicom/mask",
    output_path="./results",
    num_workers="auto",
    feature_value_mode="APPROXIMATE_VALUE",     # Using 'APPROXIMATE_VALUE' to handle NaN values - Default: 'REAL_VALUE'
    aggregation_lesion=True,
    extraction_mode="handcrafted_feature",
    temporary_files_path="./tmp",       # Path to a temporary file to handle large files
)

print(f"processing_time: {result['processing_time']}")