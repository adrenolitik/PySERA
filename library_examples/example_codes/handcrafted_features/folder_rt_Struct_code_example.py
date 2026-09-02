import pysera

result = pysera.process_batch(
    image_input=".\Examples\Data\RT-STRUCT\image",
    mask_input=".\Examples\Data\RT-STRUCT\mask",
    output_path="./results",    # Where to save the output result
    num_workers="4",
    enable_parallelism=True,
    categories="gldzm, ngtdm, ngldm",
    dimensions="2d",
)

print(result)