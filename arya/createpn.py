#!/usr/bin/env python
'''
Autogenerated code using arya.py
Original Object Document Input: 
{"totalCount":"1","imdata":[{"fvTenant":{"attributes":{"descr":"","dn":"uni/tn-Tenant_ARYA10","name":"Tenant_ARYA10","ownerKey":"","ownerTag":""},"children":[{"fvRsTenantMonPol":{"attributes":{"tnMonEPGPolName":""}}}]}}]}
'''
#raise RuntimeError('Please review the auto generated code before ' +
 #                   'executing the output. Some placeholders will ' +
  #                  'need to be changed')

# list of packages that should be imported for this code to work
import cobra.mit.access
import cobra.mit.request
import cobra.mit.session
import cobra.model.fv
import cobra.model.pol
from cobra.internal.codec.xmlcodec import toXMLStr

# log into an APIC and create a directory object
ls = cobra.mit.session.LoginSession('http://172.31.216.24', 'admin', 'scotch123')
md = cobra.mit.access.MoDirectory(ls)
md.login()

# the top level object on which operations will be made
polUni = cobra.model.pol.Uni('')

# build the request using cobra syntax
fvTenant = cobra.model.fv.Tenant(polUni, ownerKey=u'', name=u'Tenant_ARYA10', descr=u'', ownerTag=u'')
fvRsTenantMonPol = cobra.model.fv.RsTenantMonPol(fvTenant, tnMonEPGPolName=u'')


# commit the generated code to APIC
print toXMLStr(polUni)
c = cobra.mit.request.ConfigRequest()
c.addMo(polUni)
md.commit(c)

