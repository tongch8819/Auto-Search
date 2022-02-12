import platform
import os, re
import argparse


def get_platform():
    """
    Call platform.platform() API 
    - return: platform keyword
    """
    rst = platform.platform().split('-')[0]

    # determine value of rst, which is platform keyword
    if rst == "":
        rst = git_bash()
    return rst

def git_bash():
    """
    platform.platform() API does not work on git-bash-windows
    - return: Windows if run on git-bash-windows
    """
    path = os.popen("which bash")
    description = os.popen("file " + path)
    print(description)
    regex = re.compile("windows")
    obj = re.match(description, flags=re.IGNORECASE)
    if obj is not None:
        return "Windows"
    else:
        return "Unknown"
    
    
platform_dict = {
    "Windows": ("Windows", ),
    "MacOS": ("Darwin", "macOS"),
    "Linux": ("Linux", ),
}


def main():
    """
    Test passed on: 
        - windows powershell, 
        - windows cmd
        - windows git bash
        - macOS iterm
        - ubuntu terminal
    - return: platform_dict.values, i.e. Windows, Darwin, Linux 
    """
    rst = get_platform()
    print("Current platform: %s" % rst)


if __name__ == "__main__":
    main()