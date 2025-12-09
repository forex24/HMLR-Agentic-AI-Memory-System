"""
Test script to validate local HMLR installation
"""
import os

def test_basic_imports():
    """Test basic HMLR imports"""
    print("🧪 Testing HMLR local installation...")
    
    # Test imports
    print("   Testing imports...")
    from hmlr import HMLRClient
    print("   ✅ HMLRClient import successful")
    
    from hmlr.core.component_factory import ComponentFactory
    print("   ✅ ComponentFactory import successful")
    
    from hmlr.memory.storage import Storage
    print("   ✅ Storage import successful")
    
    from hmlr.core.conversation_engine import ConversationEngine
    print("   ✅ ConversationEngine import successful")
    
    print("\n✅ All imports successful!")
    print("\n📦 Package structure validated")
    print("   - HMLRClient (public API)")
    print("   - ComponentFactory (component initialization)")
    print("   - Storage (database layer)")
    print("   - ConversationEngine (core conversation logic)")
    
    print("\n🎉 Local installation test PASSED!")
    print("\nℹ️  Note: Full functional test requires OPENAI_API_KEY")
    print("   To test with real conversations:")
    print("   export OPENAI_API_KEY=your-key-here")
    print("   python -m pytest tests/test_12_hydra_e2e.py")

if __name__ == "__main__":
    test_basic_imports()

