#!/bin/bash
#SBATCH --job-name=build-apptainer
#SBATCH --ntasks=1
#SBATCH --partition=debug_rome
#SBATCH --cpus-per-task=4
#SBATCH --gpus-per-node=1
#SBATCH --time=00:30:00
#SBATCH --output=build1_apptainer.stdout
#SBATCH --error=build1_apptainer.stderr
#SBATCH --account=2024_300

cd /tmp
chmod a+rwx .
cp $VSC_SCRATCH_PROJECTS_BASE/2024_300/twoller/containers/cellpose3.def /tmp/cellpose3.def


export APPTAINER_CACHEDIR=/tmp/.apptainer/cache
mkdir -p $APPTAINER_CACHEDIR
export APPTAINER_TMPDIR=/tmp/.apptainer/tmp
mkdir -p $APPTAINER_TMPDIR
apptainer build --nv cellpose3.sif cellpose3.def

mv /tmp/cellpose3.sif $VSC_SCRATCH_PROJECTS_BASE/2024_300/yourfolder/containers/
