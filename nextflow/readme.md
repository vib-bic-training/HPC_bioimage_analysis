# Usage

## Cloning the repository

```
cd $VSC_SCRATCH_PROJECTS_BASE/2024_300/yourfolder
git clone https://github.com/vib-bic-training/HPC_bioimage_analysis/tree/main
```

## Building the container

```
cd HPC_bioimage_analysis/scripts
# change the script to build the container
vi build_container_tier1.slurm
sbatch build_container_tier1.slurm
# change the script to run the container
sbatch run_container_tier1.slurm
```

## how to run
```
cd HPC_bioimage_analysis/nextflow
# adapt the configuration file
vi nextflow.config
chmod +x bin/*.py
module load Nextflow
nextflow run main.nf -profile vsc_ugent
```
