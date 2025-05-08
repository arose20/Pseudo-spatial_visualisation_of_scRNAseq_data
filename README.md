# Pseudo-spatial visualisation of scRNAseq data

This repository contains information about visulaising counts based information data (in this case scRNAseq data) through free form polygons.

This visualisation is also sometimes termed ELMER visualisation.

For online visualisation please visit: [https://github.com/arose20/sci-adifa-elmer](https://github.com/arose20/sci-adifa-elmer)

For a real life example please see [Example use case below](#example-use-case)

## Example workflow

Below is an example abstract workflow of how this visualisation can work for single cell data.

Note, this visualisation doesn't require any spatial information / change to protocol for scRNA-seq generation if instead want to use masks for different metadata instead such as donor, age, sex, location etc. 

This example just suggests how you could implement some physical spatial metadata into the scRNA-seq protocol (designed for non-spatial specific scRNA-seq data). This can also work with other types of data e.g. protein. 

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

Important notes:
- Given this works off the inputted counts matrix, if you were to subset the counts matrix prior to a specific celltype(s) / lineage of interest then the visualisation will be only representing this subset of the original data. This enables more detailed investigations of count expression without considering all data within a pseudo-spatial region.

- This visualisation uses a counts matrix so this could be swapped out to represent different types of data such as protein

## Example use case

As part of linking the [Human Developmental Cell Atlas](https://www.humancellatlas.org/biological-networks/development-biological-network/) with the clinical community, the organisation [DECIPHER](https://www.deciphergenomics.org/) in collaboration with the [Haniffa lab](https://haniffalab.com/) utalise this pseudo-spatial visualisation technique to show the expression of clinical genes of interest across twelve broad anatomical regions of late stage human embryos. The data to enable this, generated and provided by the Haniffa lab, is three human embryos staged at 6 post conception weeks (PCW); a key timepoint during organogenesis where the development of most organs have commenced. These embryos were deeply profiled to generate scRNA-seq data where each cell can be mapped to a broad spatial region. This data is currently unpublished.

The below example shows the inclusion of a 'Expression' tab to the Decipher portal layout (added in v11.31) which displays the gene of interest using pseudo-spatial visualisation. TBX5 is key for upper limb development and it is known that haploinsufficiency of TBX5 causes Holt-Oram syndrome; a hand-heart syndromeis. Using pseudo-spatial visualisation, TBX5 expression is shown in the segments of the embryo related to the heart and limbs.


<div style="display: flex; justify-content: center;">
  <a href="https://www.humancellatlas.org/biological-networks/development-biological-network/" target="_blank">
    <img src="https://github.com/arose20/Pseudo-spatial_visualisation_of_scRNAseq_data/blob/arose20-patch-Decipher/resources/Haniffa_lab_logo.png" height="60" style="margin-right: 10px;" />
  </a>
  <a href="https://haniffalab.com/" target="_blank">
    <img src="https://github.com/arose20/Pseudo-spatial_visualisation_of_scRNAseq_data/blob/arose20-patch-Decipher/resources/logo-hca.png" height="60" style="margin-right: 10px;" />
  </a>
  <a href="https://www.deciphergenomics.org/" target="_blank">
    <img src="https://github.com/arose20/Pseudo-spatial_visualisation_of_scRNAseq_data/blob/arose20-patch-Decipher/resources/Decipher_logo.png" height="60" />
  </a>
</div><br><br>

![https://github.com/arose20/Pseudo-spatial_visualisation_of_scRNAseq_data/blob/arose20-patch-Decipher/resources/Decipher_TBX5_example.png](https://github.com/arose20/Pseudo-spatial_visualisation_of_scRNAseq_data/blob/arose20-patch-Decipher/resources/Decipher_TBX5_example.png)


## Repository content
This repository is split into the following:
1. Mask generation
    - Options to generate masks in a common co-ordinate framework (CCF) using either Fiji or Plotly
      
2. Combine single cell data and masks
    - Adapter notebook to combine the masks and single cell data together (will also work for sci-adifa-elmer web atlas platform)
      
3. Local visualisation
    - Options to plot the pseudo-spatial visualisation using matplotlib or plotly


