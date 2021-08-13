import subprocess, os

# check that a recent version of Android is being used
# as this affects the uninstall command used
recentVersion = input("Are you using a recent version of Android (~2015 or later)? [Y]es or [n]o: ").lower() in ['y', 'yes', '']

# get the package list
list_command="adb.exe shell pm list packages"
result = subprocess.check_output(list_command, shell=True).decode()

# process the list
names = [i.strip() for i in result.strip().split('\n') if i.strip() != '']
packages = [i.split(':')[1] for i in names]

# print out the lsit of packages
print('\n'.join(packages))

# iterate over the packages
for name in packages:

    # assume there is no confirmation
    confirmation = False

    prompt = ""

    while not confirmation:
        prompt = input(f"\nUninstalling {name}. [C]ontinue, [s]kip, or [a]bort? ") # find out what the user wants to do
        confirmation = (input("Are you sure? [Y]es or [n]o: ").lower() in ['y', 'yes', '']) # ask them to confirm

    # if they chose to skip, continue to the next iteration
    if prompt.lower() in ['s', 'skip', '']:
        continue

    # if they chose to abort, exit the script
    elif prompt.lower() in ['a', 'abort']:
        break

    # if they chose to continue, uninstall the package
    elif prompt.lower() in ['c', 'continue']:
        if recentVersion:
            os.system(f"adb.exe shell pm uninstall -k --user 0 {name}")
        
        else:
            os.system(f"adb.exe shell pm block {name}")
