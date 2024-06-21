# Populate Labelbox Workspace

These scripts are designed to populate a Labelbox Workspaces with public data for testing purposes.

## Regular Data Rows

The main script is `import.py`. Run this script, and it will parse through the text files in the `files` folder. These files contain gs URLs to publicly available assets. The name of the text files is the name of your Labelbox Dataset, with the "_" replaced with a space.

## Geospatial Data Rows

The `import_tile.py` script imports tile data. It does the same thing as the `import.py` script but uses the `files_geospatial` folder.

## Workflow

A GitHub action workflow is created to populate your workspace through the cloud. Just fork this repo, add your Labelbox API key inside the repo secrets name `LABELBOX_API_KEY,` go to the Actions tab, click the workflow on the left-side panel, and select run on the top of the main panel.

<img width="1716" alt="Screenshot 2024-06-21 at 9 23 03 AM" src="https://github.com/Gabefire/labelbox-import/assets/33893811/15e94d94-4025-44c3-bf54-f10c8bce448c">
<img width="1728" alt="Screenshot 2024-06-21 at 9 22 18 AM" src="https://github.com/Gabefire/labelbox-import/assets/33893811/f805b552-2fbe-49d2-aaa1-ea9cae4d5266">
