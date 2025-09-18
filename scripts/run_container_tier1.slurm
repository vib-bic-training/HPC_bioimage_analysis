#!/bin/bash
#SBATCH -A 2024_300
#SBATCH --partition=gpu_rome_a100_40
#SBATCH --nodes="1"
#SBATCH --reservation=vib_bioimaging
#SBATCH --ntasks-per-node="1"
#SBATCH --cpus-per-task=8
#SBATCH --gpus-per-task=1
#SBATCH --output=cellpose4.out
#SBATCH --error=cellpose4.err
#SBATCH --time=00:30:00

# change path
export APPTAINER_TMPDIR=$VSC_SCRATCH_PROJECTS_BASE/2024_300/yourfolder/containers/.apptainer/tmp
export APPTAINER_CACHEDIR=$VSC_SCRATCH_PROJECTS_BASE/2024_300/yourfolder/containers/.apptainer/cache
 
apptainer run --nv $VSC_SCRATCH_PROJECTS_BASE/2024_300/training/2025/containers_gui/cellpose4_cuda121.sif cellpose --Zstack --do_3D --diameter 60  --use_gpu --save_tif --image_path $VSC_SCRATCH_PROJECTS_BASE/2024_300/training/2025/data/cellpose/hela_prolongdiamond_dapi_tubulin-af488_mitochondria-af568_40x_s02_3D.ome.tiff --verbose
