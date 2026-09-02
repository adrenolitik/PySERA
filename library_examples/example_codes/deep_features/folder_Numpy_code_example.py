import pysera

result = pysera.process_batch(
    image_input=".\Examples\Data\img_np",
    mask_input=".\Examples\Data\mask_np",
    output_path="./results",
    num_workers="6",
    apply_preprocessing=False,
    enable_parallelism=True,
    min_roi_volume=5,       # Discards RoIs with number of voxels below this threshold
    roi_selection_mode="per_img",
    roi_num=12,         # Number of ROIs to process
    extraction_mode="deep_feature",
    deep_learning_model="vgg16",
    report="all",
)

print(result)