import os
fichier = open("/tmp/monfichier.txt","w")
def files_in_dir(odir) :
    res = os.listdir(odir)
    for f in res :
        new_path = os.path.join(odir + "/" + f)
        if os.path.isfile(new_path)== True :
            objtype = "file"
        else :
            if os.path.isdir(new_path)==True :
                objtype = "directory"
            else :
                objtype = "other"
        print (new_path, objtype)
        st = new_path + ";" + objtype
        st = st + '\n'
        fichier.write(st)
        if objtype == "directory" :
            files_in_dir(new_path)
        


path = "/etc/systemd"
path = os.path.join(path)
files_in_dir(path)

fichier.close()
