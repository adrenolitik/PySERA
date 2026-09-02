import pysera

result = pysera.process_batch(
    image_input="./Examples/Data/image_Multidicom",
    mask_input="./Examples/Data/mask_Multidicom",
    output_path="./results",
    roi_selection_mode="per_region",        # ROI selection strategy - Default: 'per_img'
    extraction_mode="deep_feature",
)


print(f"Success: {result['success']}")
print(f"Output path: {result['output_path']}")