#!/usr/bin/env python
"""
Convert microscopy file format using bioio ( https://github.com/bioio-devs/bioio ) and save as OME-TIFF.
Use --channels and --time_point to select specific channels and time points.

Author: Benjamin Pavie
        Tatiana Woller
Created: 2025-07-04
"""

__author__ = "Benjamin Pavie , Tatiana Woller"

# python convert_to_ome_tiff.py --image_path bioimage_analysis_training_dataset_cells.czi --output_dir ..\\cellpose --channels 0,2 --time_point 0  

from bioio import BioImage
import tifffile
import numpy as np
from argparse import ArgumentParser
import os
from pathlib import Path

def _xy_voxel_size(tags, key):
    """Get the physical pixel size in micrometers for X or Y resolution"""
    assert key in ['XResolution', 'YResolution']
    if key in tags:
        num_pixels, units = tags[key].value
        return units / num_pixels
    # return default
    return 1.

def create_argument_parser():
    """Create and return an argument parser."""
    parser = ArgumentParser(description='Process some parameters.')
    parser.add_argument('--image_path',  type=str, required=True, help='image path')
    parser.add_argument('--output_dir', type=str, required=True, help='output directory')  
    parser.add_argument(
        '--channels', 
        type=lambda s: list(map(int, s.split(','))),
        help='Comma-separated list of channels to keep (e.g., "0,2")'
    )
    parser.add_argument('--time_point', type=int, help='time point to use, if more than one')
    return parser


if __name__ == "__main__":
    parser = create_argument_parser()
    args = parser.parse_args()
    img = BioImage(args.image_path)
    print(img.dims, img.data.shape, img.dims.order)
    if args.time_point and img.dims.T<=args.time_point is not None:
        data = img.get_image_data("ZYXC", T=args.time_point)
    else:
        data = img.get_image_data("ZYXC", T=0)  # returns 4D CZYX numpy array
    # Keep only channel specific channels if specified
    data = data[..., args.channels] if args.channels else data
    #print(data.shape)

    output_file_path = os.path.join(args.output_dir, Path(args.image_path).stem + '.ome.tiff')


    if(data.shape[3] > 1):
        # Save as OME-TIFF ZYXC
        tifffile.imwrite(output_file_path,
            data,
            photometric='minisblack',
            planarconfig='contig',
            metadata={'axes': 'ZYXC',
            'PhysicalSizeX': img.physical_pixel_sizes.X,
            'PhysicalSizeY': img.physical_pixel_sizes.Y,
            'PhysicalSizeZ': img.physical_pixel_sizes.Z,
            'PhysicalSizeXUnit': 'µm',
            'PhysicalSizeYUnit': 'µm',
            'PhysicalSizeZUnit': 'µm'
            }
        )
    else:        
        # Save as OME-TIFF ZYX
        tifffile.imwrite(output_file_path,
            data[..., 0],
            photometric='minisblack',
            metadata={'axes': 'ZYX',
            'PhysicalSizeX': img.physical_pixel_sizes.X,
            'PhysicalSizeY': img.physical_pixel_sizes.Y,
            'PhysicalSizeZ': img.physical_pixel_sizes.Z,
            'PhysicalSizeXUnit': 'µm',
            'PhysicalSizeYUnit': 'µm',
            'PhysicalSizeZUnit': 'µm'
            }
        )
