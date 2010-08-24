#!/usr/bin/env python
"""
_Parentage_

Oracle implementation of Fileset.New

"""
__all__ = []
__revision__ = "$Id: New.py,v 1.3 2009/03/03 14:54:09 sfoulkes Exp $"
__version__ = "$Revision: 1.3 $"

from WMCore.WMBS.MySQL.Fileset.New import New as NewFilesetMySQL

class New(NewFilesetMySQL):
    sql = """INSERT INTO wmbs_fileset (id, name, last_update, open)
               VALUES (wmbs_fileset_SEQ.nextval, :NAME, :LAST_UPDATE, :OPEN)"""
