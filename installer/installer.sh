#!/bin/bash

# Nazwa pliku zip
zip_file="database.zip"
zip_file1="p.zip"

# Katalog docelowy
target_directory="../website/"
target_directory1="../website/src/img/"

# Sprawdź, czy plik zip istnieje
if [ -e "$zip_file" ]; then
    # Rozpakuj plik zip do folderu tymczasowego
    temp_dir=$(mktemp -d)
    unzip "$zip_file" -d "$temp_dir"

    # Przenieś rozpakowany folder do katalogu docelowego
    mv "$temp_dir/database" "$target_directory"

    # Usuń katalog tymczasowy
    rm -r "$temp_dir"

    echo "Rozpakowano i przeniesiono zawartość $zip_file do $target_directory"
else
    echo "Plik $zip_file nie istnieje."
fi

# Sprawdź, czy plik zip istnieje
if [ -e "$zip_file1" ]; then
    # Rozpakuj plik zip do folderu tymczasowego
    temp_dir=$(mktemp -d)
    unzip "$zip_file1" -d "$temp_dir"

	# Usuń stary katalog katalog
	rm -rf "$target_directory1/p"
	
    # Przenieś rozpakowany folder do katalogu docelowego
    mv "$temp_dir/p" "$target_directory1"

    # Usuń katalog tymczasowy
    rm -r "$temp_dir"

    echo "Rozpakowano i przeniesiono zawartość $zip_file1 do $target_directory1"
else
    echo "Plik $zip_file1 nie istnieje."
fi
