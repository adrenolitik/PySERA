import numpy as np
import nrrd
import pysera

# Load NRRD files using pynrrd
image_array, image_header = nrrd.read(r"image_path")
mask_array, mask_header = nrrd.read(r"mask_path")

# Convert to float32 (PySERA expects float32 typically)
image_array = image_array.astype(np.float32)
mask_array = mask_array.astype(np.float32)

result = pysera.process_batch(
    image_input=image_array,
    mask_input=mask_array,
    output_path=r".\results",
    enable_parallelism=True,
    extraction_mode="deep_feature",     # Feature extraction strategy - Choices: 'deep_feature', 'handcrafted_feature'
)

print(f"--- processing_time ---: {result['processing_time']}")
print(f"--- logs ---: {result['logs']}")