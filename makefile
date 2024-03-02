SHELL = bash
all:
	@echo -e "JPKG package builder.\n\nUsage:\n\tmake package\n\tmake clean"
update_modules:
	@echo "Updating git submodules from remotes.."
	@git submodule update --init --recursive --remote .
	@echo -e "Submodules ready\n\nMake sure to git commit before procceding to make!!"
modules:
	@echo "Preparing git submodules.."
	@git submodule update --init --recursive .
	@echo "Submodules ready"
package: modules
	@python3 -u scripts/make_lib.py
	@python3 -u scripts/generate_package.py
clean:
	@if [ -e "ftpd.jpk" ]; then rm ftpd.jpk; fi
	@if [ -e "./files/ftp_server.mpy" ]; then rm ./files/ftp_server.mpy; fi
