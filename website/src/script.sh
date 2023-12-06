 #!/bin/bash

# Ustal ścieżkę do katalogu, w którym chcesz usunąć ZoneIdentifier
target_directory="themes"

# Przejdź do katalogu docelowego
cd "$target_directory" || exit

# Znajdź i usuń ZoneIdentifier dla wszystkich plików w katalogu
find . -type f -exec rm -r {} \;

echo "Usunięto ZoneIdentifier ze wszystkich plików w katalogu: $target_directory"
