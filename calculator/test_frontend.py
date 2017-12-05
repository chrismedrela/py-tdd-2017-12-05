from nose2.tools import such
from unittest import mock

import frontend

with such.A('Calculator Web Frontend') as it:
    with it.having('Home Page'):
        @it.should('display the home page')
        @mock.patch('frontend.request')
        def test(request_mock):
            request_mock.method = 'GET'
            html = frontend.home()
            it.assertIn('Home Page', html)

        with it.having('addition form'):
            @it.should('display the form')
            @mock.patch('frontend.request')
            def test(request_mock):
                request_mock.method = 'GET'
                html = frontend.home()
                it.assertIn('<form', html)
                it.assertIn('name="first"', html)
                it.assertIn('name="second"', html)
            
            @it.should('delegate request parameters to backend.add')
            @mock.patch('frontend.request')
            @mock.patch('frontend.backend')
            def test(backend_mock, request_mock):
                request_mock.method = 'POST'
                request_mock.form = {
                    'first': '50',
                    'second': '70',
                }

                frontend.home()

                backend_mock.add.assert_called_once_with(50, 70)

    it.createTests(globals())