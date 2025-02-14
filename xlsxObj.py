#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# DESCRIPTION:
#
#   Read XLSX file

import pandas as pd

class xlsxObj:
    
    def __init__( self ) -> None:
        with open ( 'settings.yml' ) as FH:
            settings=yaml.safe_load(FH)
    
        self.workbook = pd.read_excel( settings['draping']['filename'])

