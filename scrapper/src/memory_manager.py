from config import *
import os
import io
import cv2
import shutil
from PIL import Image
from utils import *

### RUNTIME PARAMETERS
category_product_limit = 100
img_limit = 2
category_label_number = 3
delimiter_total_count = 52

img_directory = directory + "img"
img_output_directory = output_directory + "img"


###

def make_directories():
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)


def copy_csv_files(input_path, destination_path):
    files = [shutil.copy(directory + f, output_directory + f) for f in os.listdir(directory) if
             os.path.isfile(directory + f) and f != "products.csv"]
    println("Files copied:" + str(files))


def reduce_product_list(input_path, destination_path, verbose=False):
    source_file = open(input_path, 'r')
    destination_file = open(destination_path, 'w')
    delimiter_counter = 0
    product_counter = 0
    reduced_product_counter = 0
    category_dict = {}
    reduced_category_dict = {}
    is_in_quotation = False
    is_to_copy = True
    to_copy = ""

    # skip first line
    while True:
        character = source_file.read(1)
        to_copy += character
        if character == '\n':
            break

    destination_file.write(to_copy)
    to_copy = ""

    while True:
        character = source_file.read(1)

        if not character:
            println("Reached EOF")
            break

        if character == ';' and is_in_quotation is False:
            delimiter_counter += 1
        elif character == '"':
            is_in_quotation = not is_in_quotation
        elif character == '\n':
            character = "<br><br>"

        to_copy += character

        if delimiter_counter == category_label_number:
            category = ""
            while True:
                character = source_file.read(1)
                to_copy += character
                if character == ';' and is_in_quotation is False:
                    delimiter_counter += 1
                    break
                category += character

            if category_dict.get(category) is not None:
                category_dict[category] = category_dict[category] + 1
                if category_dict[category] > category_product_limit:
                    is_to_copy = False
                else:
                    reduced_category_dict[category] = reduced_category_dict[category] + 1
            else:
                category_dict[category] = 1
                reduced_category_dict[category] = 1

        elif delimiter_counter == delimiter_total_count:
            delimiter_counter = 0
            product_counter += 1

            ### Scan until the end of the line
            while True:
                character = source_file.read(1)
                to_copy += character
                if not character or character == '\n':
                    break

            if is_to_copy is True:
                destination_file.write(to_copy)
                if verbose:
                    println("Copied product " + str(product_counter))
                reduced_product_counter += 1
            else:
                is_to_copy = True
                if verbose:
                    println("Skipped product " + str(product_counter))

            to_copy = ""

    source_file.close()
    destination_file.close()
    println("Total number of products: " + str(product_counter))
    println("Reduced number of products: " + str(reduced_product_counter))
    println("Initial category count:" + str(category_dict))
    println("Reduced category count:" + str(reduced_category_dict))


def reduce_image_list(input_path, destination_path, verbose=False):
    shutil.rmtree(img_output_directory)
    if not os.path.exists(img_output_directory):
        os.makedirs(img_output_directory)

    for product_catalog in os.listdir(input_path):
        img_count = 0
        if not os.path.exists(img_output_directory + "/" + product_catalog):
            os.makedirs(img_output_directory + "/" + product_catalog)

        imgs = os.listdir(input_path + "/" + product_catalog)
        if os.path.exists(input_path + "/" + product_catalog + "/listing.png"):
            shutil.copy(input_path + "/" + product_catalog + "/listing.png",
                        destination_path + "/" + product_catalog + "/listing.png")
            img_count += 1
            if verbose:
                println("Copied listing img of product " + product_catalog)
        for img in sorted(imgs, key=lambda x: os.stat(input_path + "/" + product_catalog + "/" + x).st_size):
            if img == "listing.png":
                pass
            elif img_count < img_limit:
                shutil.copy(input_path + "/" + product_catalog + "/" + img,
                            destination_path + "/" + product_catalog + "/" + img)
                if verbose:
                    println("Copied img " + str(img) + " of product " + product_catalog)
                img_count += 1


def semicolon_counter(path):
    source_file = open(path, 'r')
    is_in_quotation = False
    semicolon_count = 0
    to_copy = ""

    while True:
        character = source_file.read(1)
        to_copy += character

        if not character:
            break

        elif character == '"':
            is_in_quotation = not is_in_quotation

        elif character == ';':
            if not is_in_quotation:
                semicolon_count += 1

    println("Semicolon counter: " + str(semicolon_count))


make_directories()
copy_csv_files(directory, output_directory)
reduce_product_list(directory + "/products.csv", output_directory + "/products.csv")
reduce_image_list(img_directory, img_output_directory)
semicolon_counter(os.path.join(directory, "products.csv"))
semicolon_counter(os.path.join(output_directory, "products.csv"))
