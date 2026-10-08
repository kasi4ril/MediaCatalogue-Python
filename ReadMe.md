# Media Catalogue Project

## Description
A robust, Object-Oriented Python application designed to manage a media catalogue. This project was developed as part of a Python learning exercise and demonstrates core OOP principles including class inheritance, polymorphism, custom exceptions, and input validation.

## Features
* **Media Type Management**: Dedicated `Movie` and `TVSeries` classes to handle different media structures.
* **Strict Input Validation**: Initialization rules preventing invalid data states (e.g., negative durations, empty titles).
* **Custom Error Handling**: Implements a `MediaError` class to cleanly catch and display domain-specific errors.
* **Type Filtering**: Uses strict and inheritance-aware type checking (`type()` vs `isinstance()`) to accurately categorize items during retrieval.
* **Formatted Output**: Overridden magic methods (`__str__`) for clean, human-readable console outputs.

## Usage
Simply run the Python file from your terminal. The built-in example will create a catalogue, add movies and TV series, and print out the formatted list.

```bash
python media_catalogue.py