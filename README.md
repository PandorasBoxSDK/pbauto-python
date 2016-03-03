# pbauto-python
This project is part of the Pandoras Box SDK. It implements an interface to access the Pandoras Box Automation.

## Requirements
* Python (tested on 3, 2 should work as well)
* coolux Pandoras Box

## Installation
The code is currently distributed as a single file. There might be a pip package in the future.

## Usage
The PBAuto class expects a connector in the constructor. Currently there is only the TCP connector.

```python
import pbauto

# Use Tcp Connector
ip = "127.0.0.1"
domain = 0

connector = Tcp(ip, domain) # domain is optional
pb = pbauto.PBAuto(connector)

# ... or use the convenience function
pb = pbauto.PBAuto.connect_tcp(ip, domain)
```

You can then proceed to use all api functions.

```python
pb.getSelectedDeviceCount()
# returns {'selectedDevicesCount': 2, 'ok': True, 'code': 81}
```

## Versioning
The version consists of a major, a minor and a revision field. (major.minor.revision)
If the major version changes, then these changes are incompatible with prior versions. Changes to the minor version indicate backwards compatibility. The revision field is reserved for the Pandoras Box revision that is required to use all features. It might be possible to use the SDK with an older revision of Pandoras Box, but not all the commands will work.

## Contributing
Most of the files in this repository are generated. Please contribute to the template files instead.
https://github.com/PandorasBoxSDK/pbauto-generator

v0.3.12086, generated on 2016-03-03