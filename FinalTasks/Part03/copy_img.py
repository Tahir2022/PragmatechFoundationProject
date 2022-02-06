#Python vasitəsi ilə bir şəkli bir qovluqdan başqa qovluğa kopyalayan app yazaraq linkini qeyd edin

import shutil

original = r'C:\Users\Tahir PC\Desktop\Github\web1\Screenshot_2.png'
target = r'C:\Users\Tahir PC\Desktop\Github\Project\Screenshot_2.png'

shutil.copyfile(original, target)