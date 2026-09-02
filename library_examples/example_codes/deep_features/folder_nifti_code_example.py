import pysera

result = pysera.process_batch(
    image_input="./Examples/Data/CT",
    mask_input="./Examples/Data/CT-Mask",
    output_path="./results",
    num_workers="4",        # Number of CPU cores engaged with the process
    enable_parallelism=True,    # Enables parallel processing - Default: True
    min_roi_volume=10,
    roi_selection_mode="per_region",
    roi_num=1,
    extraction_mode="deep_feature",
    deep_learning_model="densenet121",
    apply_preprocessing=True,
)

print(result)