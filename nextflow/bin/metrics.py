#!/usr/bin/env python
"""
Metric Script

Author: Benjamin Pavie
        Tatiana Woller
Created: 2025-07-02
"""

__author__ = "Benjamin Pavie , Tatiana Woller"

from skimage.measure import regionprops_table
import pandas as pd
from pathlib import Path
from argparse import ArgumentParser
import os
import numpy as np
import bioio
import tifffile
from bioio import BioImage
import openpyxl

def reorder_axis_manual(data, original_axes, desired_axes):
    """
    Reorder numpy array images axes from original_axes to desired_axes.
    
    Parameters:
        data (np.ndarray): A numpy array representing the image data
        original_axes (str): Axis order in the file (e.g., "ZCYX")
        desired_axes (str): Desired axis order (e.g., "ZYXC")
    
    Returns:
        np.ndarray: Reordered data
    """
    
    # Ensure the number of axes matches the shape
    assert len(original_axes) == data.ndim, f"Expected {data.ndim} axes, got {original_axes}"

    # Map each axis label to its index in the current data
    axis_map = {axis: i for i, axis in enumerate(original_axes)}
    
    # Determine the permutation to achieve desired_axes
    perm = [axis_map[a] for a in desired_axes]

    # Reorder the data
    data_reordered = np.transpose(data, perm)
    
    return data_reordered

def create_argument_parser():
    """Create and return an argument parser."""
    parser = ArgumentParser(description='Extracts features from a labels image using skimage.measure.regionprops_table. \n' \
    'The output is saved as an Excel file with the features of each label in the labels image. \n' \
    'The script can handle images with different axes orders and will reorder them to ZYXC for images and ZYX for labels by default. \n' \
    'You can specify the axes order of the input images using --image_axes and --label_axes arguments. \n' \
    'The properties to extract can be specified using the --properties argument, separated by commas. \n' \
    'python metrics.py --image_path ..\\cellpose\\test_ZYXC_c2_tifffile.czi --label_path ..\\cellpose\\test_ZYXC_c2_tifffile.ome_cp_masks.tif --image_axes ZYXC --label_axes ZYX --properties label,centroid,area,max_intensity --output_dir ..\\cellpose')
    parser.add_argument('--image_path',  type=str, help='image path')
    parser.add_argument('--label_path', type=str, help='labels image path')
    parser.add_argument('--image_axes',  type=str, help='image axes order (default ZYXC)')
    parser.add_argument('--label_axes', type=str, help='label axes order (default ZYX)')

    parser.add_argument('--output_dir', type=str, help='output directory')  
    parser.add_argument(
        '--properties', 
        type=lambda s: s.split(','),
        default=['label', 'centroid', 'area', 'max_intensity', 'mean_intensity', 'min_intensity'], 
        help='properties to extract from the labels image, separated by commas (default  label,centroid,area,max_intensity,mean_intensity,min_intensity)'
    )
    return parser

if __name__ == "__main__":
    args = create_argument_parser()
    args = args.parse_args()
    img_bioio = BioImage(args.image_path)
    image = img_bioio.get_image_data("ZYXC", T=0)  # returns 4D CZYX numpy array
    labels = tifffile.imread(Path(args.label_path))

    if args.image_axes:
        image = reorder_axis_manual(image, original_axes=args.image_axes, desired_axes='ZYXC')
    if args.label_axes:
        labels = reorder_axis_manual(labels, original_axes=args.label_axes, desired_axes='ZYX')

    features_table = regionprops_table(
        labels,
        intensity_image=image,
       properties = args.properties,
    )
    df_features = pd.DataFrame(features_table)
    image_filename = Path(args.image_path).stem
    df_features.insert(0, 'file', image_filename)
    output_excel = os.path.join(args.output_dir, f"nuclei_analysis_{image_filename}.xlsx")
    df_features.to_excel(output_excel, index=False)
