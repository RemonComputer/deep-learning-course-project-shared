# What is this?
- This is a two notebook project that enables you to install Julia on colab and use it like Julia box or like the local juputer with julia kernel
- "Installing_Julia_and_checking_kernel.ipynb" Will install julia and display the version of available colab kernels, Julia Kernel should be displayed
- "Julia_Kernel.ipynb" This is your julia starting point.

# How did I made the above files
- I intsalled Julia from colab.
- I modified an normal ipynb notebook to use the julia kernel that was installed by a command in the first notebook, this notebook uses GPU but it can be modified using the same principle to use TPU, of course TPU support in julia should be installed, I modified the file using Nomal Text Editor (open it and you will see what I am talking about).
- For more info and How did I know this info in the first place see the Credits Section.

# How to open those notebooks from colab
- To open any of the above notebooks:
    - Choose File -> open notebook -> upload -> choose the notebook file
    - You can now run the notebook
- Run the installation note book
- Run the Julia Kernel notebook as your starting point.
- If you at any point you find that colab cannot run julia commands then this means that the environment has been reset and you need to need to re-run the intsallation notebook, and you might need to re-run Julia Kernel notebook (I didn't try it).
    
# Credits
- https://discourse.julialang.org/t/julia-on-google-colab-free-gpu-accelerated-shareable-notebooks/15319
- https://github.com/googlecolab/colabtools/issues/13
