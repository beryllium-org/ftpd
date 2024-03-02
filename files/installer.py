for pv[get_pid()]["filee"] in ["ftpd.lja", "ftpd.py"]:
    be.based.run("cp " + vr("filee") + " /bin/" + vr("filee"))
be.based.run("cp ftp_serv.py &/ftp_serv.py")

be.api.setvar("return", "0")
