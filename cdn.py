from bottle import route, run
import os
import shutil

@route('/<content>/@<version>')
def serveContent(content, version):
	if (version == "latest"):
		contentData = "/" + content + "/" + content + "-latest/"
		archiveName = content + "-latest.zip"
		shutil.make_archive(archiveName, 'zip', contentData)
		return open(archiveName)

run(host='localhost', port=9999, debug=True)