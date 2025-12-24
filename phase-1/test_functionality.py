#!/usr/bin/env python3
"""
Test script to verify all functionality works in a single run.
"""
import sys
import os
# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from cli.cli_interface import TodoCLI


def main():
    """Test all functionality in a single run."""
    cli = TodoCLI()
    
    print("Testing add command:")
    cli.run(['add', 'Test Task 1', 'Description for task 1'])
    
    print("\nTesting list command:")
    cli.run(['list'])
    
    print("\nTesting update command:")
    cli.run(['update', '1', 'Updated Task 1', 'Updated description'])
    
    print("\nTesting list command after update:")
    cli.run(['list'])
    
    print("\nTesting complete command:")
    cli.run(['complete', '1'])
    
    print("\nTesting list command after marking complete:")
    cli.run(['list'])
    
    print("\nTesting incomplete command:")
    cli.run(['incomplete', '1'])
    
    print("\nTesting list command after marking incomplete:")
    cli.run(['list'])
    
    print("\nTesting delete command:")
    cli.run(['delete', '1'])
    
    print("\nTesting list command after deletion:")
    cli.run(['list'])


if __name__ == "__main__":
    main()