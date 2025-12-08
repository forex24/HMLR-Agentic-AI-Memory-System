"""
Test the new HMLRClient public API
"""
import sys
sys.path.insert(0, 'hmlr')

print("=" * 60)
print("HMLR Public API Test")
print("=" * 60)

# Test 1: Import HMLRClient
print("\nTest 1: Importing HMLRClient...")
try:
    from hmlr import HMLRClient
    print("  [PASS] HMLRClient imported from package root")
except Exception as e:
    print(f"  [FAIL] HMLRClient import: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 2: Import from hmlr.client module directly  
print("\nTest 2: Importing from hmlr.client module...")
try:
    from hmlr.client import HMLRClient as DirectClient
    print("  [PASS] HMLRClient imported from hmlr.client module")
except Exception as e:
    print(f"  [FAIL] Direct import: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 3: Check __all__ export
print("\nTest 3: Checking package exports...")
try:
    import hmlr
    if "HMLRClient" in hmlr.__all__:
        print("  [PASS] HMLRClient in __all__")
    else:
        print(f"  [FAIL] HMLRClient not in __all__: {hmlr.__all__}")
        sys.exit(1)
except Exception as e:
    print(f"  [FAIL] __all__ check: {e}")
    sys.exit(1)

# Test 4: Check version
print("\nTest 4: Checking package version...")
try:
    import hmlr
    if hasattr(hmlr, '__version__'):
        print(f"  [PASS] Version: {hmlr.__version__}")
    else:
        print("  [FAIL] No __version__ attribute")
        sys.exit(1)
except Exception as e:
    print(f"  [FAIL] Version check: {e}")
    sys.exit(1)

# Test 5: Verify LangChain integration exists (but may require langchain)
print("\nTest 5: Checking LangChain integration...")
try:
    # File should exist
    import os
    langchain_path = os.path.join('hmlr', 'integrations', 'langchain.py')
    if os.path.exists(langchain_path):
        print("  [PASS] LangChain integration file exists")
        print("  [INFO] Import will fail without langchain installed (expected)")
    else:
        print(f"  [FAIL] LangChain integration file not found")
        sys.exit(1)
except Exception as e:
    print(f"  [FAIL] LangChain integration check: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("ALL PUBLIC API TESTS PASSED!")
print("=" * 60)
