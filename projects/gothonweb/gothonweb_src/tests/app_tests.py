from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
	# check that we got a 404 on the / url
	resp = app.request("/")
	assert_response(resp, status="404")

	# test our first GET request to /hello
	resp = app.request("/hello")
	assert_response(resp)

	# make sure default vaules work for the form
	resp = app.request("/hello", method="POST")
	assert_response(resp, contains="Nobody")

	# test that we get expected values
	data = {'name':'Zee', 'greet': 'Hola' }
	resp = app.request("/hello", method="POST", data=data)
	assert_response(resp, contains="Zee")