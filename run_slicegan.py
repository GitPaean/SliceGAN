### Welcome to SliceGAN ###
####### Steve Kench #######
'''
Use this file to define your settings for a training run, or
to generate a synthetic image using a trained generator.
'''

from slicegan import model, networks, util
import argparse
# Define project name
Project_name = 'NMC_exemplar_final'
# Specify project folder.
# Project_dir = 'Trained_Generators/NMC'
Project_dir = 'Trained_Generators/new'
# Run with False to show an image during or after training
# parser = argparse.ArgumentParser()
# parser.add_argument('training', type=int)
# args = parser.parse_args()
# Training = args.training
Training = True
Training = False
Project_path = util.mkdr(Project_name, Project_dir, Training)

## Data Processing
# Define image  type (colour, grayscale, three-phase or two-phase.
# n-phase materials must be segmented)
image_type = 'twophase'
# define data type (for colour/grayscale images, must be 'colour' / '
# greyscale. nphase can be, 'tif', 'png', 'jpg','array')
data_type = 'png'
# Path to your data. One string for isotrpic, 3 for anisotropic
# data_path = ['Examples/NMC.tif']
data_path = ['Examples/1024-890-max_bw.png']

## Network Architectures
# Training image size, no. channels and scale factor vs raw data
img_size, img_channels, scale_factor = 64, 3,  1
# z vector depth
z_channels = 16
# Layers in G and D
lays = 6
# kernals for each layer
dk, gk = [4]*lays, [4]*lays
# strides
ds, gs = [2]*lays, [2]*lays
# no. filters
df, gf = [img_channels,64,128,256,512,1], [z_channels,512,256,128,64,img_channels]
# paddings
dp, gp = [1,1,1,1,0],[2,2,2,2,3]

## Create Networks
netD, netG = networks.slicegan_nets(Project_path, Training, image_type, dk, ds, df,dp, gk ,gs, gf, gp)

# Train
if Training:
    model.train(Project_path, image_type, data_type, data_path, netD, netG, img_channels, img_size, z_channels, scale_factor, False)
else:
    img, raw, netG = util.test_img(Project_path, image_type, netG(), z_channels, lf=6, periodic=[0, 1, 1])
