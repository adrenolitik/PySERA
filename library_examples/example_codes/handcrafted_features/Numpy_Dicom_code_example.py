import numpy as np
import pydicom
import pysera

# Load DICOM file using pydicom  as NumPy arrays
dicom_image = pydicom.dcmread(r"image_path")
image_array = dicom_image.pixel_array.astype(np.float32)

dicom_mask = pydicom.dcmread(r"mask_path")
mask_array = dicom_mask.pixel_array.astype(np.float32)

result = pysera.process_batch(
    image_input=image_array,
    mask_input=mask_array,
    output_path=r".\results",
    num_workers="auto",
    feature_value_mode="APPROXIMATE_VALUE",     # Using 'APPROXIMATE_VALUE' to handle NaN values - Default: 'REAL_VALUE'
    aggregation_lesion=True,
    extraction_mode="handcrafted_feature",
    temporary_files_path="./tmp",       # Path to a temporary file to handle large files
)

print(f"processing_time: {result['processing_time']}") 