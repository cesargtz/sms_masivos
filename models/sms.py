# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
# import requests 
import urllib, urllib2, json
from money import Money


class sms_payents(models.Model):
    _inherit = 'account.payment'
    send_message = fields.Boolean(string="Mandar mensaje", default=False, help="Seleccionar el checkbox si desea mandar mensaje de pago")

    @api.multi
    def post(self):
        if self.send_message:
            mon = Money(amount=self.amount, currency='USD')
            mensaje = 'Yecora: Se realizo su pago por la cantidad de %s, Gracias.' % (mon.format('en_US'))
            movil = self.partner_id.mobile.replace(" ", "")
            parametros = urllib.urlencode({'apikey':'bc258950888b605045cc1ee0340d48c538903715','mensaje': mensaje,'numcelular': movil,'numregion':'52'})
            headers = {"Content-type": "application/x-www-form-urlencoded", "Accept":"text/plain"}
            request = urllib2.Request('http://smsmasivos.com.mx/sms/api.envio.new.php', parametros, headers)
            opener = urllib2.build_opener()
            respuesta = opener.open(request).read()
            j=json.loads(respuesta)
            if j['estatus'] != "ok":
                raise exceptions.ValidationError("Sucedio un error: %s " % (j['mensaje']))
        return super(sms_payents, self).post()