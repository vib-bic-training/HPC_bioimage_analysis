#!/bin/bash
#SBATCH --job-name=build-apptainer
#SBATCH --ntasks=1
#SBATCH --partition=gpu_rome_a100_40
#SBATCH --cpus-per-task=4
#SBATCH --gpus-per-node=1
#SBATCH --time=00:30:00
#SBATCH --reservation=vib_bioimaging
#SBATCH --output=build1_apptainer.stdout
#SBATCH --error=build1_apptainer.stderr
#SBATCH --account=2024_300

# change the path
export APPTAINER_CACHEDIR=/tmp/.apptainer/cache
mkdir -p $APPTAINER_CACHEDIR
export APPTAINER_TMPDIR=/tmp/.apptainer/tmp
mkdir -p $APPTAINER_TMPDIR
apptainer build metrics.sif metrics.def
