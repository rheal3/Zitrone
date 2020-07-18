#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

import sys
import app
import quick_input

# Options
if "--help" in sys.argv:
    main_functions.help()
elif "--about" in sys.argv:
    main_functions.about()
elif "--input" in sys.argv:
    quick_input.quick_input()
else:
    app.main_code()
