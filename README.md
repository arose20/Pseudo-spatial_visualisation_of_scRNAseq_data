# Pseudo-spatial visualisation of scRNAseq data

This repository contains information about visulaising counts based information data (in this case scRNAseq data) through free form polygons.

For online visualisation please visit: [https://github.com/arose20/sci-adifa-elmer](https://github.com/arose20/sci-adifa-elmer)

## Example workflow

Below is an abstract worklow of how this visualisation can work for single cell data.

![https://github.com/ar32/Pseudo-spaital_visualisation_of_scRNAseq_data/resources/pseudo_spatial_example_workflow.png](https://github.com/arose20/Pseudo-spatial_visualisation_of_scRNAseq_data/blob/main/resources/pseudo_spatial_example_workflow.png)

## Pseudo-spatial plotting options

This repository contains code to plot these pseudo-spatial images using Matplotlib or Plotly within python, as well as a basic Excel implementation.

Current options for how to use this visualisation:
- Plot gene expression values across sections
- Plot the number of counts for a given celltype(s) for each section
- Plot the percentage contribution for a given celltype(s) for each section
- Plot the percentage contribution for a given celltype(s) across sections
- Plot completely manual values for each section

Additional features:
- Turn individual masks on or off. This is useful for example if 1 section is overshadowing other sections too much
- Swap masks out depending on what image you want to use to represent the data
- Change colourmap and scale bar range

## Repository content
This repository is split into the following:
1. Mask generation
    - Options to generate masks in a common co-ordinate framework using either Fiji or Plotly
2. Combine single cell data and masks
    - Adapter notebook to combine the masks and single cell data together (will also work for sci-adifa-elmer web atlas platform)
3. Local visualisation
    - Options to plot the pseudo-spatial visualisation using matplotlib or plotly


