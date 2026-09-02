import pysera

img = "image_path"
mask = "mask_path"

result = pysera.process_batch(
    image_input=img,
    mask_input=mask,
    output_path="./results",
    categories="morph, glcm, glrlm",
    dimensions="1st, 2_5d, 3d",
)


print(f"Success: {result['success']}")
print(f"Output path: {result['output_path']}")