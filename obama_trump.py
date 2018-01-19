# obama_trump.py
# inspired by https://github.com/tyarkoni/pliers
# see also http://tyarkoni.github.io/pliers/

from pliers.extractors import GoogleVisionAPIFaceExtractor

obama_img = 'img/obama.jpg'
trump_img = 'img/trump.jpg'

ext = GoogleVisionAPIFaceExtractor()

obama = ext.transform(obama_img).to_df()
trump = ext.transform(trump_img).to_df()

print(obama['angerLikelihood'])
print(obama['joyLikelihood'])
print(trump['angerLikelihood'])
print(trump['joyLikelihood'])