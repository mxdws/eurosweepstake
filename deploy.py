import time, requests, os, sys, shutil, json
from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader

def removeSite():
    outputFolder = 'site'
    if os.path.exists(outputFolder):
        shutil.rmtree(outputFolder)

def copyAssets():
    outputFolder = 'site'
    assetSource = 'assets'
    assetTarget = 'assets'

    assetSourcePath = f"./{assetSource}"
    assetTargetPath = f"./{outputFolder}/{assetTarget}"

    if os.path.isdir(assetSource):
        # os.makedirs(assetTargetPath, exist_ok=True)  # Force the creation of the target folder
        shutil.copytree(assetSourcePath, assetTargetPath)
        print(f"Assets copied to the {assetTargetPath} folder")
    else:
        print(f"Assets source folder does not exist: {assetSource}")

def genDrawPages():
    # Get the Sweepstake Results

    dataFile = './sweepstake.json'
    with open(dataFile,'r') as f:
        sweepResults = json.load(f)

    templateFolder = './templates'
    templateFile = "page.html"
    outputFolder = 'site'

    # Create a Page for each drawn person in a for loop

    # Initialise Jinja2
    file_loader = FileSystemLoader(templateFolder)
    env = Environment(loader=file_loader)

    title="Euro2020 - Family Sweepstake"
    description="The results of the Euro2020 Family Sweepstake"

    for s in sweepResults:
        drawNumber = (sweepResults.index(s))+1

        # print(s)

        # Render with Jinja2
        targetTemplate = env.get_template(templateFile)
        targetHTML = targetTemplate.render(title=title, description=description, sweepResults=s)
        targetPath = f"./{outputFolder}/draw/{drawNumber}"

        # Write the file to the output folder
        targetFile = f"{targetPath}/index.html"
        os.makedirs(targetPath, exist_ok=True)  # Force the creation of the target folder
        with open(targetFile, 'w') as file:
            file.write(targetHTML)

    print("Draw pages generated for Family Sweepstake")


def genHome():
    dataFile = './sweepstake.json'

    with open(dataFile,'r') as f:
        sweepResults = json.load(f)

    templateFolder = './templates'
    templateFile = "home.html"
    outputFolder = 'site'

    # Create a Page for each drawn person in a for loop

    # Initialise Jinja2
    file_loader = FileSystemLoader(templateFolder)
    env = Environment(loader=file_loader)

    title="Euro2020 - Family Sweepstake"
    description="The results of the Euro2020 Family Sweepstake"

    # Render with Jinja2
    targetTemplate = env.get_template(templateFile)
    targetHTML = targetTemplate.render(title=title, description=description, sweepResults=sweepResults)
    targetPath = f"./{outputFolder}"

    # Write the file to the output folder
    targetFile = f"{targetPath}/index.html"
    os.makedirs(targetPath, exist_ok=True)  # Force the creation of the target folder
    with open(targetFile, 'w') as file:
        file.write(targetHTML)

    print("Homepage generated for Family Sweepstake")

def genDraw():
    templateFolder = './templates'
    templateFile = "draw.html"
    outputFolder = 'site'

    # Create a Page for each drawn person in a for loop

    # Initialise Jinja2
    file_loader = FileSystemLoader(templateFolder)
    env = Environment(loader=file_loader)

    title="Euro2020 - Family Sweepstake"
    description="The results of the Euro2020 Family Sweepstake"

    # Render with Jinja2
    targetTemplate = env.get_template(templateFile)
    targetHTML = targetTemplate.render(title=title, description=description)
    targetPath = f"./{outputFolder}/draw"

    # Write the file to the output folder
    targetFile = f"{targetPath}/index.html"
    os.makedirs(targetPath, exist_ok=True)  # Force the creation of the target folder
    with open(targetFile, 'w') as file:
        file.write(targetHTML)

    print("Homepage generated for Family Sweepstake")

removeSite()
genHome()
genDrawPages()
genDraw()
copyAssets()