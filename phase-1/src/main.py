#!/usr/bin/env python3
"""
Main entry point for the CLI Todo Application.
"""

import argparse
import sys
import os
# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from cli.cli_interface import TodoCLI


def main():
    """Main function to run the CLI Todo Application."""
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()