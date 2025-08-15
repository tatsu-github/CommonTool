# 正規表現を使ってパスの一部を置換
import re
ver = re.compile('v\d\d\d\d')
path = 'hoge/hoge/hoge.v0001.%04d.exr'
new_path = ver.sub('v0002', path)
# >>Result: hoge/hoge/hoge.v0002.%04d.exr

# Get import module path
import mymodule
mymodule.__file__

# Relative Module Import
import importlib
package_name = __package__
module = importlib.import_module(package_name)
my_module_name = getattr(module, 'my_module_name')  # from __package__ import dino_change_permission

# Get directory existence and create if not exist
import os
path = 'SERVER/project/ep01/sq01/s01/maya/cache'
if not os.path.exists(path):
    os.makedirs(path)

# set GUI position to monitor center
self.desktop = QtGui.qApp.desktop()
screen_number = self.desktop.screenNumber( QtGui.QCursor().pos() )
self.resize(400, 200)
screen = QtWidgets.QDesktopWidget().screenGeometry(screen_number)
self.move(screen.center()-self.frameGeometry().center())

# calculate motion blur length from shutter angle
# shoot_fps for High Speed camera
length = (shutter_angle / 360.0) * (plate_fps / shoot_fps)

# Return v#### to V####+1
def get_up_ver():
    cur_file_name = self.filename_le.text()
    pattern = '.*?(_v(\d+)).*'  # set search pattern _v####
    get_ver = re.search(pattern, cur_file_name)  # get _v####
    
    if get_ver:
        cur_ver_number = int(get_ver.group(2))  # pick number from _v####
        new_ver_number = cur_ver_number + 1
        new_ver_str = str(new_ver_number).zfill(len(get_ver.group(2)))
        new_file_name = re.sub(r'(_v\d+)', '_v{}'.format(new_ver_str), cur_file_name)
        self.filename_le.setText(new_file_name)  # update UI file name to up version
        return True
    else:
        print('This file name has no version number')
        return False
