#   Copyright Matthew Copperwaite 2011
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#   See the README.txt file for contact information.
 
#!/bin/env python
import shelve
import uuid

class SimpleKeyDB:
    def __init__ (self, db_path):
        """Description: initiator for SimpleKeyDB.
           Arguments:
             db_path: str() The file the database will be stored in."""
        self.open(db_path)

    def __del__ (self):
        """Description: destruction method. Closes and saves file."""
        self.close()

    def open (self, db_path):
        """Description: opens the database file and stores it in a private object.
           Arguments:
             db_path: str() - the file the database will be stored in."""
        self._db = shelve.open(db_path)
        self._db_old = self._db;

    def save(self):
        """Description: save any changes to the database to the file."""
        self._db.sync()
        self._db_old = self._db

    def close(self, save=True):
        """Description: save and close the database."""
        if not save:
            self.revert()
        self._db.close()

    def revert(self):
        """Description: reset database to before last save."""
        self._db = self._db_old

    def add_key (self, key_name, key_value, save=True):
	"""Description: adds or updates a single key/value pair to the database.
           Arguments:
             key_name: str() - the name of the key.
             key_value: obj() - the value to associate with the key.
             save: bool() - whether to save changes to the file (default: True)"""
        self._db[key_name] = key_value
        if save:
            self.save()

    def add_keys (self, key_dict, save=True):
        """Description: similar to add_key, but for multiple entries.
           Arguments:
             key_dict: dict() - a dictionary object containing new and updated values.
             save: bool() - whether to save changes to the file (default: True)"""
        self._db.update(key_dict)
        if save:
            self.save()

    def get_key (self, key):
        """Description: returns the value for a key in the database.
           Arguments:
             key: str() - the name of the key to find the value of"""
        return self._db[key]

    def get_keys (self, keys):
        """Description: returns a dictionary containing values of keys.
           Arguments:
             keys: list() - a list of keys as str() to find the values of."""
        returnValues = {}
        for key in keys:
            returnValues[key] = self.get_key(key)
        return returnValues

    def delete_key (self, key, save=True):
        """Description: remove the key/value from the database.
           Arguments:
             key: str() - the name of the key to delete.
             save: bool() - whether to save the database to the file (default: True)"""
        del self._db[key]
        if save:
            self.save()

    def delete_keys (self, keys, save=True):
        """Description: similar to delete_key but for several keys.
           Arguments:
             keys: list() - a list of keys to delete from the database.
             save: bool() - whether to save these changes to the database (default: True)"""
        for key in keys:
            del self._db[key]
        if save:
            self.save()

    def dump (self):
        """Description: returns a copy of the database."""
        return dict(self._db)

    def generate_uuid (self):
        """Description: returns a random UUID to use for keys."""
        return str(uuid.uuid4())
