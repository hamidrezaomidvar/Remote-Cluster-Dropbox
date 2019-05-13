# Remote to Dropbox

The aim of this project is to convert a remote folder to a Dropbox folder. 

It is python base, and uses [this](https://github.com/andreafabrizi/Dropbox-Uploader) to transfer files to the Dropbox folder. 

# Some considereations
- If you are copying or moving (`cp`, `mv`) large files to the target folder, make sure the script is run on the same machine as the process of copying/moving. Otherwise, you would get to some problems in syincing the copied file.
