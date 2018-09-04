from contextlib import contextmanager
import os
import tarfile
import errno

# from cdunn2001 on SO
@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)


# This hackery is needed because some files may have 0600 permissions or
# whatever and tarfile will break in this case
def extract_tar(path):
    tar = tarfile.open(path, 'r:gz', errorlevel=1)
    for file_ in tar:
        try:
            tar.extract(file_)
        except IOError as e:
            os.remove(file_.name)
            tar.extract(file_)
        finally:
            os.chmod(file_.name, file_.mode)
    tar.close()


# replaceable with a pathlib operation in later pythons but not in 3.4
def mkdir_uncaring(directory):
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
