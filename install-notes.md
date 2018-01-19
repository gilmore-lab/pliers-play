# Notes on Mac OS install 2018-01-12

- Create a separate Python 2.7 environment via `conda create --name myenv Python=2.7` and then activate it via `source activate myenv` or deactivate via `source deactivate`. See <https://conda.io/docs/user-guide/tasks/manage-environments.html>.

- Must install Google API client manually via
`pip install --upgrade google-api-python-client`

- Advisable to install optional `pliers` dependencies via `pip install -r optional-dependencies.txt`. On Mac OS 10.12.6 Sierra, this resulted in the following build failures:
	- pygraphviz, due to `pygraphviz/graphviz_wrap.c:2954:10: fatal error: 'graphviz/cgraph.h' file not found`
    - `Failed building wheel for dlib` probably because CUDA is not installed. Investigate this further here: <http://docs.nvidia.com/cuda/cuda-installation-guide-mac-os-x/index.html>. On further investigation, this particular MacBook Air does not have an NVIDIA GPU and thus is not compatible with CUDA.
    - `Command "/Users/rick/anaconda/envs/ricko/bin/python -u -c "import setuptools, tokenize;__file__='/private/var/folders/4w/c4zm1ghx0jq994mlryh37jdh0000gv/T/pip-build-37f6ng/dlib/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /var/folders/4w/c4zm1ghx0jq994mlryh37jdh0000gv/T/pip-7byNat-record/install-record.txt --single-version-externally-managed --compile" failed with error code 1 in /private/var/folders/4w/c4zm1ghx0jq994mlryh37jdh0000gv/T/pip-build-37f6ng/dlib/`

- Install api-key(s) in a good place. I chose `~/api-keys/json`.

- For some reason Terminal.app does not `source ~/.bashrc` when opening a new shell, so I had to `export GOOGLE_APPLICATION_CREDENTIALS=~/api-keys/json/google-vision-api-56d1e16c6ebc.json` manually before launching python.
On further investigation, the recommendation is to put global environment variables in `~/.bash_profile` or if these variables are in `~/.bashrc` to add ``source ~/.bashrc` to `~/.bash_profile`.
- With these caveats, I was able to get the following example from <https://github.com/tyarkoni/pliers#example-the-first>to work:

>from pliers.extractors import GoogleVisionAPIFaceExtractor
>ext = GoogleVisionAPIFaceExtractor()
>result = ext.transform('obama.jpg').to_df()

via `python demo-1.py`
