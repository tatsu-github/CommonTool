# 正規表現を使ってパスの一部を置換
import re
ver = re.compile('v\d\d\d\d')
path = 'hoge/hoge/hoge.v0001.%04d.exr'
new_path = ver.sub('v0002', path)
# >>Result: hoge/hoge/hoge.v0002.%04d.exr

# Get import module path
import mymodule
mymodule.__file__

# Get directory existence and create if not exist
import os
path = 'SERVER/project/ep01/sq01/s01/maya/cache'
if os.path.exists(path) == 0:
    os.makedirs(path)

# set GUI position monitor center
self.desktop = QtGui.qApp.desktop()
screen_number = self.desktop.screenNumber( QtGui.QCursor().pos() )
self.resize(400, 200)
screen = QtWidgets.QDesktopWidget().screenGeometry(screen_number)
self.move(screen.center()-self.frameGeometry().center())
