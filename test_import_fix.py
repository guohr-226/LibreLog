#!/usr/bin/env python3
"""
Test script to verify that the import issue is fixed.
"""

# Test the specific import that was failing
try:
    from parser.llama_parser import get_logs_from_group, verify_one_regex
    print("SUCCESS: Import from parser.llama_parser works!")
    
    # Test the api_config import specifically
    from parser.api_config import get_llm_client
    print("SUCCESS: Import from parser.api_config works!")
    
    # Test that the function works
    client = get_llm_client()
    print(f"SUCCESS: get_llm_client() returned: {client}")
    
    print("All imports work correctly. The original issue has been fixed!")
    
except ImportError as e:
    print(f"FAILED: Import error still exists: {e}")
    import traceback
    traceback.print_exc()