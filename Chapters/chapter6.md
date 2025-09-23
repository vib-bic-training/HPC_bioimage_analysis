# Chapter 6: Bioimaging meets Bioinformatics

##  Theory (Discuss the concept of workflow, reproducibility issue with user)
### 0. Reproducibility and scalability
Given the constant technology evolution, bioimage analysts are confronted complexer, bigger data whose analysis rely on ML and require important computational ressource. 
In addition, interdisciplinar fields such spacial omics or multiomics are gaining importance and tools from Bioinformatics can be used to tackle problems in Bioimaging.
Common problem in Bioinformatics and Bioimaging are: 
- scalability of the analysis
- how to make sure the analysis is reproducible (on different system)
- how to deal with multi-step analysis where each steps use different tool/ programming language.
Those problems can be partially solved using HPC, containers and workflow managers.

## 🐳 **Containers** vs 🏗️ **Modules** vs 🐍 **Conda** Comparison (à modifier)

| Aspect | 🐳 **Containers** | 🏗️ **Modules** | 🐍 **Conda** |
|--------|------------------|------------------|---------------|
| **📦 Reproducibility** | ✅ **Excellent** <br/>Complete system isolation <br/>Same everywhere | ✅ **Very Good** <br/>Version-controlled builds <br/>Dependency tracking | ⚠️ **Moderate** <br/>Environment files <br/>Platform differences |
| **⚡ Performance** | ⚠️ **Moderate** <br/>Container runtime cost <br/>I/O can be slower | ✅ **Native** <br/>Optimized builds <br/>No virtualization overhead | ⚠️ **Moderate** <br/>Direct execution <br/>Minimal overhead |
| **🔧 User experience** | ❌ **Complex** <br/>Requires expertise <br/>Build time intensive | ✅ **Good** <br/>if you have the right version  | ⚠️ **Good**<br/>Nice as long as you don't need GPU|
| **🚀 Portability** | ✅ **Excellent** <br/>Works anywhere <br/>OS independent | ⚠️ **Moderate** <br/>HPC-specific <br/>Architecture dependent | ❌ **Limited**<br/>Cross-platform <br/>Some package conflicts |
| **💾 Resource Usage** | ❌ **Heavy** <br/>Large image sizes <br/>Duplicate dependencies | ⚠️ **Moderate** <br/>Optimized builds <br/>Shared libraries | ✅ **Lightweight** <br/>Small environments <br/>Efficient storage |

### 1. Slurm jobs

Slurm stands for Simple Linux Utility for Resource Management and is a workload manager.
Basically, Slurm takes care of the following task: 
- Manage and allocate cluster resources
- Allocate resources to users for jobs
- Starts and monitors work
- Manages a queue of pending jobs

- Here is an example of a gpu job (where you will select the appropriate partition, amount of cpu, gpus, time and memory, load some env variable of load some modules)

