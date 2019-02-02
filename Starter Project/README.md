# What is this?
- This is a starter project you can use to start your project
- It does the following:
    - installes Juila.
    - downloads the original training set and the modified training set (see "Filtering Training Data" Folder on instructions how this data was made) using a perl script.
    - It contains the note book that you will use to experiment in your project "Julia Kernel" (for instructions on how this kernel was made see "Hacking Google Colab For Julia" Folder).

# What you should expect after running the environment preparation notebook
- You should expect that Julia is installed
- There is a Folder called Dataset which contains:
    - train.tar.xz (The training data which only contains the 12 labels by the doctor document).
    - train (The result of  extraction of train.tar.xz folder).
    - train.csv (The labels file of the 12 whale Ids).
    - test.zip (The test data of the competition).
    - test (The result of extracting test.zip).
    - sample_submission.csv (A sample submission file - of the original competition).
    - train_original.csv (The original labels file of the competition).
    - train_original.zip (The original training data).
    - train_original (The result of extracting train_original.zip).

# How to open those notebooks from colab
- To open any of the above notebooks (in colab do the following):
    - Choose File -> open notebook -> upload -> choose the notebook file
    - You can now run the notebook
- Run the preparation notebook.
- Run the Julia Kernel notebook as your starting point.
- If you at any point you find that colab cannot run julia commands then this means that the environment has been reset and you need to need to re-run the intsallation notebook, and you might need to re-run Julia Kernel notebook (I didn't try it).
    
# Credits
- https://discourse.julialang.org/t/julia-on-google-colab-free-gpu-accelerated-shareable-notebooks/15319
- https://github.com/googlecolab/colabtools/issues/13
- https://github.com/circulosmeos/gdown.pl

