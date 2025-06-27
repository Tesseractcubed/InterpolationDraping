import pandas
import subprocess



def main ():
    ## Get file location (excel)
    ## Translate into python
    ## Translate to Inkscape svg standard
    ## Open and Save File ^
    ## Launch Inkscape w/ file
    return None

def importExcelFile(path):
    points_to_plot = pandas.read_excel(path, sheet_name=1)
    # This means sheet 2 (indexing) on the excel document should be the computer readable output.
    # This allows for the first page to be user facing, and a consistent output. May change to "ComputerOutput"
    return
def translateExcelToInkscape():
    return
def launchInkscapeFile(filePath):
    try:
        subprocess.run(["inkscape", filePath], check=True)
    except: subprocess.CalledProcessError
    return

main()