```bash
#!/bin/bash
#SBATCH -A 2024_300
#SBATCH --partition=gpu_rome_a100_40
#SBATCH --nodes="1"
#SBATCH --ntasks-per-node="1"
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=1g
#SBATCH --gpus-per-task=1
#SBATCH --output=cellpose3.out
#SBATCH --error=cellpose3.err
#SBATCH --time=00:30:00

export APPTAINER_TMPDIR=$VSC_SCRATCH_PROJECTS_BASE/2024_300/yourfolder/containers/.apptainer/tmp
export APPTAINER_CACHEDIR=$VSC_SCRATCH_PROJECTS_BASE/2024_300/yourfolder/containers/.apptainer/cache
 
apptainer run --nv cellpose3.sif cellpose --image_path ../training/2024/cellpose/hdab_fat_cells_2d.tif --pretrained_model cyto3 --gpu

```
- to launch a jon ```sbatch  my_job.slurm```
- to cancel a job: ``` scancel jobid```
- to monitor a job: ```slurm_jobinfo 9176837```
- to see the efficiency of a finished jobs: ```sacct -j jobid --format=jobid,jobname,reqcpus,reqmem,averss,maxrss,elapsed,state%20,exitcode --unit=M```
- you can also use job dependency so one job waits for the previous job to be finished(https://docs.vscentrum.be/compute/jobs/job_submission.html#specifying-dependencies)
- or do some parameters search through job arrays: https://docs.vscentrum.be/compute/jobs/job_types.html#job-arrays-and-parameter-exploration



### 2. Containers

#### Introduction
A container is way to pack your software so that it is isolated from the external world and can be used independently of the explotation system (unix, windows). 
The advantage of a container is its reproducibility across different infrastructures. 
There exists plethora of containers but the most important are Docker and Apptainer. 
Interestingly, there exist many avalaible free resource for containers for image analysis (EMBL, dockerhub (https://hub.docker.com/), wavecontainer (https://seqera.io/containers/), github) and BIC can share/help with containers for image analysis. 

#### Small demo on prebuild containers
- How to run cellpose from an available container on dockerhub
```
export APPTAINER_TMPDIR=$VSC_SCRATCH_PROJECTS_BASE/2024_300/yourfolder/apptainer_tmp
mkdir -p $APPTAINER_TMPDIR
export APPTAINER_CACHEDIR=$VSC_SCRATCH_PROJECTS_BASE/2024_300/yourfolderapptainer_cache
mkdir -p $APPTAINER_CACHEDIR
apptainer pull docker://biocontainers/cellpose:3.1.0_cv1
```
- how to see the available option and how to run
```
apptainer exec cellpose_3.1.0_cv1.sif cellpose --help
apptainer run cellpose_3.1.0_cv1.sif cellpose --image_path ../training/2024/cellpose/hdab_fat_cells_2d.tif --pretrained_model cyto3
```
- Exercise: what is the issue with this container?
#### Using complex or customed containers
If you cannot find the container that you need, then you have to build it.
However, learning how to build and maintain containers has a steep learning curve. 
Therefore, we highly recommend to follow the VIB docker and apptainer course (https://training.vib.be/all-trainings/reproducible-data-analysis-0) if you want to know more about this topic. 
```
cd training/2025/containers_gui
apptainer exec cellpose4_cuda121.sif cellpose --help
apptainer run cellpose4_cuda121.sif cellpose --Zstack
```

#### Bonus (out of the scope of this course)
```
# How to build a container
cd $VSC_SCRATCH_PROJECTS_BASE/2024_300/yourfolder
git clone https://github.com/vib-bic-training/HPC_bioimage_analysis
cd HPC_bioimage_analysis
cd scripts
# construct a container
sbatch build_container_tier1.slurm
# run the container in the job
sbatch run_container_tier1.slurm
```
- if you want to know more about those topics, follow (https://training.vib.be/all-trainings/reproducible-data-analysis-0) and/or dedicated HPC training
  
## 3. Workflow managers

A scientific workflow system is a specialized form of a workflow management system designed specifically to compose and execute a series of computational or data manipulation steps, or workflow, for scientific applications. Scientific workflows are common in earth science, astronomy and bioIT.
They enable to link different building blocks (modules and subworkflows) together. Popular workflows managers are Galaxy, Nextflow and Snakemake. The most popular workflows currently are Nextflow and Snakemake. Nextflow is using Groovy (java-based), while Snakemake is using python. 

## Snakemake vs  Nextflow Comparison

| Aspect |  <img src="https://github.com/vib-bic-training/HPC_bioimage_analysis/blob/main/images/snakemake.png?raw=true" width="20"> **Snakemake** |  <img src="https://github.com/vib-bic-training/HPC_bioimage_analysis/blob/main/images/nextflow.png?raw=true" width="20"> **Nextflow** |
|--------|------------------|------------------|
| **📝 Ease of Use** | ✅ **Easier** <br/>Python-like syntax <br/>Simple rule-based | ❌ **Harder** <br/>Groovy syntax <br/>Complex processes |
| **☁️ Cloud & Scalability** | ⚠️ **Limited** <br/>Basic cloud support <br/>Good for HPC | ✅ **Excellent** <br/>Native cloud integration <br/>Superior scaling |
| **🐳 Container Support** | ✅ **Good** <br/>Docker + Singularity <br/>Conda integration | ✅ **Excellent** <br/>All container types <br/>Seamless integration |
| **🔧 Ecosystem** | ⚠️ **Smaller** <br/>Growing community <br/>Python-focused | ✅ **Rich** <br/>nf-core pipelines <br/>Large bioinformatics community |
| **🚀 Performance** | ✅ **Good** <br/>Efficient execution <br/>Easy debugging | ✅ **Excellent** <br/>Advanced parallelization <br/>Better resume capabilities |

How to choose:


## 🎯 **Quick Decision Guide**

| Select <img src="https://github.com/vib-bic-training/HPC_bioimage_analysis/blob/main/images/snakemake.png?raw=true" width="20"> Snakemake** if: | Select <img src="https://github.com/vib-bic-training/HPC_bioimage_analysis/blob/main/images/nextflow.png?raw=true" width="20"> Nextflow** if: |
|---------------------------|--------------------------|
| • You know Python | • You need cloud deployment |
| • Simple HPC workflows | • Want ready-made pipelines |
| • Prefer easy debugging | • Need maximum scalability |
| • File-based processing | • Complex data flows |


- Here we will give a small demo about nextflow and containers explain where you can find resources. Nevertheless, we highly recommend following VIB nextflow course (https://training.vib.be/all-trainings/reproducible-data-analysis-0).

### Use case 
- Containers and workflow managements for image analysis

### 🔧 **Pipeline Overview**

| Step | Input | Process | Output | Tools | GPU |
|------|-------|---------|--------|---------|--------|
| **1** | CZI | 🔄 **Conversion** | OME.TIFF |skimage&bioio|❌|
| **2** | OME.TIFF | 🎯 **Segmentation** | Labels |CellposeSAM|✅|
| **3** | Labels + Raw | 📏 **Measurements** | XLSX |skimage&bioio|❌|
  

- Show some graphic example (with flowchart) and some graphics (our own and nfcore) 
- demonstrate one example with cellpose and with small dataset
- Here is how my pipeline is structured
```bash
tree nextflow/
nextflow
├── bin
│   ├── cellpose_seg_nextflow.py
│   ├── convert_czi2ometiff.py
│   └── metrics.py
├── main.nf
├── modules
│   ├── cellpose
│   │   └── main.nf
│   ├── conversion
│   │   └── main.nf
│   └── metrics
│       └── main.nf
└── nextflow.config
```
- On HPC, there are different way to run it:
 ```bash
# using slurm 
module load Nextflow
nextflow run main.nf
```
- of course running nextflow on different cluster will have an incidence and it will lead to slight change in the configuration file.
- show where the output is and explain how you can run it
```bash
tree results
results/
├── cellpose
│   └── bioimage_analysis_training_dataset_cells.ome_cp_masks.tif
├── converted
│   └── bioimage_analysis_training_dataset_cells.ome.tiff
└── metrics
    └── nuclei_analysis_bioimage_analysis_training_dataset_cells.ome.xlsx
```

### Big advantage of nextflow
Nfcore pipeline and module:
- https://nf-co.re/pipelines
- https://nf-co.re/modules
- https://seqera.io/containers/
  
### What we are working on and what you would need
- segmentation (ilastik, cellpose)
- EM ( alignment)
- EM + LM denoising
- future plan: EM segmentation 
- deconvolution?
- lightsheet?

