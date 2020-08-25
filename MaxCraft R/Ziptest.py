from zipfile import ZipFile

min_zip = "Hej.zip"

def get_txt(var):
    nu = str(var)[2:]
    return nu[:-1]
    

with ZipFile(min_zip, "r") as zip:
    hej = get_txt(zip.read("Hej.txt"))
    print(hej)
