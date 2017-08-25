#!/usr/bin/env python
import tweepy


class Twitter:
    def __init__(self):
        self._consumer_key = None
        self._consumer_secret = None
        self._access_token = None
        self._access_token_secret = None

    # Getters.
    @property
    def consumer_key(self):
        return self._consumer_key

    @property
    def consumer_secret(self):
        return self._consumer_secret

    @property
    def access_token(self):
        return self._access_token

    @property
    def access_token_secret(self):
        return self._access_token_secret

    # Setters.
    @consumer_key.setter
    def consumer_key(self, value):
        self._consumer_key = value

    @consumer_secret.setter
    def consumer_secret(self, value):
        self._consumer_secret = value

    @access_token.setter
    def access_token(self, value):
        self._access_token = value

    @access_token_secret.setter
    def access_token_secret(self, value):
        self._access_token_secret = value

    # Deleters.
    @consumer_key.deleter
    def consumer_key(self):
        del self._consumer_key

    @consumer_secret.deleter
    def consumer_secret(self):
        del self._consumer_secret

    @access_token.deleter
    def access_token(self):
        del self._access_token

    @access_token_secret.deleter
    def access_token_secret(self):
        del self._access_token_secret

    def check_config(self):
        all_config_set = True
        if self._consumer_key is None:
            all_config_set = False
        if self._consumer_secret is None:
            all_config_set = False
        if self._access_token is None:
            all_config_set = False
        if self._access_token_secret is None:
            all_config_set = False

        if all_config_set is True:
            print("All OK")
        else:
            print("Not all twitter settings set!")

