import numpy as np
import SimpleITK as sitk
import pysera

# Load DICOM series from directory
image_reader = sitk.ImageSeriesReader()
dicom_names = image_reader.GetGDCMSeriesFileNames(
    r"image_path"
)
image_reader.SetFileNames(dicom_names)
image_sitk = image_reader.Execute()
image_array = sitk.GetArrayFromImage(image_sitk).astype(np.float32)

# Load DICOM mask file
mask_sitk = sitk.ReadImage(r"mask_path")
mask_array = sitk.GetArrayFromImage(mask_sitk).astype(np.float32)

result = pysera.process_batch(
    image_input=image_array,
    mask_input=mask_array,
    output_path=r".\results",
    roi_selection_mode="per_region",        # ROI selection strategy - Default: 'per_img'
    extraction_mode="deep_feature",
)


print(f"Success: {result['success']}")
print(f"Output path: {result['output_path']}")