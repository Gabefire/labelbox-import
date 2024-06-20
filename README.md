# Populate Labelbox Workspace

These scripts are designed to populate a Labelbox Workspaces with public data for testing purposes.

## Regular Data Rows

The main script is `import.py` run this script and it will parse through the text files in the `files` folder. These files contain gs urls to publicly available assets. The name of the text files are the name of your Labelbox Dataset with the "_" replaced with a space.

## Geospatial Data Rows

The `import_tile.py` script is uses to import tile data. It does the same thing as the `import.py` script but uses the `files_tile` folder.
