
# adapted from: https://gist.github.com/Athena75/b7ef6febcb942446c4930ca894b0d8b9
import os
import tqdm
import requests
import zipfile

def get_file_dir_name(url):
    file_name = url.split('/')[-1]
    dir_name = file_name.split('.')[0]

    return file_name, dir_name


def download_zip(url, target_file):
    # download (large) zip file
    # for large https request on stream mode to avoid out of memory issues
    # see : http://masnun.com/2016/09/18/python-using-the-requests-module-to-download-large-files-efficiently.html
    print("Downloading zip file")

    response = requests.get(url, stream=True)
    handle = open(target_file, "wb")
    # read chunk by chunk
    for chunk in tqdm.tqdm(response.iter_content(chunk_size=512), desc='Downloading '):
        if chunk:  
            handle.write(chunk)
    handle.close()  
    print("Download complete")


def fetch_data(url, delete_zip=False):
    target_file, target_dir = get_file_dir_name(url)

    # check if dataset already downloaded
    if os.path.isfile(target_file):
        print("datasets already exists")
        return

    download_zip(url, target_file)

    return target_file, target_dir


def cleanup_data(target_file):
    # delete zip_file
    print("Deleting {} ".format(target_file))
    
    os.remove(path=target_file)


def extract_data(target_file, target_dir, delete_zip=False):

    if not target_file:
        return

    # extract zip_file
    print("Extracting {} ".format(target_file))

    with zipfile.ZipFile(target_file) as zf:
        for member in tqdm.tqdm(zf.infolist(), desc='Extracting '):
            try:
                zf.extract(member, path=target_dir)
            except zipfile.error as e:
                pass
    
    if delete_zip:
        cleanup_data(target_file)




if __name__ == "__main__":
    URL = "https://service.unece.org/trade/locode/loc212csv.zip"

    target_file, target_dir = fetch_data(url=URL)
    extract_data(target_file, target_dir, delete_zip=True)