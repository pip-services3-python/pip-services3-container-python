# -*- coding: utf-8 -*-
"""
    app.py
    ~~~~~~~~~~~~~~~~~~~~

    Dummy app run implementation

    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_components.log import ConsoleLogger
from .DummyProcess import DummyProcess

if __name__ == '__main__':
    runner = DummyProcess()
    try:
        runner.run()
    except Exception as ex:
        ConsoleLogger().fatal("dummy", ex, "Error: ")
        #print(traceback.format_exc(ex))
        #sys.stderr.write(str(e) + '\n')