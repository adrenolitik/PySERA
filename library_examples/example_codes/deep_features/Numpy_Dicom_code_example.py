import numpy as np
import pydicom
import pysera

# Load DICOM file using pydicom
dicom_image = pydicom.dcmread(r"image_path")
image_array = dicom_image.pixel_array.astype(np.float32)

dicom_mask = pydicom.dcmread(r"mask_path")
mask_array = dicom_mask.pixel_array.astype(np.float32)

result = pysera.process_batch(
    image_input=image_array,
    mask_input=mask_array,
    output_path=r".\results",
    apply_preprocessing=True,       # Apply preprocessing or use raw masks - default: False
    enable_parallelism=True,
    min_roi_volume=1,
    roi_selection_mode="per_region",
    roi_num=20,
    extraction_mode="deep_feature",
    deep_learning_model="densenet121",
    report="all",
)

print(f"--- success ---: {result['success']}")
print(f"--- output_path ---: {result['output_path']}")
print(f"--- features_extracted -- : {result['features_extracted']}")