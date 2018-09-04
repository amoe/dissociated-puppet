from contextlib import contextmanager
import os
import tarfile

# from cdunn2001 on SO
@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)


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
