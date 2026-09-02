import numpy as np
import SimpleITK as sitk
import pysera

# Load DICOM series from directory  as NumPy arrays   
image_reader = sitk.ImageSeriesReader()
dicom_names = image_reader.GetGDCMSeriesFileNames(
    r"C:\Users\AsemaN\Desktop\PySERA_Videos\Data\Multi_Dicom images\MRI\Image\1"  
)
image_reader.SetFileNames(dicom_names)
image_sitk = image_reader.Execute()
image_array = sitk.GetArrayFromImage(image_sitk).astype(np.float32)

# Load DICOM mask file  as NumPy arrays
mask_sitk = sitk.ReadImage(r"C:\Users\AsemaN\Desktop\PySERA_Videos\Data\Multi_Dicom images\MRI\Mask\1.dcm")
mask_array = sitk.GetArrayFromImage(mask_sitk).astype(np.float32)

result = pysera.process_batch( 
    image_input=image_array,
    mask_input=mask_array,
    output_path=r"C:\Users\AsemaN\Desktop\PySERA_Videos\results",
    categories="all",       # Category of features to extract - Example: 'morph,glcm,glrlm,glszm'
    dimensions="2_5d",      # Determines dimension for feature extraction - Example: '1st,2_5d,3d'
    roi_selection_mode="per_region",
    min_roi_volume=50,
)  

print(result)