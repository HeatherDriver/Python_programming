#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Heather D.
# DATE CREATED:  06.10.2021                     
# REVISED DATE: 
# PURPOSE: Creates the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# Defines get_pet_labels function 

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that was created with this
    # function
    results_dic = {}
    pets_names = []
    
    pet_labels = [pets for pets in listdir(image_dir)]
    image_labels = [image_labels.lower() for image_labels in pet_labels]
    images = [images.split("_") for images in image_labels]
    
    # Get Values for Dictionary
    pets_names = []
    for image in images:
        pet_name = ""
        for i in image:
            if i.isalpha():
                pet_name += i + " "
        pets_names.append(pet_name)
    values = [pets.rstrip(" ") for pets in pets_names]
    
    # Append Keys, Values to Results_Dic:
    for idx in range(0, len(pet_labels), 1):
        if pet_labels[idx] not in results_dic:
            results_dic[pet_labels[idx]] = [values[idx]]
        else:
            results_dic[pet_labels[idx]]

    return results_dic
