# Chapter 5 : Python and Notebooks

The following notebooks are used :
- https://github.com/vib-bic-training/HPC_bioimage_analysis/blob/main/notebooks/modules_cell_segmentation_cellpose.ipynb
- https://github.com/vib-bic-training/HPC_bioimage_analysis/blob/main/notebooks/test_venv.ipynb

You do not need to download unless you do not have an access to Tier1

## Why should I use this
- Run Interactive Code
- In a web browser (Chrome/Firefox/Safari/…)
- Combine Code (Python), Text (Markdown) and Visualization in a single document
- Ideal to explore Bio-Image Analysis
- 3 flavors :

| VSCode Server    | Jupyter | JupyterLab |
| -------- | ------- | ------- |
| <img width="90" height="90" alt="vs_code_server_logo" src="https://github.com/user-attachments/assets/deced641-5ab5-49c1-a001-053ec2ca9c11" /> | <img width="90" height="90" alt="jupyter_lab" src="https://github.com/user-attachments/assets/1be7e077-d664-4994-8fd4-760d270789f8" /> | <img width="88" height="107" alt="jupyter_notebook_logo" src="https://github.com/user-attachments/assets/b5d44681-c723-4bc7-9f7c-dd9b49e0e14b" /> |

All 3 are available on Tier 1 via the On Demand interface

<img width="354" height="423" alt="notebook_on_demand" src="https://github.com/user-attachments/assets/8e1e2bd2-5af5-4f92-89f3-586899ca4888" />


In this tutorial, we will focus on **VS Code Server**

## Which infrastructure to use
### Using pre-installed libraries
- EasyBuidl Modules : if you can work with centrally installed softwares (modules), you can use either VS Code Server, Jupyter notebook or Jupyterlab.
### Using custom libraries 
In case, you need more specific python librairy, you can:
- Use venv and use it with VS Code Server. In that case, you can mix **easybuild** modules **and** extra **pip** packages
- Use conda : Install a miniconda and create your own conda environment with **conda** and/or **pip** packages

## EasyBuild Modules & VS Code Server

