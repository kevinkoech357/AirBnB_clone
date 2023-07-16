# AirBnB Clone
This repository contains a clone of the AirBnB application, implemented as a command-line interface (CLI) for managing objects and data storage. It allows users to create, update, delete, and retrieve objects from various classes like users, places, bookings, and more.

## Table of Contents
* Features
* Installation
* Usage
* Contributing
* License

## Features
* Interactive command-line interface for managing objects.
* Object-oriented design with support for different classes.
* Persistent data storage using JSON files.
* CRUD operations for creating, updating, deleting, and retrieving objects.
* Extensible and modular architecture for adding new classes and functionality.
* Unit tests for ensuring code quality and correctness.

## Installation
Clone the repository
```bash
git clone https://github.com/kevinkoech357/AirBnB_clone.git
```
Navigate to the directory
```bash
cd AirBnB_clone
```
Run the console
```bash
./console.py
```
## Usage
The application provides a command-line interface for interacting with different objects and classes. Here are some example commands you can try:

To create a new user:
```bash
(hbnb) create User
```
To list all existing users:
```bash
(hbnb) all User
```
To update an attribute of a user:
```bash
(hbnb) update User 1234-5678-9012 email "test@example.com"
```
To delete a user:
```bash
(hbnb) destroy User 1234-5678-9012
```
For a complete list of available commands and usage instructions, please refer to the command documentation within the application.
