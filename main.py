#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

import sys
import app

# Options
if "--help" in sys.argv:
    main_functions.help()
elif "--about" in sys.argv:
    main_functions.about()
else:
    app.main_code()
