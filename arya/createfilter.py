#!/usr/bin/env python
'''
Autogenerated code using arya.py
Original Object Document Input: 
{"vzFilter":{"attributes":{"dn":"uni/tn-Tenant_ARYA10/flt-SSH","name":"SSH","rn":"flt-SSH","status":"created"},"children":[{"vzEntry":{"attributes":{"dn":"uni/tn-VTenant12/flt-SSH/e-TCP-SSH","name":"TCP-SSH","etherT":"ip","prot":"tcp","dFromPort":"22","dToPort":"22","rn":"e-TCP-SSH","status":"created"},"children":[]}}]}}
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
import cobra.model.vz
from cobra.internal.codec.xmlcodec import toXMLStr

# log into an APIC and create a directory object
ls = cobra.mit.session.LoginSession('http://172.31.216.24', 'admin', 'scotch123')
md = cobra.mit.access.MoDirectory(ls)
md.login()

# the top level object on which operations will be made
polUni = cobra.model.pol.Uni('')
fvTenant = cobra.model.fv.Tenant(polUni, 'Tenant_ARYA10')

# build the request using cobra syntax
vzFilter = cobra.model.vz.Filter(fvTenant, name=u'SSH')
vzEntry = cobra.model.vz.Entry(vzFilter, name=u'TCP-SSH', prot=u'tcp', etherT=u'ip', dFromPort=u'22', dToPort=u'22')


# commit the generated code to APIC
print toXMLStr(fvTenant)
c = cobra.mit.request.ConfigRequest()
c.addMo(fvTenant)
md.commit(c)
