for i in ["ftpd.lja", "ftpd.py"]:
    shutil.copyfile(i, path.join(root, "bin", i))
shutil.copyfile("ftp_serv.py", path.join(root, "..", "ftp_serv.py"))
shutil.copyfile("ftp_server.mpy", path.join(root, "lib", "ftp_server.mpy"))
