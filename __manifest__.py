# -*- coding: utf-8 -*-
{
    'name': "sms payments",


    'description': """
       Sends messages from smsmasivos.com.mx
    """,

    'author': "César Gtz",
    'website': "yecora.mx",


    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        'security/sms_access.xml',
        'views/sms_views.xml',
    ],

}
