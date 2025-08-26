<!--

author:   Pavie Benjamin, Tatiana Woller
email:    benjamin.pavie@vib.be, tatiana.woller@vib.be
version:  2.0.0
language: en
narrator: UK English Female

icon:     https://vib.be/sites/vib.sites.vib.be/files/logo_VIB_noTagline.svg

comment:  This document shall provide an entire compendium and course on the
          development of Open-courSes with [LiaScript](https://LiaScript.github.io).
          As the language and the systems grows, also this document will be updated.
          Feel free to fork or copy it, translations are very welcome...

script:   https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.js
          https://felixhao28.github.io/JSCPP/dist/JSCPP.es5.min.js

link:     https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.css
link:     https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css
link:     https://raw.githubusercontent.com/vibbits/material-liascript/master/img/org.css
link:     https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css
link:     https://fonts.googleapis.com/css2?family=Saira+Condensed:wght@300&display=swap
link:     https://fonts.googleapis.com/css2?family=Open+Sans&display=swap
link:     https://raw.githubusercontent.com/vibbits/material-liascript/master/vib-styles.css

tutor:    VIB
edition:  1st 
workshop_name:     Bioimaging data analysis on HPC
workshop_edition: 1st

@JSONLD
<script run-once>
  let json = @0 

  const script = document.createElement('script');
  script.type = 'application/ld+json';
  script.text = JSON.stringify(json);

  document.head.appendChild(script);

  // this is only needed to prevent and output,
  // as long as the result of a script is undefined,
  // it is not shown or rendered within LiaScript
  console.debug("added json to head")
</script>
@end

orcid:    [@0](@1)<!--class="orcid-logo-for-author-list"
-->

# Chapter x: Installed software

## General linux command

From a terminal (or from a Jupyter notebook, add a `!` to use this command)

- See loaded modules
```
ml
module list
```
- See available modules 
```
module avail
```
- Search for a module X
```
module av |& grep -i X
```
- Search for a module X and get details
```
module spider X
```
- Load a module X
```
module load x
```
- Unload a module X
```
module unload x
```
- Swap a module Y to X
```
module swap Y  X
```
- Remove all loaded modules except the cluster one
```
module purge
```
⚠️ Do not load modules built with intel and foss toolchains

🗎 https://docs.vscentrum.be/software/software_stack.html#using-the-module-system


## Modules for bioimage analysis 
1. [Napari](https://github.com/napari/napari): Napari/0.4.15-foss-2021b, napari/0.4.18-foss-2022a, napari/0.4.18-foss-2022a,  napari/0.4.18-foss-2023a
2. [Napari empanada](https://empanada.readthedocs.io/en/latest/): empanada-napari/1.1.0-foss-2023a
3. [Napari devbio](https://github.com/haesleinhuepf/devbio-napari): devbio-napari/0.10.1-foss-2022a-CUDA-11.7.0, devbio-napari/0.10.1-foss-2022a, empanada-napari/1.1.0-foss-2023a
4. [Napari microsam](https://github.com/computational-cell-analytics/micro-sam):micro-sam/1.0.1-foss-2023a
5. [napari ilastik](): ilastik-napari/0.2.4-foss-2023a
6. [Napari denoiseg]():napari-denoiseg/0.0.1-foss-2023a
7. [n2v](https://github.com/juglab/n2v):n2v/0.3.2-foss-2022a-CUDA-11.7.0, n2v/0.3.2-foss-2022a, n2v/0.3.3-foss-2023a
8. [Cellpose](https://github.com/MouseLand/cellpose): Cellpose/2.2.2-foss-2022a or Cellpose/2.2.2-foss-2022a-CUDA-11.7.0
9. Omnipose:  Omnipose/0.4.4-foss-2022a-CUDA-11.7.0 or  Omnipose/0.4.4-foss-2022a
10. [stardist](https://github.com/stardist/stardist): stardist/0.8.3-foss-2021b-CUDA-11.4.1 or stardist/0.8.3-foss-2021b
11. [AICSImageIO](https://github.com/AllenCellModeling/aicsimageio) : AICSImageIO/4.14.0-foss-2022a
12. Tiffile: tifffile/2023.7.18, tifffile/2024.6.18
13. Monai: MONAI/1.0.1-foss-2022a
14. QuPath: QuPath/0.5.0-GCCcore-12.3.0-Java-17
15. Cellprofiler: CellProfiler/4.2.4-foss-2021a
16. Fiji: Fiji/2.9.0-Java-1.8
17. Zarr:  zarr/2.17.1-foss-2023a, zarr/2.13.3-foss-2022a, zarr/2.13.3-foss-2021b
18. Empanada: empanada-dl-0.1.7


## General libraries 
1. Scikit-learn:
   - scikit-learn/1.1.2-foss-2022a
   - scikit-learn/1.0.1-foss-2021b
   - scikit-learn/1.4.0-gfbf-2023b
   - scikit-learn/1.4.2-gfbf-2023a
2. Scikit-image:
   - scikit-image/0.19.3-foss-2022a
   - scikit-image/0.19.1-foss-2021b
   - scikit-image/0.22.0-foss-2023a
3. scipy:
   - SciPy-bundle/2022.05-foss-2022a
   - SciPy-bundle/2021.10-foss-2021b
   - SciPy-bundle/2023.02-gfbf-2022b
   - SciPy-bundle/2023.07-gfbf-2023a
   - SciPy-bundle/2023.11-gfbf-2023b
   - SciPy-bundle/2024.05-gfbf-2024a
4. seaborn:
   - Seaborn/0.11.2-foss-2021b
   - Seaborn/0.12.1-foss-2022a
   - Seaborn/0.13.2-gfbf-2023a
   - Seaborn/0.13.2-gfbf-2023b
5. tensorflow:
   - TensorFlow/2.7.1-foss-2021b-CUDA-11.4.1
   - TensorFlow/2.7.1-foss-2021b
   - TensorFlow/2.15.1-foss-2023a-CUDA-12.1.1
     
_Nota bene_: There exists many flavours of tensorflow: estimator, probability, etc ...
- To see them all use: ```module spider tensorflow```
6. pytorch:  PyTorch/2.1.2-foss-2023a-CUDA-12.1.1
-_Nota bene_:there are many flavours of pytorch: geometric, lightning, ignite,
- to see them all: ```module spider pytorch```
7. Jupyter notebook: 
- JupyterNotebook/6.4.0-GCCcore-11.3.0-IPython-8.5.0
- JupyterNotebook/7.0.2-GCCcore-12.3.0
- JupyterNotebook/7.0.3-GCCcore-12.2.0
- JupyterNotebook/7.2.0-GCCcore-13.2.0
8. Jupyterlab:
- JupyterLab/4.2.0-GCCcore-13.2.0
- JupyterLab/4.0.5-GCCcore-12.3.0
- JupyterLab/4.0.3-GCCcore-12.2.0
- JupyterLab/3.5.0-GCCcore-11.3.0
9. Matplotlib:
- matplotlib/3.5.2-foss-2022a
- matplotlib/3.4.3-intel-2021
- matplotlib/3.7.2-gfbf-2023a
- matplotlib/3.8.2-gfbf-2023b
- matplotlib/3.9.2-gfbf-2024a
10. Python: type ```module avail  Python/```
   
- _nota bene_: R and matlab  modules are also available
- reference: https://docs.hpc.ugent.be/Linux/python/

[Chapters List](https://liascript.github.io/course/?https://raw.githubusercontent.com/vib-bic-training/2024_Bioimaging_data_analysis_on_HPC/refs/heads/main/README.md#5) | [next chapter](https://liascript.github.io/course/?https://raw.githubusercontent.com/vib-bic-training/2024_Bioimaging_data_analysis_on_HPC/refs/heads/main/Chapters/Chapter02.md)




