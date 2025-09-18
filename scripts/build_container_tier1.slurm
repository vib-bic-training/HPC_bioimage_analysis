#!/bin/bash
#SBATCH --job-name=build-apptainer
#SBATCH --ntasks=1
#SBATCH --partition=gpu_rome_a100_40
#SBATCH --cpus-per-task=4
#SBATCH --gpus-per-node=1
#SBATCH --time=00:30:00
#SBATCH --output=build1_apptainer.stdout
#SBATCH --error=build1_apptainer.stderr
#SBATCH --account=2024_300

cd /tmp
chmod a+rwx .
# change the path
cp $VSC_SCRATCH_PROJECTS_BASE/2024_300/yourfolder/HPC_bioimage_analysis/cellpose4.def /tmp/cellpose4.def


export APPTAINER_CACHEDIR=/tmp/.apptainer/cache
mkdir -p $APPTAINER_CACHEDIR
export APPTAINER_TMPDIR=/tmp/.apptainer/tmp
mkdir -p $APPTAINER_TMPDIR
apptainer build --nv cellpose4.sif cellpose4.def

# change the path
mv /tmp/cellpose3.sif $VSC_SCRATCH_PROJECTS_BASE/2024_300/yourfolder/HPC_bioimage_analysis/
