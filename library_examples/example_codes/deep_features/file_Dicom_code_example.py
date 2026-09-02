import pysera

result = pysera.process_batch(
    image_input=r"C:\Users\AsemaN\Desktop\PySERA_Videos\Data\Multi_Dicom images\MRI\Image\1",
    mask_input=r"C:\Users\AsemaN\Desktop\PySERA_Videos\Data\Multi_Dicom images\MRI\Mask\1.dcm",

    apply_preprocessing=True,            #### enable the preprocessing
    min_roi_volume=1,
    roi_selection_mode="per_region",
    roi_num=20,
    extraction_mode="deep_feature",
    deep_learning_model="densenet121",
    report="all",
    output_path=r"C:\Users\AsemaN\Desktop\PySERA_Videos\results",   
)

print(f"--- success ---: {result['success']}")
print(f"--- output_path ---: {result['output_path']}")
print(f"--- features_extracted -- : {result['features_extracted']}")