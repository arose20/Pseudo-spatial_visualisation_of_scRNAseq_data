# Pseudo-spatial visualisation of scRNAseq data

This repository contains information about visulaising counts based information data (in this case scRNAseq data) through free form polygons.

This visualisation is also termed ELMER visualisation.

For online visualisation please visit: [https://github.com/arose20/sci-adifa-elmer](https://github.com/arose20/sci-adifa-elmer)

## Example workflow

Below is an example abstract workflow of how this visualisation can work for single cell data.

Note, this visualisation doesn't require any spatial information / change to protocol for scRNA-seq generation if instead want to use masks for different metadata instead such as donor, age, sex, location etc. 

This example just suggests how you could implement some physical spatial metadata into the scRNA-seq protocol (designed for non-spatial specific scRNA-seq data).

The image can be whatever the user can draw and link individual data points to, treating it like it had a spatial image or any other representative image(s).

![https://github.com/ar32/Pseudo-spaital_visualisation_of_scRNAseq_data/resources/pseudo_spatial_example_workflow.png](https://github.com/arose20/Pseudo-spatial_visualisation_of_scRNAseq_data/blob/main/resources/elmer_github_workflow.gif)

## Pseudo-spatial plotting options

This repository contains code to plot these pseudo-spatial images using Matplotlib or Plotly within python, as well as a basic Excel implementation.

Current options for how to use this visualisation:
- Plot gene expression values across sections
- Plot the number of counts for a given celltype(s) for each section
- Plot the percentage contribution for a given celltype(s) for each section
- Plot the percentage contribution for a given celltype(s) across sections
- Plot completely manual values for each section

Additional features:
- Turn individual masks on or off. This is useful for example if 1 or multiple section(s) is overshadowing other sections too much
- Swap masks out depending on what image you want to use to represent the data
- Change colourmap and scale bar range

Note: this visualisation uses a counts matrix so this could be swapped out to represent different types of data such as protein

## Repository content
This repository is split into the following:
1. Mask generation
    - Options to generate masks in a common co-ordinate framework (CCF) using either Fiji or Plotly
      
2. Combine single cell data and masks
    - Adapter notebook to combine the masks and single cell data together (will also work for sci-adifa-elmer web atlas platform)
      
3. Local visualisation
    - Options to plot the pseudo-spatial visualisation using matplotlib or plotly


