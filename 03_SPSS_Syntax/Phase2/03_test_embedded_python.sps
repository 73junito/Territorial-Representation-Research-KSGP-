* TRR-CONFIG-001.
* Diagnostic only.
* No input dataset modification.
* No output file overwrite.

BEGIN PROGRAM PYTHON3.
import sys
import spss
import spssaux

print("TRR SPSS PYTHON DIAGNOSTIC")
print("Python version:", sys.version)
print("Embedded SPSS Python: AVAILABLE")
print("SPSS module: IMPORT SUCCESS")
print("spssaux module: IMPORT SUCCESS")
END PROGRAM.