import re

class VersionManager:
    @staticmethod
    def version_tuple(v):
        list_version = []
        for vmj in v.split('.'):
            list_d = re.findall('[0-9]+', vmj)
            list_version.extend(int(vmn) for vmn in list_d)
        return tuple(list_version)
