import os


def _check_cache(cache):
    """Check the cache folder directory exists

    Parameters
    ----------
    cache : str
        Folder directory of local cache location.

    Returns
    -------
    str
        Updated cache if not already specified.
    """
    if not os.path.isdir(cache):
        print("Creating new cache in current directory.")
        os.mkdir("CACHE")
        cache = os.path.join(os.getcwd(), "CACHE")
    return cache
