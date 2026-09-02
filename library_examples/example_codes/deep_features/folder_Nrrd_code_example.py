import pysera

result = pysera.process_batch(
    image_input="./Examples/Data/NRRD_img",
    mask_input="./Examples/Data/NRRD_mask",
    output_path="./output_results",
    enable_parallelism=True,
    extraction_mode="deep_feature",     # Feature extraction strategy - Choices: 'deep_feature', 'handcrafted_feature'
)

print(f"--- processing_time ---: {result['processing_time']}")
print(f"--- logs ---: {result['logs']}")