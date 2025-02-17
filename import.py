import labelbox as lb
import os

API_KEY = None

data_rows = []

for file_name in os.listdir("./files"):
    try:
        with open(f"./files/{file_name}", "r") as file:
            for i, line in enumerate(file.readlines()):
                if i > 2_000_000:
                    break
                if not line:
                    continue
                file_path = line[5:].rstrip()
                full_file = "https://storage.googleapis.com/" + file_path
                data_rows.append({
                    "row_data": full_file,
                    "global_key": file_path,
                })

        client = lb.Client(API_KEY)

        dataset = client.create_dataset(name=file_name.replace("_", " ").rstrip("\.txt"), iam_integration=None)

        task = dataset.create_data_rows(data_rows)
        task.wait_till_done()

        print(task.errors)
    except:
        continue