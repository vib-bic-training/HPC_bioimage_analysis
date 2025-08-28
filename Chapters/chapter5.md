# Chapter 5 : Python and jupyter notebooks

## Which infrastructure to use

If you can work with centrally installed softwares (modules) and you want to use jupyter notebooks, you can use either Jupyter notebook or Jupyterlab.
In case, you need more specific python librairy, you can install a miniconda and create your own conda environment that can be used in Jupyter notebook or Jupyterlab.
If you can work with only python scripts or you need to mix different languages, you can use vscode server. 

## How to make customed conda environments

### Installation miniconda3
```
cd $VSC_DATA
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh
```
The installer will show the license agreement. Read and accept it. When asked for the desired Miniconda installation location, do *not* accept the default path but instead enter `$VSC_DATA/miniconda3`. The default installation folder would be your home folder, whose disk space is too limited. 

![miniconda installation](../images/miniconda-installation1.png)

When asked "Do you wish the installer to initialize Miniconda3 by running conda init? [yes|no]", answer `yes`.

![miniconda installation](../images/miniconda-installation2.png)

When the installation has finished,

- restart your environement: `. ~/.bashrc` so conda command will be set in your path
- run

```
conda config --set auto_activate_base false
```

in the terminal. This will avoid activating the base conda environment automatically every time a new terminal window is opened.


Open a new terminal window. No conda environment should be activated yet. You can activate the default environment with:

```
conda activate
```

The terminal prompt should then change to something like `(base) [vsc12345@gpu123 ~]$ `

### Creating a new conda environment

A new conda environment can now be created as usual, and Python packages can be installed in it.

```
conda create --name my-conda-env
conda activate my-conda-env
pip install apythonpackage
```

Alternatively, if you have a conda environment yaml file, the environment can be created from it, like so:

```
conda env create -f environment.yml
```

To list the available conda env or to get more info about the conda installation, type:
```
conda env list
conda info
# to remove an environment
conda env remove -n myenv
```
 To create a kernel for jupyter notebook:

 ```
source activate myenv
conda install ipykernel
python -m ipykernel install --user  --name careamics --display-name CAREamics 
```
> [!TIP]
> 
> you can pull from public and private repositories from github on VSC and then build a conda env from the yaml of the repo. In addition, you can also push back your code.
>
> ``` git clone any_repository```
>

## How to use venv and combined it with modules

```
# choose the right python version
module load Python/3.10.4-GCCcore-11.3.0
# load vsc-venv
module load vsc-venv
python -m venv bioio
source bioio/bin/activate
pip install bioio bioio-czi
pip install ipykernel
python -m ipykernel install --user  --name bioio --display-name bioioczi 
```


## Jupyter notebook
## How to start Jupyter notebook
Go to [the Open On Demand portal](https://tier1.hpc.ugent.be/) and log in after multifactor-authentification

Select **Jupyter notebook** or Jupyterlab (maybe more **Jupyter notebook** since you can modify the `Working Directory`) with the following specifications: 
![image](https://github.com/vib-bic-training/HPC_training_bioimaging_1/assets/103046100/2dd8d125-d679-4837-9798-07b78b2b0bbd)
![image](https://github.com/vib-bic-training/HPC_training_bioimaging_1/assets/103046100/31182681-1283-47ec-ad04-a43efffeb34a)

How to list existing kernels and how to remove them:
```
!jupyter kernelspec list
!jupyter kernelspec uninstall  pycudadecon -y
```


Required modules:
- `module load n2v/0.3.2-foss-2022a-CUDA-11.7.0`
- `module load matplotlib/3.5.2-foss-2022a`

## Get the notebook
The notebooks are located in https://github.com/vib-bic-training/HPC_training_bioimaging_1/tree/main/code/notebooks

Download both of them and upload them to your local storage on the VSC using the jupyter interface:
![Exclude labels on edge](/images/jupyter/02_jupyter_notebooks.png)

Then double click on the notebook `n2v_demo_01_training.ipynb` to open it and edit it to change `output_folder`:
```python
output_folder = '/dodrio/scratch/projects/2024_300/<YOUR_NAME>/nv2' #TO CHANGE
```

> [!TIP]
> 
> you could select another place as a `Working Directory`, byt modifying the value when you configure the launch of the jupyter interface
>
> ![Jupyter Working Direcotry](/images/jupyter/03_jupyter_notebooks.png)
> 

## Jupyterlab
- not working properly with modules of 2022a and not loading napari modules

## VSCode server
The advantage of vscode is that you don't need to fix the python version in advance and you can also run other programming languages beside Python (i.e. Groovy, R, Julia, Rust, C/C#/C++).

### How to start VSCode
To start vscode, select code server (nb: on Tier2 KUL: it would be called vsc code server):
![image](https://github.com/vib-bic-training/HPC_bioimage_analysis/blob/main/images/vscode_server_start.png)

Then, select the right account, the right workdir and the appropriate queue with the amount of CPU and GPU (in this example, it is CPU only)
![image](https://github.com/vib-bic-training/HPC_bioimage_analysis/blob/main/images/vscode_server_start_2.png)

### How to start a terminal and set-up

Here is how to open a terminal:
![image](https://github.com/vib-bic-training/HPC_bioimage_analysis/blob/main/images/how_to_open_a_terminal.png)

To change from folder, you can click on File > Open new folder

Nota bene: you can also install additional extension for GIT, Nextflow and docker by clicking on the extension icon (cube).

### How to run a jupyter notebook with a specific pre-build conda env

To run a specific notebook with a specific python environment, open the python notebook and then select the kernel on the top right side and click on python environment.
![image](https://github.com/vib-bic-training/HPC_bioimage_analysis/blob/main/images/how_to_select_kernel.png)

You can either make a new environment or use an existing one:
![image](https://github.com/vib-bic-training/HPC_bioimage_analysis/blob/main/images/how_to_select_env.png)

Then you should be able to import your python librairies
![images](https://github.com/vib-bic-training/HPC_bioimage_analysis/blob/main/images/vscode_check.png)


## Additional resources

### VSC reference on Python
- https://docs.vscentrum.be/compute/software/python_package_management.html
- https://docs.hpc.ugent.be/Windows/jupyter/
- https://docs.hpc.ugent.be/Windows/python/

### Jupyter Notebook 
- Deep learning : https://github.com/HenriquesLab/ZeroCostDL4Mic 
- Pipeline: https://github.com/BiaPyX/BiaPy
​- Super-resolution imaging: https://github.com/HenriquesLab/NanoPyx 

### Napari notebooks: ​
- https://github.com/BiAPoL/Bio-image_Analysis_with_Python
- https://biapol.github.io/PoL-BioImage-Analysis-TS-GPU-Accelerated-Image-Analysis/intro.html
- https://biapol.github.io/PoL-BioImage-Analysis-TS-Early-Career-Track/intro.html
- https://github.com/FrancisCrickInstitute/cbias-napari

#### BIC code
- notebooks: https://github.com/vib-bic-code/notebooks
- conda environment: https://github.com/vib-bic-code/conda_environments

### Bioimage model zoo :​
- General one: ​ https://bioimage.io/#/​

[previous chapter](https://liascript.github.io/course/?https://raw.githubusercontent.com/vib-bic-training/2024_Bioimaging_data_analysis_on_HPC/refs/heads/main/Chapters/Chapter04.md) | [next chapter](https://liascript.github.io/course/?https://raw.githubusercontent.com/vib-bic-training/2024_Bioimaging_data_analysis_on_HPC/refs/heads/main/Chapters/Chapter06.md)
