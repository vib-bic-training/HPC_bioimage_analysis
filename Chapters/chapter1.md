<!--

author:   Tatiana Woller, Bruna Piereck, Alexander Botzki
email:    trainingandconferences@vib.be
version:  1.0.0
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

@orcid: [@0](@1)<!--class="orcid-logo-for-author-list"-->

# Chapter 1: Infrastructure

## What is a High-Performance Computing system ?

A HPC brings together several technologies such as computer architecture, algorithms, programs and electronics, and system software to solve advanced problems effectively and quickly. A HPC uses clusters of powerful processors, working in parallel, to process massive multi-dimensional datasets (big data) and solve complex problems at extremely high speeds. HPC systems typically perform at speeds more than one million times faster than the fastest commodity desktop, laptop or server systems. [https://www.ibm.com/topics/hpc].

Among the technologies intergated in a HPC system it can include

**High-end compute nodes:** multicore processors.

**Fast interconnect:** multiple processor cores work together through parallel processing. Fast connections between the nodes are necessary to make quick data exchange possible.

**Parallel shared filesystem:** the compute nodes are connected to a shared filesystem for storing input data, temporary data, and final calculation results.

**High-memory nodes:** some nodes are equipped with lots of RAM memory, mitigating low disk reads impacting analysis that generate large amounts of intermediary results.

**GPU (Graphical processing units) nodes:** are specialized processors, ideally suited for higly demanding data processing tasks.


## Infrastructure

The european model for HPC classifies that different offers in HPC resource and accessibility in different levels called **Tiers**.

_ 

<img src="../images/tierEuropeanHPCsytem.svg" width="500"/>

_ 

* **Tier-0** clusters are ***Very large*** computing infrastructure available at EU level, for example [PRACE association](https://prace-ri.eu/prace-association/) (Partnership for advanced computing in Europe) has [6 partners](https://prace-ri.eu/prace-archive/infrastructure-support/prace-hpc-infrastructure/) offering a Tier-0 cluster. Belgium is not hosting a Tier-0 but is one of ~25 member in PRACE.

* **Tier-1** clusters are clusters with services at the level of a region/country because it exceeds the capacity of an institution in terms of needs/costs. For example in the [VSC (Vlaams supercomputer centrum)](https://www.vscentrum.be/compute) there is [Hortense](https://www.vscentrum.be/compute), the Tier-1 computer cluster hosted by UGent university 

* **Tier-2** clusters are available at research institutions level. There are [4 Tier-2 cluster in flandres](https://docs.vscentrum.be/hardware-tier2.html#), hosted bu the universities UAntwerp, VUB, UGent and KULeuven.

* **Tier-3** is representing your personal computer, can be a desktop or a laptop. But is mainly for personal use and has limited resources.


>> _
>>
>> In this course we will detail more the resources of UGent, KULeuven and VIB instances.
>>
>> However all along we will try to explain the building blocks allowing you easily understand and adapt to other HPC instances.
>>
>> _

## Storage and Computer Nodes systems

A HPC needs different types of storage to maintain the efficience of its vast and complex infrastructure. Each instace will possibly name them differently, but they have defined purposes that you need to take in account when using their environmet. On top of the filesystem, each node will have different computational powers, therefore, depending on your needs, you can choose the one that most suits you.

It means that the files and storage systems in place **will vary**. Knowing this what storages, their purpose and maintanance will be important to understand ***how*** and ***where*** to keep, analyze and backup your data. Additionlly, as you probably already guessed, there is a difference if we are talking about personal use and project wise. Specific projects might request specific resources and will define who can access it.

Generally is good to keep in mind that when you connect to the HPC, the area you start at is like the hall of a house, you should not keep too many things there or do tasks in this location. You will also have a long-term storage, where you can keep your data, but also not where your tasks will be done. Last you will have a temporary large storage place that can be access when using your tasks


<!-- style="color: #7CA1CC;" --> \** Storage space for a group of users (Virtual Organisation or VO for short) in VSC can be increased significantly on request, check for [more information](https://docs.vscentrum.be/gent/tier1_hortense.html#system-specific-aspects) if you need.

## UGent TIER 1
<!-- style="color: magenta" --> VO = virtual organization

If for your training session you are using the [UGent section]((https://docs.vscentrum.be/gent/tier2_hardware.html) or Tier1 of the [Flemish Supercomputing Center](https://www.vscentrum.be/), it's very likely that you will be using the GPU cluster and debug cluster through the. As you can imagine this is not the only cluster you can use, but for trai is good to have an interactive session in order to understand how it is working.

It means that the files and storage systems in place **will vary**. Knowing this details will be important to understand ***how*** and ***where*** to keep , analyze and backup your data.

As you probably already guessed, there is a difference if we are talking about personal use and project wise. Specific projects might request specific resources and will define who can access it.


| Tier  | Login (vscnumber) | Personal storage space | VO Storage Space |  VO Project space |
| ------------- | ------------- | ------------- | ------------- | ------------- |
|Tier 1 | tier1.hpc.ugent.be |yes|yes|yes|


| Cluster name  | Memory (GiB) | Disk space (GB) SSD  |  GPU | GPU memory (GiB)|
| --- | --- | --- | --- | --- |
| cpu_rome | 256 | 480 | - | - |
| cpu_rome_512 | 512 | 480 | - | - |
| cpu_milan | 256 | 480 | - | - |
| gpu_rome_a100_40| 256 | 480 | 4 NVIDIA A100  | 40 |
| gpu_rome_a100_80 | 512 | 480 | 4 NVIDIA A100  | 80 |
| debug_rome ** | 256| 100 | 1 NVIDIA Quadro P1000 | 4 |

\** [debugging cluster (Used for debugging and training)](https://docs.hpc.ugent.be/Linux/interactive_debug/)

NB: There are two additional two clusters called `cpu_rome_all` and `gpu_rome_a100`.
- `cpu_rome_all corresponds` to a combination of `cpu_rome` and `cpu_rome_512`.
- `gpu_rome_a100_all` corresponds to a combination of `gpu_rome_a100_40` and `gpu_rome_a100_80`.


#### Filesystems specifics

| Filesystem name  | Intended usage | Total storage space | Personal storage space | VO storage space ** |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| $VSC_HOME | Home directory, Not the entry point to the system, same as Tier2 | ? | 3GB (fixed) | ❌ |
| $VSC_SCRATCH | Entry point to the system | ? | 3GB (fixed) | ❌ |
| $VSC_DATA | Long-term storage of large data files | ? | Depend of you account(Leuven/Gent, see above) | ❌ |
| $VSC_SCRATCH_PROJECTS_BASE/2024_300/| Temporary fast storage of ‘live’ data for calculations | ? | 20TB | upon request |

<!-- style="color: #7CA1CC;" --> \** Storage space for a group of users (Virtual Organisation or VO for short) can be increased significantly on request.

> Source : https://docs.vscentrum.be/gent/tier1_hortense.html#system-specific-aspects
> For more information on the different partitions: https://docs.vscentrum.be/en/latest/gent/tier1_hortense.html#general-information

#### Check the quota

`my_dodrio_quota`

```bash
Userquota:
Disk quotas for prj 2534840 (pid 2534840):
     Filesystem    used   quota   limit   grace   files   quota   limit   grace
        /dodrio  1.709G   2.85G      3G       -   24566  1048576 1048576       -

Quota for project gpr_compute_2024_300:
Disk quotas for prj 2641240 (pid 2641240):
     Filesystem    used   quota   limit   grace   files   quota   limit   grace
        /dodrio   15.4T     19T     20T       -  739564  1048576 1048576       -
```

On Tier1, `my_dodrio_quota` give the space available on the `$VSC_SCRATCH` (first result) and on the one on our project (in that case `/dodrio/scratch/projects/2024_300/`)



[Chapters List](https://liascript.github.io/course/?https://raw.githubusercontent.com/vib-bic-training/2024_Bioimaging_data_analysis_on_HPC/refs/heads/main/README.md#5) | [next chapter](https://liascript.github.io/course/?https://raw.githubusercontent.com/vib-bic-training/2024_Bioimaging_data_analysis_on_HPC/refs/heads/main/Chapters/Chapter02.md)




