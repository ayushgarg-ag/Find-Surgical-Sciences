import os

def get_patients_list():
    # Getting the current work directory (cwd)
    thisdir = os.path.dirname(os.getcwd()) + "/mmvt_root/mmvt_blend"

    # r=root, d=directories, f = files
    for r, d, f in os.walk(thisdir):
        folders = d
        break
        # for file in f:
        #     print(os.path.join(r, file))

    ignore_list = ['logs', 'color_maps', 'empty_subject', 'figures']
    patients = []
    for item in folders:
        if item not in ignore_list:
            patients.append(item)

    return patients

def readPrevIniFile(patient):
    thisdir = os.path.dirname(os.getcwd()) + "/mmvt_root/mmvt_blend/" + patient + "/config/calculate_meeg_casuality.ini"
    if(os.path.isfile(thisdir)):
        f = open(thisdir, "r")
        return f.read()
    else:
        return ""
    
def saveFileToPatient(info, patient):
    if (patient != ""):
        thisdir = os.path.dirname(os.getcwd()) + "/mmvt_root/mmvt_blend/" + \
        patient + "/config/calculate_meeg_casuality.ini"
    else:
        thisdir = "./calculate_meeg_casuality.ini"

    f = open(thisdir, "w")
    f.write(info)
    f.close()