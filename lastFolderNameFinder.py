class FilterModule():

    def lastFolderNameFinder(self, path):
        folderName = path.split('/')
        return folderName[-1]
