# What?
A Python module that allows you to store a key/value pair database (much like [[CouchDB]]) on your local filesystem, using Python APIs. 

# API
 * __init__ -- Accepts path to database file
 * __del__ -- Closes database file when no longer being used
 * open -- Opens the database object. Shouldn't need to be used.
 * revert -- Reverts any unsaved in changes.
 * close -- Closes the document.
 * add_key -- Accepts Name string and Value as object
 * add_keys -- Same as above except you can pass in a dict
     * This function doesn't force add_key to save, it forces the save once the process is complete
 * get_key -- Accepts Key string
 * get_keys -- Same as above but accepts tuple containing Key strings and returns a dict containing values
 * delete_key -- Accepts Key string
 * delete_keys -- Same as above but accepts tuple containing Key strings
     * This function doesn't force DeleteKey to save, it forces the save once the process is complete
 * dump -- Returns the entire database

# Future
 1. More advanced key matching

# Examples
## Basic
    from simplekeydb import SimpleKeyDB

    db = SimpleKeyDB('simple.db')
    db.add_key('foo', 'bar')
    db.add_key('dictionary', {'foo': 12345})
    # changes are automatically saved unless:
    db.add_key('nosave', {'foo': [9, 8, 7, 6, 5]}, False)

More examples will be made available on my wiki.
