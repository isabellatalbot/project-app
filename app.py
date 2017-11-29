import os

if 'PORT' in os.environ:
	app.run(host='0.0.0.0', port=int(os.environ[PORT]))
else:
	app.run(debug=True)