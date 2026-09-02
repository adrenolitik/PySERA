import numpy as np
import SimpleITK as sitk
from rt_utils import RTStructBuilder
import pysera

# Load image as NumPy array
reader = sitk.ImageSeriesReader()
reader.SetFileNames(reader.GetGDCMSeriesFileNames(r"image_path"))
image_array = sitk.GetArrayFromImage(reader.Execute()).astype(np.float32)

# Load RT-STRUCT as NumPy array mask
rt_struct = RTStructBuilder.create_from(
    dicom_series_path=r"image_path",
    rt_struct_path=r"mask_path"
)
mask_array = rt_struct.get_roi_mask_by_name(rt_struct.get_roi_names()[0]).astype(np.float32)
mask_array = np.transpose(mask_array, (2, 1, 0))  # Adjust dimensions if needed

# Process the image and mask directly from memory
result = pysera.process_batch(
    image_input=image_array,
    mask_input=mask_array,
    output_path=r".\results",
    roi_num=5,
    extraction_mode="deep_feature",
    deep_learning_model="resnet50",
    aggregation_lesion=True,
)

print(f"Success: {result['success']}")
print(f"Processing time: {result['processing_time']:.2f} seconds")