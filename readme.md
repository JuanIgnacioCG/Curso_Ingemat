# USE-CASES

This repository contains lessons for the Juan Ignacio's tutorials/use-cases. Each  is a
[jupyter lab](https://jupyter.org/), located inside the `use-cases` folder.

To be able to run the code you should do the following three steps.

# 0. Download Anaconda

Download [anaconda](https://www.anaconda.com/products/individual) and install for your operative system. 


# 1. setup

Start by downloading this repository. If you already use git, you can use the
following command to clone this repository to your local machine:

```
git clone https://github.com/sofroniewn/napari-training-course
```

If you don't already use git, you can download the whole repository as a zip
file, which you can then unzip on your computer. The file is available at green button where it is written 'code' in the upper part of the web:


Once cloned or unzipped you should open an 'Anaconda-prompt' or terminal and navigate to the `napari-training-course`
directory from the command line replacing if necessary '(yourpath_use-cases)'.

```
cd (yourpath_use-cases)napari-training-course
```

Another option is to open the anaconda-navigator, in the environment tab select import and select the 'napari.yml' file from the location you downloaded.


# 2. installation

If you have never seen conda environments, Robert 
Haase provides a simple introduction in [this lecture](https://www.youtube.com/watch?v=MOEPe9TGBK0).

Once you have a working conda installation, you have two options. The second
one should work in non-conda environments too but only do this if you know what
you are doing!

## a. create a conda environment for the use-cases (recommended)

We have provided a pre-defined environment for you to use. Using the command line,
you can create it with the command:

```python
conda env create -f napari.yml
```

And then activate it with:

```python
conda activate napari
```

## or b. use a pre-existing conda environment (alternative)

you can use our provided requirements.txt file (Not implemented yet):

```
pip install -r requirements.txt
```


# 3. checking that your install is working

So far there is no other way than running the cases.