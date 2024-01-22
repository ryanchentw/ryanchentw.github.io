---
title: "Gsutil Need Pip Install Pyopenssl"
date: 2024-01-22T11:55:13+08:00
Categories:
- coding
tags:
- python
---

Need to create some signed-url links, using following command.
```
gsutil signurl -d 2d service-account-key.json gs://my-gcs-bucket/my-object
```

But the response keeps auguing
```
The signurl command requires the pyopenssl library (try pip install pyopenssl or easy_install pyopenssl)
```

Already check those variables and install pyopenssl thousand times.
```
CLOUDSDK_PYTHON=path/to/python
CLOUDSDK_PYTHON_SITEPACKAGES=1
```

After checking the source code under `platform/gsutil/gslib/commands/signurl.py`
```
try:
  from OpenSSL.crypto import FILETYPE_PEM
  from OpenSSL.crypto import load_pkcs12
  from OpenSSL.crypto import load_privatekey
  from OpenSSL.crypto import sign
  HAVE_OPENSSL = True
except ImportError:
  HAVE_OPENSSL = False
  ...
```

The `load_pkcs12` has been removed from PyOpenSSL==23.3.0, so I install the previous version and get works.
```
pip install pyopenssl==22.1.0
```


References:
- [Create Signed URLs using gsutil](https://dev.to/suavebajaj/using-gsutil-signed-url-3pnj)
