<!--

author:   Pavie Benjamin, Tatiana Woller
email:    benjamin.pavie@vib.de
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
# Chapter 1 : Infrastructure

Check here what are the clusters available in each section of the VSC. You can see the names and some of the resources linked to each of them. This might not make much difference for you now, but is very useful when you wan to optimize your analysis and pipelines.

Sending a job into an appropriate cluster can make the difference in how much time you wait in the "line" and how much memory you will have available for example.


## Introduction to HPC

High performance computing (HPC) is a technology that uses clusters of powerful processors, working in parallel, to process massive multi-dimensional datasets (big data) and solve complex problems at extremely high speeds. HPC systems typically perform at speeds more than one million times faster than the fastest commodity desktop, laptop or server systems. [https://www.ibm.com/topics/hpc].

HPC is extremely valuable for fields where deep-learning and machine learning algorithms are daily routine for example.

The European model for HPC consists of three levels of computing capacity:

1. When available at research institutions its called Tier-2.

2. When provided at the level of a region/country because it exceeds the capacity of an institution in terms of needs/costs its called Tier-1.

3. When available at EU level, with **very** large-scale computing infrastructure, its called Tier-0.

**By contrast, Tier-3 corresponds to single computers (your own infrastructure)**


> Flemish super computing centre (VSC)
>
> REF: https://www.vscentrum.be/about
> The Flemish Supercomputing Centre (_Vlaams Supercomputer Center_) is a collaboration between the five universities in Flanders
> - VUB
> - KU Leuven
> - UGent
> - UHasselt
> - UAntwerpen). 
> [replace with the logo of each university for a better visual]
>
>The VSC has developed a differentiated infrastructure (Tier-1 and Tier-2 level) that is available to the academic and business world. 
> Researchers of those universities can get access to Tier-2 infrastructures through their university for free or for a preferential prices.
> In addition, access to Tier-1 infrastructures is allocated through project grants.
> The Tier-1 services encompass :
> - Tier-1 data (active storage and RDM)
> - Tier-1 cloud (virtual machines and etc...)
> - Tier-1 compute (calculations, access through terminal or through graphical user interface through Open On Demand)


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




