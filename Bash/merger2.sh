#!/bin/bash

# Check if a directory is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 directory"
    exit 1
fi

# The directory to start the search from
BASE_DIR="$1"

# Function to traverse through directories and run cdo mergetime
process_directories() {
    local current_dir="$1"
    
    # Find all subdirectories and process them
    find "$current_dir" -type d | while read -r sub_dir; do
        # Check if there are .nc files in the current subdirectory
        nc_files=("$sub_dir"/*.nc)
        if [ -e "${nc_files[0]}" ]; then
            echo "Processing directory: $sub_dir"
            cd "$sub_dir" || exit
            cdo mergetime *.nc a.nc
            cd - || exit
        fi
    done
}

# Start processing from the base directory
process_directories "$BASE_DIR"
