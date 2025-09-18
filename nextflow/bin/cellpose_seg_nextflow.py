#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from cellpose import models
import numpy as np
from pathlib import Path
import tifffile
from argparse import ArgumentParser


parser = ArgumentParser(description='Process some parameters.')
parser.add_argument('--image_path', type=str, help='image path')
parser.add_argument('--output_dir', type=str, help='output directory')
parser.add_argument('--cellpose_model', type=str, default='', help='model type')
parser.add_argument('--file_extension', type=str, help='file extension')
parser.add_argument('--diameter', type=float, default=70, help='cell diameter')
parser.add_argument('--cellprob_threshold', type=float, default=-3, help='cell probability threshold')
parser.add_argument('--flow3D_smooth', type=float, default=2, help='3D flow smoothing')
parser.add_argument('--anisotropy', type=float, default=5, help='anisotropy factor for 3D')
parser.add_argument('--min_size', type=int, default=1000, help='minimum size of objects')
parser.add_argument('--channel_axis', type=int, default=3, help='channel axis')
parser.add_argument('--z_axis', type=int, default=0, help='z axis')
# New boolean arguments
parser.add_argument('--use_gpu', action='store_true', help='use GPU for processing')
parser.add_argument('--Zstack', action='store_true', help='process Z-stack images')
parser.add_argument('--do_3D', action='store_true', help='enable 3D processing')
parser.add_argument('--verbose', action='store_true', help='verbose output')
parser.add_argument('--save_tif', action='store_true', help='save TIFF files')
parser.add_argument('--no_npy', action='store_true', help='do not save NPY files')

args = parser.parse_args()

# Load image
image = tifffile.imread(Path(args.image_path))
image_name = Path(args.image_path).stem

# Initialize model with GPU support based on argument
model = models.CellposeModel(gpu=args.use_gpu, model_type=args.cellpose_model)


# Run segmentation with 3D processing if enabled
masks, flows, styles = model.eval(
    image, 
    diameter=args.diameter,
    channel_axis=args.channel_axis,
    z_axis=args.z_axis,
    do_3D=args.do_3D,
    anisotropy=args.anisotropy,
    cellprob_threshold=args.cellprob_threshold,
    flow_threshold=None,
    min_size=args.min_size,
    stitch_threshold=0.0,
    progress=args.verbose  
)

# Create output directory if it doesn't exist
output_dir = Path(args.output_dir)
output_dir.mkdir(exist_ok=True)

# Save the mask as a separate tif file (controlled by save_tif argument)
if args.save_tif:
    tifffile.imwrite(output_dir / f"{image_name}_cp_masks.tif", masks.astype(np.uint16))
    
    # Save flows if needed (equivalent to --save_tif behavior)
  #  if flows is not None and len(flows) > 0:
  #      tifffile.imwrite(output_dir / f"{image_name}_cp_flows.tif", flows[0])

# Save NPY files only if --no_npy is not specified
if not args.no_npy:
    np.save(output_dir / f"{image_name}_cp_masks.npy", masks)
    if flows is not None and len(flows) > 0:
        np.save(output_dir / f"{image_name}_cp_flows.npy", flows[0])

if args.verbose:
    print(f"Segmentation complete. Results saved to: {output_dir}")
    if args.save_tif:
        print(f"TIFF masks saved to: {output_dir / f'{image_name}_cp_masks.tif'}")
    if not args.no_npy:
        print(f"NPY masks saved to: {output_dir / f'{image_name}_cp_masks.npy'}")
