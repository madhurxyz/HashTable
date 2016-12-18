#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(self.length())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def length(self):
        """Return the length of this hash table by traversing its buckets"""

    def contains(self, key):


    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""


    def set(self, key, value):
        """Insert or update the given key with its associated value"""


    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""


    def keys(self):
        """Return a list of all keys in this hash table"""


    def values(self):
        """Return a list of all values in this hash table"""
