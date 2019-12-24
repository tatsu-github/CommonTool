# Get import module path
import mymodule
mymodule.__file__

# Get directory existence and create if not exist
import os
path = 'SERVER/project/ep01/sq01/s01/maya/cache'
if os.path.exists(path) == 0:
    os.makedirs(path)
