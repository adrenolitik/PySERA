import pysera

result = pysera.process_batch(
    image_input=r"C:\Users\AsemaN\Desktop\PySERA_Videos\Data\Multi_Dicom images\MRI\Image",
    mask_input=r"C:\Users\AsemaN\Desktop\PySERA_Videos\Data\Multi_Dicom images\MRI\Mask",
    categories="all",       # Category of features to extract - Example: 'morph,glcm,glrlm,glszm'
    dimensions="2_5d",      # Determines dimension for feature extraction - Example: '1st,2_5d,3d'
    roi_selection_mode="per_region",
    min_roi_volume=50,
    output_path=r"C:\Users\AsemaN\Desktop\PySERA_Videos\results", 
)

print(result) 