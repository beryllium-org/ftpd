for i in ["ftpd.lja", "ftpd.py"]:
    shutil.copy(i, path.join(root, "bin", i))
shutil.copy("ftp_serv.py", path.join(root, "..", "ftp_serv.py"))
