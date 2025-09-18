# Usage

## Cloning the repository

```
cd $VSC_SCRATCH_PROJECTS_BASE/2024_300/yourfolder
git clone https://github.com/vib-bic-training/HPC_bioimage_analysis.git
```

## Building the container

```
cd HPC_bioimage_analysis/scripts
# change the script to build the container
vi build_container_tier1.slurm
sbatch build_container_tier1.slurm
```

## how to run
```
cd HPC_bioimage_analysis/nextflow
# check the configuration file
vi nextflow.config
chmod +x bin/*.py
module load Nextflow
nextflow run main.nf 
```
