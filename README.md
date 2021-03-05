# Website Pinger

[![GitHub issues](https://img.shields.io/github/issues/Salaah01/website_pinger)](https://github.com/Salaah01/website_pinger/issues) [![GitHub forks](https://img.shields.io/github/forks/Salaah01/website_pinger)](https://github.com/Salaah01/website_pinger/network) [![GitHub stars](https://img.shields.io/github/stars/Salaah01/website_pinger)](https://github.com/Salaah01/website_pinger/stargazers)

Ping a server checking that it is alive. If it is not, then sends am email notifying the server is down.

Would recommend using this along with a cron job which would periodically run the script.

## Requirements
* Python 3

## Usage

`website_pinger.sh server_address [options]`

```bash  
  -c, --config-file Path to the config file.
  -f, --mail-from   Email from address
  -t, --mail-to     Email to address
  -i, --host        Email host
  -j, --port        Email port
  -u, --user        Email user
  -p, --password    Email password
  -s, --subject     Subject
  -a, --msg-prefix  Text to the added to the beginning of the email body.
  -z, --msg-suffix  Text to be added to the end of the email body.
```

Any parameters defined in the config file will be overwritten by any of the other optional arguments.

The config file should be a JSON file. Example is below. Do note, that not all keys need to be defined, some can be provided via the other arguments.

```json
{
  "HOST": "smtp.host",
  "PORT": 587,
  "USER": "username",
  "PASSWORD": "password",
  "TO": "email@email.com",
  "FROM": "email@email.com"
}
```

Not all keys need to exist in the the config, those which are not in the config must be at least provided as arguments when calling the script.
