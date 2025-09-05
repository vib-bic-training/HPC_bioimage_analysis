# Chapter 6: Bioimaging meets Bioinformatics

##  Theory (Discuss the concept of workflow, reproducibility issue with user)
### 1. Reproducibility and scalability
Given the constant technology evolution, bioimage analysts are confronted complexer, bigger data whose analysis rely on ML and require important computational ressource. 
In addition, interdisciplinar fields such spacial omics or multiomics are gaining importance and tools from Bioinformatics can be used to tackle problems in Bioimaging.
Common problem in Bioinformatics and Bioimaging are: 
- scalability of the analysis
- how to make sure the analysis is reproducible (on different system)
- how to deal with multi-step analysis where each steps use different tool/ programming language.
Those problems can be partially solved using HPC, containers and workflow managers.

### 2. Containers

#### Introduction
A container is way to pack your software so that it is isolated from the external world and can be used independently of the explotation system (unix, windows). 
The advantage of a container is its reproducibility and it is less demanding for the system (check with Bruna). 
There exists plethora of containers but the most important are Docker and Apptainer. 
Interestingly, there exist many avalaible free resource for containers for image analysis (EMBL, dockerhub (https://hub.docker.com/), wavecontainer (https://seqera.io/containers/), github) and BIC can share/help with containers for image analysis. 

#### Small demo on prebuild containers
- How to run cellpose from an available container on dockerhub
```
export APPTAINER_TMPDIR=$VSC_SCRATCH/apptainer_tmp
mkdir -p $APPTAINER_TMPDIR
export APPTAINER_CACHEDIR=$VSC_SCRATCH/apptainer_cache
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



## 3. Workflow managers

A scientific workflow system is a specialized form of a workflow management system designed specifically to compose and execute a series of computational or data manipulation steps, or workflow, in a scientific application (a reformuler). Scientific workflows are common in earth science, astronomy and bioIT.
They enable to link different building blocks (modules and subworkflows) together. Popular workflows managers are Galaxy, Nextflow and Snakemake. The most popular workflows currently are Nextflow and Snakemake. Nextflow is using Groovy (java-based), while Snakemake is using python. 

## 🐍 **Snakemake** vs 🌊 **Nextflow** Comparison

| Aspect | 🐍 **Snakemake** | 🌊 **Nextflow** |
|--------|------------------|------------------|
| **📝 Ease of Use** | ✅ **Easier** <br/>Python-like syntax <br/>Simple rule-based | ❌ **Harder** <br/>Groovy syntax <br/>Complex processes |
| **☁️ Cloud & Scalability** | ⚠️ **Limited** <br/>Basic cloud support <br/>Good for HPC | ✅ **Excellent** <br/>Native cloud integration <br/>Superior scaling |
| **🐳 Container Support** | ✅ **Good** <br/>Docker + Singularity <br/>Conda integration | ✅ **Excellent** <br/>All container types <br/>Seamless integration |
| **🔧 Ecosystem** | ⚠️ **Smaller** <br/>Growing community <br/>Python-focused | ✅ **Rich** <br/>nf-core pipelines <br/>Large bioinformatics community |
| **🚀 Performance** | ✅ **Good** <br/>Efficient execution <br/>Easy debugging | ✅ **Excellent** <br/>Advanced parallelization <br/>Better resume capabilities |

How to choose:


## 🎯 **Quick Decision Guide**

| Choose **🐍 Snakemake** if: | Choose **🌊 Nextflow** if: |
|---------------------------|--------------------------|
| • You know Python | • You need cloud deployment |
| • Simple HPC workflows | • Want ready-made pipelines |
| • Prefer easy debugging | • Need maximum scalability |
| • File-based processing | • Complex data flows |


 
 Here we will give a small demo about nextflow and containers explain where you can find resources. Nevertheless, we highly recommend following VIB nextflow course (https://training.vib.be/all-trainings/reproducible-data-analysis-0).

### Use case 
- Containers and workflow managements for image analysis
-  E.g. Raw Image -> Ome Tiff Image -> Cellpose SAM (3D) -> measurement
- Show some graphic example (with flowchart) and some graphics (our own and nfcore) 
- demonstrate one example with cellpose and with small dataset
- show where the output is and explain how you can run it

### What we are working on and what you would need
- segmentation
- alignment
- denoising
- deconvolution?

