# pliers-play

This repo is Rick Gilmore's playground for exploring the [`pliers`](http://tyarkoni.github.io/pliers/index.html) feature extraction package.

I run this in a clean, custom Python 2.7 environment, created using `conda create -n myenv python=2.7` under conda 4.3.30.

On my Mac OS (10.12.6), I found that I needed to manually install some package dependencies. These are listed in `pliers_dependencies.txt`.

Once those are in place, it's possible to activate the environment with `source activate myenv`, and then run the demo programs:

`obama_trump.py`
`peep_spectrum.py`
`peep_transcript.py`

using, for example, `python obama_trump.py`.

Note that I have created my own Google and IBM API keys and stored those credentials as environment variables in `~/api-keys/json` and `~/.bash_profile`. Also, these are really toy demos I'm using to learn how `pliers` works.

## Other observations

- I discovered that the speech recognition facility requires sound files in `WAV, AIFF, or FLAC` formats. The `pydub` package can be used to convert sound file formats.
- `pliers` seems to be picky about the version of `ffmpeg`. So, I add the following code to the start of any jupyter notebook cell or python script:

```
import imageio
imageio.plugins.ffmpeg.download()
```
