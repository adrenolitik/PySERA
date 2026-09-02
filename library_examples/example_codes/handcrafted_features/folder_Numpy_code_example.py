import pysera

imgs = ".\Examples\Data\img_np"
masks = ".\Examples\Data\mask_np"

result = pysera.process_batch(
    image_input=imgs,
    mask_input=masks,
    output_path="./results",
)


print(f"Success: {result['success']}")
print(f"Output path: {result['output_path']}")