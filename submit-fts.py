import sys
import os
import json
import copy
import random
import string


job_template = {"files": []}

file_template = {"sources": [], "destinations": [], "metadata": {"request_id": "8d2776414a7847b59f2cc8fb524aa167", "scope": "cms", "name": "", "activity": "Data Challenge", "request_type": "TRANSFER", "src_type": "DISK", "dst_type": "DISK", "src_rse": "T2_US_UCSD", "dst_rse": "T2_US_Caltech", "filesize": 1073741824, "adler32": "c02d0001"}, "checksum": "UPDATE"}

#"src_rse_id": "087ee3383b9d45f6b31814af07b2c56d", "dest_rse_id": "d722087822d3481cb1a441ab9d6034dc",

def getRandomName():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(15))

def submittofts(allfiles, outname):
    fileList = []
    with open(allfiles, 'r') as fd:
        fileList = fd.readlines()
    for fline in fileList:
        # need /store/file ADLER32
        fline = fline.strip()
        sourceurl = f"davs://xrootd-sense-ucsd-redirector.sdsc.optiputer.net:1094/{fline}"
        desturl = f"davs://sense-redir-01.ultralight.org:1094/store/user/jbalcas/{getRandomName()}"
        tmpTmpl = copy.deepcopy(file_template)
        tmpTmpl['sources'].append(sourceurl)
        tmpTmpl['destinations'].append(desturl)
        tmpTmpl['checksum'] = 'ADLER32:c02d0001'
        tmpTmpl['metadata']['name'] = fline
        job_template['files'].append(tmpTmpl)
        with open(f'bulk-out-{outname}.json', 'w') as fd:
            json.dump(job_template, fd)

if __name__ == "__main__":
    submittofts(sys.argv[1], sys.argv[2])
