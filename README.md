# fixsonos
Sonos at home.

using: https://soco.readthedocs.io/en/latest/

## Install

`docker run -it debian`

```
apt-get update
apt-get install -y git python3 python3-pip
pip install pipenv
```

```
cd /opt
git clone https://github.com/h1f1x/fixsonos.git
pipenv install
pipenv run python index.py
```

```
cd /opt/fixsonos
cd fixsonos.init.sh /etc/init.d/
update-rc.d fixsonos.init.sh defaults
```