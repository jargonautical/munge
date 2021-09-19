def catalogue_files(dir_name):
    import os
    import platform
    from datetime import datetime
    #dir_name = './app_dev/dot'
    
    def creation_date(path_to_file):
        """
        Try to get the date that a file was created, falling back to when it was
        last modified if that isn't possible.
        See http://stackoverflow.com/a/39501288/1709587 for explanation.
        """
        if platform.system() == 'Windows':
            return os.path.getctime(path_to_file)
        else:
            stat = os.stat(path_to_file)
            try:
                return stat.st_birthtime
            except AttributeError:
                # We're probably on Linux. No easy way to get creation dates here,
                # so we'll settle for when its content was last modified.
                return stat.st_mtime

    # Get list of all files only in the given directory
    list_of_files = filter( lambda x: os.path.isfile(os.path.join(dir_name, x)),
                           os.listdir(dir_name) )
    # Create a list of files in directory along with the size
    files_with_size = [ (file_name, os.stat(os.path.join(dir_name, file_name)).st_size, creation_date(os.path.join(dir_name, file_name)))
                       for file_name in list_of_files  ]
    # Iterate over list of files along with size 
    # and print them one by one.
    for file_name, size, stamp in files_with_size:
        newStamp = datetime.fromtimestamp(stamp).strftime('%Y-%m-%d-%HH:%mm') # yyyy-MM-dd HH:mm:ss
        print(size, file_name, stamp, newStamp) 
        
catalogue_files('./')
