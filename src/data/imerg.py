import os
import requests

def save_file(file, subdir):

    url = file

    file_name = file[78:78+66]
    file_path = f"{subdir}/{file_name}"

    result = requests.get(url)

    try:
        result.raise_for_status()
        f = open(file_path,'wb')
        f.write(result.content)
        f.close()
        # print('contents of URL written to '+file_path)
    except:
        print('requests.get() returned an error code '+str(result.status_code))

def get_files(file_path):

    with open(file_path) as f:
        files = f.readlines()[2:]

    files = [file.strip("\n") for file in files] # remove "\n"

    print(f'Number of files: {len(files)}')

    return files

def download_data(file_path, data_path, date_list):

    files = get_files(file_path)

    i = 0
    while(i<len(files)):

        print(f"File: {i}")

        file = files[i]

        file_name = file[78:78+66]

        file_date = file_name[23:23+8]
        date = f"{file_date[0:4]}-{file_date[4:6]}-{file_date[6:8]}"

        if date in date_list:

            sub_dir = f"{data_path}{date}"
            if not os.path.isdir(sub_dir):
                os.makedirs(sub_dir)

            save_file(file, sub_dir)
            i+=1
        else:
            i+=48