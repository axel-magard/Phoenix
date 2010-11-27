#---------------------------------------------------------------------------
# Name:        etg/display.py
# Author:      Robin Dunn
#
# Created:     
# Copyright:   (c) 2010 by Total Control Software
# License:     wxWindows License
#---------------------------------------------------------------------------

import etgtools
import etgtools.tweaker_tools as tools

PACKAGE   = "wx"   
MODULE    = "_core"
NAME      = "display"   # Base name of the file to generate to for this script
DOCSTRING = ""

# The classes and/or the basename of the Doxygen XML files to be processed by
# this script. 
ITEMS  = [ 'wxDisplay', ]    

#---------------------------------------------------------------------------

def run():
    # Parse the XML file(s) building a collection of Extractor objects
    module = etgtools.ModuleDef(PACKAGE, MODULE, NAME, DOCSTRING)
    etgtools.parseDoxyXML(module, ITEMS)
    
    #-----------------------------------------------------------------
    # Tweak the parsed meta objects in the module object as needed for
    # customizing the generated code and docstrings.
    
    module.addHeaderCode("#include <wx/display.h>")
    
    c = module.find('wxDisplay')
    assert isinstance(c, etgtools.ClassDef)
    c.addPrivateAssignOp()
    c.addPrivateCopyCtor()
    
    # TODO: SIP needs to know about wxArrayVideoModes before we can enable this
    c.find('GetModes').ignore()
    
    c.addProperty('ClientArea GetClientArea')
    c.addProperty('CurrentMode GetCurrentMode')
    c.addProperty('Geometry GetGeometry')
    c.addProperty('Name GetName')
    
    
    #-----------------------------------------------------------------
    tools.ignoreAssignmentOperators(module)
    tools.removeWxPrefixes(module)
    #-----------------------------------------------------------------
    # Run the generators
    
    # Create the code generator and make the wrapper code
    wg = etgtools.getWrapperGenerator()
    wg.generate(module)
    
    # Create a documentation generator and let it do its thing
    dg = etgtools.getDocsGenerator()
    dg.generate(module)
    
#---------------------------------------------------------------------------
if __name__ == '__main__':
    run()

