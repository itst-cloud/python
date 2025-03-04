import getpass

from fabric import Connection, Config

#pawwsord = getpass.getpass("Enter your root password: ")

#config = Config(overrides={'sudo': {'password': pawwsord}})
conn = Connection("192.168.10.207", user="itst")#, config=config)

conn.run("ls -la")

conn.run("pwd")