### Why VS Code Server
- (VS)Code Server use the same interface as VSCode
- EasyBuild Modules so you have nothing to install yourself (
See [here](https://github.com/vib-bic-training/HPC_bioimage_analysis/blob/main/Chapters/chapter4.md) to search available modules).

### Demo / hands-on
In this demo, we will segment with Cellpose uisng the pre-installed module.

1. Connect to the login node
<img width="371" height="88" alt="terminal_01" src="https://github.com/user-attachments/assets/29059f95-e64e-4826-a499-86412cc4e17d" />

2. In the terminal, search for the cellulose module and identify it
<img width="852" height="78" alt="terminal_02" src="https://github.com/user-attachments/assets/2f77e166-aa0d-41d6-aa9b-a07b3bcc1e25" />

```bash
module spider Cellpose
Cellpose/2.2.2-foss-2022a
```
3. Relate the module version with the right GCC

| FOSS  | GCC |  CUDA | OpenMPI | OpenBLAS | FFTW | ScaLAPACK |IPython|Python|
| ------| --- | ----- | ------- | -------- | ---- | --------- | --------- | --------- |
| 2024.05 | 13.3.0| 12.4.0-12.6.0| 5.0.3| 0.3.27| 3.3.10 | 2.2.0-fb | - | -|
| 2023b | 13.2.0 | 12.4.0-12.6.0| 4.1.6 | 0.3.24 | 3.3.10  | 2.2.0-fb | 7.2.0-GCCcore-13.2.0|3.12.3| 
| 2023a | 12.3.0 | 12.2.0| 4.1.5| 0.3.23| 3.3.10  | 2.2.0-fb |  7.0.2  GCCcore 12.3.0|Python 3.11.3  |
| 2022b | 12.2.0 | 12.0.0 | 4.1.4 | 0.3.21 | 3.3.10 | 2.2.0-fb | 7.0.3  GCCcore 12.2.0 | Python 3.10.8 |
| **2022a** | **11.3.0** | 11.7.0 | 4.1.4 | 0.3.20 | 3.3.10 | 2.2.0-fb |**8.5.0  GCCcore 11.3.0**  |  **Python 3.10.4**|
| 2021b | 11.2.0 | - | 4.1.1 | 0.3.18 | 3.3.10 | 2.1.0-fb | 6.4.0  GCCcore 11.2.0| Python 3.9.6 |
| 2021a | 10.3.0 | - | 4.1.1 | 0.3.15 | 3.3.9 | 2.1.0-fb |7.25.0 GCCcore 10.3.0 | Python 3.9.5 |

4. Start a new session with pre-loaded modules using the following parameters

- Cluster : `dodrio gpu_rome_a100`
- Time : `1 hour`
- Number of node : `1`
- Number of Core : `8`
- Number of GPU : `1`
- Code server version : `4.103.2`
- Working directory : `/dodrio/scratch/projects/2024_300`
- Custom Code : 
```bash
module load AICSImageIO/4.14.0-foss-2022a
module load matplotlib/3.5.2-foss-2022a
module load Cellpose/2.2.2-foss-2022a
```
-	Reservation ID : `vib_bioimaging`

<img width="896" height="366" alt="vs_code_server_01" src="https://github.com/user-attachments/assets/6e632676-7987-4741-b9fe-6b5730df0217" />

5. Load the jupyter notebook
Load the jupyter notebok located in `/dodrio/scratch/projects/2024_300/training/2025/notebooks/modules_cell_segmentation_cellpose.ipynb`
<img width="477" height="236" alt="vs_code_server_02" src="https://github.com/user-attachments/assets/a30f474f-5f31-426c-8728-78608aaeeaff" />

<img width="540" height="163" alt="vs_code_server_03" src="https://github.com/user-attachments/assets/dfcbd4b7-b56c-4fd9-a2ff-0680da7deb6e" />

6. Save a copy in your folder

Save it into your folder, e.g. `/dodrio/scratch/projects/2024_300/username`

<img width="316" height="223" alt="vs_code_server_04" src="https://github.com/user-attachments/assets/a94b05c8-bffa-46f9-be25-38c773a00167" />

<img width="541" height="85" alt="vs_code_server_05" src="https://github.com/user-attachments/assets/0f4a8121-3342-4e07-b735-fb461d1c48e9" />

7. Open the Notebook, and display the Terminal

<img width="601" height="107" alt="vs_code_server_06" src="https://github.com/user-attachments/assets/099fee31-90cf-47a5-8b38-1d787d9cf033" />

<img width="544" height="205" alt="vs_code_server_07" src="https://github.com/user-attachments/assets/89b24bc3-063f-4abf-b97f-8e933c7cd58b" />

8. Identify the current python in the terminal

In the terminal, check the python version running
```bash
which python
```
<img width="550" height="134" alt="vs_code_server_08" src="https://github.com/user-attachments/assets/df5e9f1b-1048-4ebe-ad19-5438419d34c5" />

9. Select the right Python
Select the correct version of python, here `Python 3.10.4`

<img width="871" height="171" alt="vs_code_server_09" src="https://github.com/user-attachments/assets/f035e991-1ff0-4495-b3d0-e401cbac8477" />

<img width="607" height="140" alt="vs_code_server_10" src="https://github.com/user-attachments/assets/fa264032-5aa0-40c3-beb5-784cf88275d5" />

<img width="471" height="374" alt="vs_code_server_11" src="https://github.com/user-attachments/assets/398b6eab-5ab4-4543-ac89-93f9b6386463" />

9. Run the notebook cell by cell

For it, put your mouse over the code block and click on the run button

<img width="447" height="118" alt="vs_code_server_13" src="https://github.com/user-attachments/assets/fa84961f-71b4-4fcb-99ae-8db5d814edfb" />

<img width="675" height="374" alt="vs_code_server_12" src="https://github.com/user-attachments/assets/52353f89-6457-4bd7-9b1b-394641fec85d" />

### Run linux command

You can run a command by adding a `!` in front of it, e.g.

```bash
!pip install czifile
```

```bash
!cp /dodrio/scratch/projects/2024_300/training/2024/devbio/*.tif /dodrio/scratch/users/vsc33625/
```

```bash
!module list
!module av | grep -i aicsimageio
!module load AICSImageIO/4.14.0-foss-2022a
```

## venv & VS Code Server

### Why 
- venv is Built-in with Python:
Part of the Python standard library, so it comes pre-installed with Python (Python 3.3 and newer).
Create virtual environments using the command: python -m venv myenv.
- Lightweight:
Relatively lightweight and provides basic virtual environment functionality.
Creates isolated Python environments with their own set of packages.
- Package Manager:
It uses pip as the package manager to install Python packages within the virtual environment.
Can co-exist with EasyBuild Module
- Notebooks:
Compatible with Jupyter notebooks and VSCode server

### Demo / hands-on

1. Start a new terminal session : Shell (tmux)

<img width="395" height="414" alt="venv_01" src="https://github.com/user-attachments/assets/dc63ba3a-5bb1-4a19-87ee-06462a52750e" />

<img width="648" height="371" alt="venv_02" src="https://github.com/user-attachments/assets/df6c2ba0-098d-4513-99fe-f2d6ea2de767" />

2. Build a new venv

In the terminal, go to you $VSC_DATA and create a directory to store your venv
```bash
cd $VSC_DATA
mkdir venv_collection
cd venv_collection
```

3. Load the easybuild modules
```bash
module load vsc-venv
module load matplotlib/3.9.2-gfbf-2024a
```

4. Create a venv named training_2025

```bash
python -m venv training_2025
```
It will create a new directory `$VSC_DATA/venv_collection/training_2025`

5. Activate the venv
```bash
source training_2025/bin/activate
```

6. Install complementary pip packages
```bash
pip install bioio==2.0.0 bioio-czi bioio-ome-tiff
pip install ipykernel stackview ipycanvas
```

7. Create a notebook kernel using the venv `training_2025` with a display name `train_2025`
```bash
python -m ipykernel install --user  --name training_2025 --display-name train_2025
```

8. Check you installed kernel
```bash
jupyter kernelspec list
```
Now, your venv is available via the Jupyter notebook, let’s try it!


> [!TIP]
> How remove a kernel :
> ```bash
> jupyter kernelspec remove training_2025
> ```

9. use the venv by starting a new Code Server Session

<img width="408" height="323" alt="venv_03" src="https://github.com/user-attachments/assets/5c550f19-fe26-47a9-b04b-10c22bb12138" />

<img width="435" height="323" alt="venv_04" src="https://github.com/user-attachments/assets/6aac6b5a-db3a-4b8d-93e0-c80ffc077c2b" />

<img width="427" height="107" alt="venv_05" src="https://github.com/user-attachments/assets/4e273710-0077-4144-8ae6-4933dc29ef99" />

<img width="928" height="322" alt="venv_06" src="https://github.com/user-attachments/assets/e1383649-3c22-4cf2-872e-d312d23bba26" />

<img width="351" height="268" alt="venv_08" src="https://github.com/user-attachments/assets/d5069986-ba27-49e4-87a7-4d4907190cf3" />

10. Open the Notebook

Select the notebook `/dodrio/scratch/projects/2024_300/training/2025/notebooks/test_venv.ipynb`

<img width="505" height="323" alt="venv_09" src="https://github.com/user-attachments/assets/991e148e-d2e6-462c-a48e-2d624af22feb" />

11. Save a copy in your folder

Save it into your folder, e.g. `/dodrio/scratch/projects/2024_300/username`

<img width="316" height="223" alt="vs_code_server_04" src="https://github.com/user-attachments/assets/a94b05c8-bffa-46f9-be25-38c773a00167" />

<img width="548" height="297" alt="venv_10" src="https://github.com/user-attachments/assets/642e3c54-13ac-4f93-bf68-2b97218b9b58" />

12. Select the right kernel

Go on `Select Kernel` > `Jupyter kernel` > `train_2025`

<img width="928" height="116" alt="venv_11" src="https://github.com/user-attachments/assets/97a463ce-f5ea-44b4-a73b-0de4bb551118" />

<img width="508" height="191" alt="venv_12" src="https://github.com/user-attachments/assets/9a4fc504-db74-4427-8000-f33d998665ae" />

13. Run the Jupyter Notebook !

### Others

You can also install additional extension for `Git`, `Nextflow`, `Docker` by clicking on the extension icon (cube).


## Conda environments

### Miniconda3 installation
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

### Create a new conda environment

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
python -m ipykernel install --user --name myenv --display-name myenvsDisplayName 
```

> [!NOTE]
> 
> - `--name` : conda environment name
> - `--display-name` : Name which will appear as a kernel name in the jupyter notebook
> 

> [!TIP]
> 
> you can pull from public and private repositories from github on VSC and then build a conda env from the yaml of the repo. In addition, you can also push back your code.
>
> ``` git clone any_repository```
>

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
