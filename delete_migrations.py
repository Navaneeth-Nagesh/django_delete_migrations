import os
import shutil
import glob

rootDir = '.'

for root, dirs, files in os.walk(rootDir):
    for dir in dirs:
        if dir == '__pycache__':
            shutil.rmtree(os.path.join(root, dir))

        if dir == 'migrations':
            migration_files = [f for f in glob.glob(
                os.path.join(root) + '\migrations\**/*.py', recursive=True)]

            for file in migration_files:
                if not file.endswith('__init__.py'):
                    os.unlink(file)

print('Succesfully, deleted all the junk.')