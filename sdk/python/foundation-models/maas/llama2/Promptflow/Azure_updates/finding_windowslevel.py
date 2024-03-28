from promptflow import tool
import subprocess


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def azure_version():
    process = subprocess.run(["pip", "list"], capture_output=True)
    output = process.stdout.decode()

    # Filter for the specific package and extract version
    for line in output.splitlines():
        if package_name in line:
            version = line.split()[1]
            return f"Azure SDK package '{package_name}' version: {version}"
            break

