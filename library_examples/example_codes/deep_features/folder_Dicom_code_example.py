import pysera

result = pysera.process_batch(
    image_input="./Examples/Data/dicom/image",
    mask_input="./Examples/Data/dicom/mask",
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