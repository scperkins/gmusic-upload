#!/usr/bin/env python2.7

import os
import argparse 
from gmusicapi import Musicmanager
from getpass import getpass


#mm.perform_oauth()

def api_init():
	api = Musicmanager()
	api.login()

	return api

def main():
	
	api = api_init()

	parser = argparse.ArgumentParser(description="Upload music files to your Google Play library")
	parser.add_argument('file', type=file, help="Specifiy the filepath for the songs(s) to be uploaded")
	args = parser.parse_args()

	path = os.path.abspath(args.file.name)
	print os.path.getsize(path)
	#song_upload = api.upload(path)
	#print song_upload

if __name__ == "__main__":
	main()


