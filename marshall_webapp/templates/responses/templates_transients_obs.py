#!/usr/local/bin/python
# encoding: utf-8
"""
*The HTML template module for the `templates_transients_obs.py` resource*

:Author:
    David Young
"""
from builtins import str
from builtins import object
import sys
import os
import khufu
from marshall_webapp.models.transients_obs import models_transients_obs_get

class templates_transients_obs(object):
    """
    The worker class for the templates_transients_obs module

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``elementId`` -- the specific element requested (or False)
    
    """

    def __init__(
        self,
        log,
        request,
        elementId=False
    ):
        self.log = log
        self.request = request
        self.elementId = elementId
        # xt-self-arg-tmpx

        log.debug("instansiating a new 'templates_transients_obs' object")

        return None

    def get(self):
        """get the templates_transients_obs object

        **Return**

        - ``filename``
        - ``obText``
        
        """
        self.log.debug('starting the ``get`` method')

        # get info needed from database
        transients_obs = models_transients_obs_get(
            log=self.log,
            request=self.request,
            elementId=self.elementId
        )
        transient_ob_data = transients_obs.get()

        # download filename and data for OB
        filename, obText = self._generate_ob_text(
            transient_ob_data=transient_ob_data
        )

        self.log.debug('completed the ``get`` method')
        return filename, obText

    def _generate_ob_text(
            self,
            transient_ob_data):
        """ generate ob text

        **Key Arguments**

        - ``transient_ob_data``
        

        **Return**

        - ``downloadFilename``
        - ``obText``
        
        """
        self.log.debug('starting the ``_generate_ob_text`` method')

        od = {}  # override dictionary

        # UNPACK DICTIONARY VALUES TO LOCAL()
        for arg, val in list(transient_ob_data.items()):
            varname = arg
            if isinstance(val, ("".__class__, u"".__class__)):
                exec(varname + ' = """%s""" ' % (val,))
            else:
                exec(varname + " = %s" % (val,))
            self.log.debug('%s = %s' % (varname, val,))

        # instrument
        if "efos" in instrument:
            od["b4_instrument"] = "EFOSC2"
        else:
            od["b4_instrument"] = "SOFI"

        if "spec" in spectrumOrImage:
            od["b5_ACQUISITION.TEMPLATE.NAME"] = "EFOSC_img_acq_MoveToSlit"
            od["b6_TEMPLATE.NAME"] = "EFOSC_spec_obs_Spectrum"
        else:
            od["b5_ACQUISITION.TEMPLATE.NAME"] = "EFOSC_img_acq_MoveToPixel"
            od["b6_TEMPLATE.NAME"] = "EFOSC_img_obs_Image"

        currentMag = float(currentMag)
        od["b2_ra"] = ra
        od["b2_dec"] = dec
        od["b2_TARGET.NAME"] = objectName
        od["b2_objectClass"] = objectClass
        od["b6_INS.GRIS1.NAME"] = "Gr#%(grism)s" % locals()

        filename = """spec_v_"""
        # SEEING
        if badSeeing is not False:
            od["b5_INS.SLIT1.NAME"] = "slit#1.5"
        else:
            od["b5_INS.SLIT1.NAME"] = "slit#1.0"
        od["b6_INS.SLIT1.NAME"] = od["b5_INS.SLIT1.NAME"]

        # DEFINE VALUES FROM CURRENT OBJECT MAGNITUDE
        if currentMag < 13.0:
            # very bright objects (V<13) => t = 40 s (V=12 => S/N~180)
            od["b1_userComments"] = "targets: V < 13"
            od["b6_DET.WIN1.UIT1"] = 40
            od["b5_DET.WIN1.UIT1"] = 1
            filename = """%(filename)sbrighter__13_0""" % locals()

        elif currentMag < 14.5:
            # bright sources (13 < V < 14.5) => t = 120 s (V=14 => S/N~120)
            od["b1_userComments"] = "targets: 13 < V < 14.5"
            od["b6_DET.WIN1.UIT1"] = 120
            od["b5_DET.WIN1.UIT1"] = 3
            filename = """%(filename)s13p0_14p5""" % locals()
        elif currentMag < 16.0:
            # relatively bright sources (14.5 < V < 16) => t = 180 s (V=15.5=>
            # S/N~70)
            od["b1_userComments"] = "targets: 14.5 < V < 16"
            od["b6_DET.WIN1.UIT1"] = 180
            od["b5_DET.WIN1.UIT1"] = 5
            filename = """%(filename)s14p5_16p0""" % locals()
        elif currentMag < 17.5:
            # intermediate mag. sources (16 < V < 17.5) => t = 300 s (V=17 =>
            # S/N~45)
            od["b1_userComments"] = "targets: 16 < V < 17.5"
            od["b6_DET.WIN1.UIT1"] = 300
            od["b5_DET.WIN1.UIT1"] = 10
            filename = """%(filename)s16p0_17p5""" % locals()
        elif currentMag < 18.5:
            # faintish sources (17.5 < V < 18.5) => t = 600 s (V=18 => S/N~35)
            od["b1_userComments"] = "targets: 17.5 < V < 18.5"
            od["b6_DET.WIN1.UIT1"] = 600
            od["b5_DET.WIN1.UIT1"] = 20
            filename = """%(filename)s17p5_18p5""" % locals()
        elif currentMag < 19.5:
            # faint sources (18.5 < V < 19.5) => t = 900 s (V=19 => S/N~25)
            od["b1_userComments"] = "targets: 18.5 < V < 19.5"
            od["b6_DET.WIN1.UIT1"] = 900
            od["b5_DET.WIN1.UIT1"] = 30
            filename = """%(filename)s18p5_19p5""" % locals()
        elif currentMag < 20.5:
            # very faint sources (19.5 < V < 20.5) => t = 1500 s (V=20 =>
            # S/N~15)
            od["b1_userComments"] = "targets: 19.5 < V < 20.5"
            od["b6_DET.WIN1.UIT1"] = 1500
            od["b5_DET.WIN1.UIT1"] = 40
            filename = """%(filename)sfainter_19p5""" % locals()
        elif currentMag > 20.5:
            obText = "object too faint"
            return None, None
        else:
            obText = "object too faint"
            return None, None

        filename = """%(filename)s_cls_g%(grism)s_s""" % locals()
        if badSeeing is not False:
            filename = """%(filename)s1p5""" % locals()
        else:
            filename = """%(filename)s1""" % locals()

        nameForFilename = objectName.replace("-", "")

        od["b1_name"] = "class_" + nameForFilename[0:23]
        od["b4_OBSERVATION.DESCRIPTION.NAME"] = filename

        filename = nameForFilename[0:15] + "_%(filename)s" % locals()
        downloadFilename = "%(filename)s.obx" % locals()

        # VARIABLES
        obText = ""
        obDictionary = {}

        obDictionary["b1_IMPEX.VERSION"] = "2.0"
        obDictionary["b1_type"] = "O"
        obDictionary["b1_STTimeIntervals"] = ""
        obDictionary["b1_calibrationReq"] = ""
        obDictionary["b1_InstrumentComments"] = ""
        # 'targets: 17.5 < V < 18.5'
        obDictionary["b1_userComments"] = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        obDictionary["b1_userPriority"] = "1"
        obDictionary["b1_LineNumber"] = "0"
        # of the form Spec_V_18_5__19_5_class_g13_s1
        obDictionary["b1_name"] = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

        obDictionary["b2_comments"] = ""
        # SN | STD
        obDictionary["b2_objectClass"] = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        obDictionary["b2_ra"] = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # sexegesimal
        obDictionary["b2_dec"] = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # sexegesimal
        obDictionary["b2_epoch"] = "2000.0"
        obDictionary["b2_equinox"] = "2000.0"
        obDictionary["b2_propDec"] = "0.000000"
        obDictionary["b2_propRA"] = "0.000000"
        obDictionary["b2_diffRA"] = "0.000000"
        obDictionary["b2_diffDec"] = "0.000000"
        obDictionary["b2_LineNumber"] = "0"
        # object name
        obDictionary["b2_TARGET.NAME"] = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

        obDictionary["b3_air_mass"] = "5.0"
        obDictionary["b3_fractional_lunar_illumination"] = "1.0"
        obDictionary["b3_sky_transparency"] = "Variable, thick cirrus"
        obDictionary["b3_moon_angular_distance"] = "30"
        obDictionary["b3_seeing"] = "1.5"
        obDictionary["b3_StrehlRatio"] = "0.0"
        obDictionary["b3_CONSTRAINT.SET.NAME"] = "No Name"

        obDictionary["b4_longDescription"] = ""
        obDictionary["b4_IPVersion"] = "89.01"
        obDictionary["b4_instrument"] = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        obDictionary["b4_LineNumber"] = "0"
        obDictionary[
            "b4_OBSERVATION.DESCRIPTION.NAME"] = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # same as 'name' in block one (name to be found in the headers of FITS files)

        # 'EFOSC_img_acq_MoveToSlit' | ????
        obDictionary[
            "b5_ACQUISITION.TEMPLATE.NAME"] = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # should be moveToSlit (EFOSC_img_acq_MoveToSlit) and photometry movetopixel
        obDictionary["b5_DET.READ.SPEED"] = "normal"
        obDictionary["b5_DET.WIN1.UIT1"] = "20"
        obDictionary["b5_DET.WIN1.BINX"] = "2"
        obDictionary["b5_DET.WIN1.BINY"] = "2"
        obDictionary["b5_DET.PIXEL.X"] = "1100"
        obDictionary["b5_TEL.ROT.OFFANGLE"] = "-9999"
        obDictionary["b5_TEL.COMBINED.OFFSET"] = "T"
        obDictionary["b5_TEL.FOCUS"] = "F"
        obDictionary["b5_TEL.PRESET.NEW"] = "T"
        obDictionary["b5_INS.FILT1.NAME"] = "V#641"
        # slit#1.0
        obDictionary["b5_INS.SLIT1.NAME"] = "xxxxxxxxxxxxxxxxxxxxxxxx"

        # 'EFOSC_spec_obs_Spectrum' | ???
        obDictionary["b6_TEMPLATE.NAME"] = "xxxxxxxxxxxxxxxxxxxxxxxx"
        obDictionary["b6_DET.READ.SPEED"] = "normal"
        # exposure time
        obDictionary["b6_DET.WIN1.UIT1"] = "xxxxxxxxxxxxxxxxxxxxxxxxx"
        obDictionary["b6_DET.WIN1.ST"] = "F"
        obDictionary["b6_DET.WIN1.STRX"] = "1"
        obDictionary["b6_DET.WIN1.STRY"] = "1"
        obDictionary["b6_DET.WIN1.NX"] = "2048"
        obDictionary["b6_DET.WIN1.NY"] = "2048"
        obDictionary["b6_DET.WIN1.BINX"] = "2"
        obDictionary["b6_DET.WIN1.BINY"] = "2"
        obDictionary["b6_SEQ.NEXPO"] = "1"
        obDictionary["b6_INS.FILT1.NAME"] = "Free"
        obDictionary[
            "b6_INS.GRIS1.NAME"] = "xxxxxxxxxxxxxxxxxxxxxxxxx"  # Gr#13
        # slit#1.0
        obDictionary["b6_INS.SLIT1.NAME"] = "xxxxxxxxxxxxxxxxxxxxxxxxx"
        obDictionary["b6_DPR.TYPE"] = "OBJECT"

        # override default values with user values
        for k, v in list(od.items()):
            obDictionary[k] = v

        block1 = [
            "b1_IMPEX.VERSION",
            "b1_type",
            "b1_STTimeIntervals",
            "b1_calibrationReq",
            "b1_InstrumentComments",
            "b1_userComments",
            "b1_userPriority",
            "b1_LineNumber",
            "b1_name",
        ]

        block2 = [
            "b2_comments",
            "b2_objectClass",
            "b2_ra",
            "b2_dec",
            "b2_epoch",
            "b2_equinox",
            "b2_propDec",
            "b2_propRA",
            "b2_diffRA",
            "b2_diffDec",
            "b2_LineNumber",
            "b2_TARGET.NAME",
        ]

        block3 = [
            "b3_air_mass",
            "b3_fractional_lunar_illumination",
            "b3_sky_transparency",
            "b3_moon_angular_distance",
            "b3_seeing",
            "b3_StrehlRatio",
            "b3_CONSTRAINT.SET.NAME",
        ]

        block4 = [
            "b4_longDescription",
            "b4_IPVersion",
            "b4_instrument",
            "b4_LineNumber",
            "b4_OBSERVATION.DESCRIPTION.NAME",
        ]

        block5 = [
            "b5_ACQUISITION.TEMPLATE.NAME",
            "b5_DET.READ.SPEED",
            "b5_DET.WIN1.UIT1",
            "b5_DET.WIN1.BINX",
            "b5_DET.WIN1.BINY",
            "b5_DET.PIXEL.X",
            "b5_TEL.ROT.OFFANGLE",
            "b5_TEL.COMBINED.OFFSET",
            "b5_TEL.FOCUS",
            "b5_TEL.PRESET.NEW",
            "b5_INS.FILT1.NAME",
            "b5_INS.SLIT1.NAME",
        ]

        block6 = [
            "b6_TEMPLATE.NAME",
            "b6_DET.READ.SPEED",
            "b6_DET.WIN1.UIT1",
            "b6_DET.WIN1.ST",
            "b6_DET.WIN1.STRX",
            "b6_DET.WIN1.STRY",
            "b6_DET.WIN1.NX",
            "b6_DET.WIN1.NY",
            "b6_DET.WIN1.BINX",
            "b6_DET.WIN1.BINY",
            "b6_SEQ.NEXPO",
            "b6_INS.FILT1.NAME",
            "b6_INS.GRIS1.NAME",
            "b6_INS.SLIT1.NAME",
            "b6_DPR.TYPE",
        ]

        blocks = [block1, block2, block3, block4, block5, block6]

        for block in blocks:
            for key in block:
                printKey = str(key)[3:].ljust(40)
                value = obDictionary[key]
                value = '"%(value)s"' % locals()

                obText = "%(obText)s%(printKey)s%(value)s\n" % locals()
            obText = "%(obText)s\n\n" % locals()

        self.log.debug('completed the ``_generate_ob_text`` method')
        return downloadFilename, obText

    # xt-class-method
