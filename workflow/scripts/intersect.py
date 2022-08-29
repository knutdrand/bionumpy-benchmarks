import bionumpy as bnp
from bionumpy.intervals import intersect

out_f = bnp.open(snakemake.output[0], "w")
a = bnp.open(snakemake.input[0])
b = bnp.open(snakemake.input[1], mode="chromosome_stream")
for chromosome, result in intersect(a, b):
    out_f.write(result)
out_f.close()
