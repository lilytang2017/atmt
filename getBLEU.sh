python translate_beam.py --beam-size 11
./postprocess_asg4.sh model_translations.txt model_translations.out en
cat model_translations.out | sacrebleu data_asg4/raw_data/test.en
