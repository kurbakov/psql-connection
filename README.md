# About

Simple test to test the connection from python to PostgreSQL.

To run the script we recomment to have docker installed and start the PostgreSQL in the docker.
But it is not a ard requirement and the script should work with any setup.

To run the docker:
```bash
cd <path to the repo>
docker-compose up &
```

To stop the docker:
```bash
cd <path to the repo>
docker-compose down
```


# Run the test

1. Make sure the postgres is running
2. Make sure the connection data like user/password are set corectly
3. make sure postgres IP port and DB are set correctly
4. Run the test
```bash
cd <path to the repo>
python3 src/psql-connection.py
```

In case of success the code should print results of the quesry:
```sql
SELECT * FROM pg_catalog.pg_tables;
```

# Dependencies

To use Postgres conecction libs we need to install psql dev dependencies. For ubuntu it was:
```
sudo apt install libpq-dev
pip3 install psycopg2
```

For more information about the lib, use: https://www.psycopg.org/docs/

If you see this error, make sure you install dependencies!
```test
$ pip3 install psycopg2
Defaulting to user installation because normal site-packages is not writeable
Collecting psycopg2
  Downloading psycopg2-2.9.9.tar.gz (384 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 384.9/384.9 KB 3.4 MB/s eta 0:00:00
  Preparing metadata (setup.py) ... error
  error: subprocess-exited-with-error
  
  × python setup.py egg_info did not run successfully.
  │ exit code: 1
  ╰─> [23 lines of output]
      running egg_info
      creating /tmp/pip-pip-egg-info-x7a_fqxp/psycopg2.egg-info
      writing /tmp/pip-pip-egg-info-x7a_fqxp/psycopg2.egg-info/PKG-INFO
      writing dependency_links to /tmp/pip-pip-egg-info-x7a_fqxp/psycopg2.egg-info/dependency_links.txt
      writing top-level names to /tmp/pip-pip-egg-info-x7a_fqxp/psycopg2.egg-info/top_level.txt
      writing manifest file '/tmp/pip-pip-egg-info-x7a_fqxp/psycopg2.egg-info/SOURCES.txt'
      
      Error: pg_config executable not found.
      
      pg_config is required to build psycopg2 from source.  Please add the directory
      containing pg_config to the $PATH or specify the full executable path with the
      option:
      
          python setup.py build_ext --pg-config /path/to/pg_config build ...
      
      or with the pg_config option in 'setup.cfg'.
      
      If you prefer to avoid building psycopg2 from source, please install the PyPI
      'psycopg2-binary' package instead.
      
      For further information please check the 'doc/src/install.rst' file (also at
      <https://www.psycopg.org/docs/install.html>).
      
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
```