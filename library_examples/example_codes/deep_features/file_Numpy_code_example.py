import pysera

img = "image_path"
mask = "mask_path"

result = pysera.process_batch(
    image_input=img,
    mask_input=mask,
    output_path="./results",
    apply_preprocessing=False,
    min_roi_volume=5,
    roi_selection_mode="per_img",
    roi_num=12,
    extraction_mode="deep_feature",
    deep_learning_model="vgg16",

    report="all",                #### report all warnings, errors, information
)

print(result)