# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
#END_HEADER


class AD_VINA:
    '''
    Module Name:
    AD_VINA

    Module Description:
    A KBase module: AD_VINA
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/asedova/AD_VINA.git"
    GIT_COMMIT_HASH = "2b6d986bb8634f474d18249f40e393ced89a786a"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        #END_CONSTRUCTOR
        pass


    def ad_vina(self, ctx, inparams):
        """
        :param inparams: instance of type "InParams" -> structure: parameter
           "receptor" of String, parameter "ligand" of String, parameter
           "center" of String, parameter "size" of String
        :returns: instance of type "OutParams" -> structure: parameter
           "outname" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN ad_vina
        (cx, cy, cz)=map(lambda x: float(x), inparams["center"].split(','))
        (sx, sy, sz)=map(lambda x: float(x), inparams["size"].split(','))
        com="/autodock_vina_1_1_2_linux_x86/bin/vina --receptor %s --ligand %s --cpu 4 --center_x %f --center_y %f  --center_z %f --size_x %f --size_y %f --size_z %f --out %s" % (inparams["receptor"], inparams["ligand"], cx, cy, cz, sx, sy, sz, inparams["outname"])
        print(com+"\n")
        os.system(com)
        output = {}
#        print(com)
        #END ad_vina

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method ad_vina return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
